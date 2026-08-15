"""Validate every skill against the Agent Skills specification.

The spec (https://agentskills.io, as published by Anthropic) requires each skill
to be a directory containing SKILL.md with YAML frontmatter carrying `name` and
`description`. `name` must be kebab-case, at most 64 characters, and match the
directory name. Optional fields are `license`, `compatibility`, `metadata`, and
`allowed-tools`; a spec-compliant packager rejects unknown keys.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

SKILLS_DIR = Path(__file__).resolve().parents[1] / "skills"

# Fields the Agent Skills spec permits in SKILL.md frontmatter. Claude Code
# accepts further fields, but they fail upload to claude.ai, so portable skills
# stay within this set.
ALLOWED_KEYS = {"name", "description", "license", "compatibility",
                "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = {"anthropic", "claude"}


def skill_dirs():
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.S)
    assert m, f"{path}: missing YAML frontmatter delimited by ---"
    meta = {}
    for line in m.group(1).split("\n"):
        if not line.strip() or line.startswith(("#", " ", "\t", "-")):
            continue
        assert ":" in line, f"{path}: malformed frontmatter line: {line!r}"
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, m.group(2)


def test_skills_directory_is_not_empty():
    assert skill_dirs(), "no skill directories found"


@pytest.mark.parametrize("d", skill_dirs(), ids=lambda p: p.name)
def test_skill_layout(d: Path):
    """Each skill is a directory containing SKILL.md."""
    skill = d / "SKILL.md"
    assert skill.is_file(), f"{d.name}: expected {d.name}/SKILL.md"
    stray = [p.name for p in d.glob("*.md") if p.name != "SKILL.md"]
    assert not stray, f"{d.name}: unexpected markdown beside SKILL.md: {stray}"


@pytest.mark.parametrize("d", skill_dirs(), ids=lambda p: p.name)
def test_frontmatter_is_spec_compliant(d: Path):
    meta, body = parse_frontmatter(d / "SKILL.md")

    unknown = set(meta) - ALLOWED_KEYS
    assert not unknown, f"{d.name}: keys outside the spec: {sorted(unknown)}"

    assert "name" in meta, f"{d.name}: 'name' is required"
    assert "description" in meta, f"{d.name}: 'description' is required"

    name = meta["name"]
    assert name == d.name, f"{d.name}: name {name!r} must match the directory"
    assert len(name) <= 64, f"{d.name}: name exceeds 64 characters"
    assert NAME_RE.fullmatch(name), f"{d.name}: name must be kebab-case"
    assert name.lower() not in RESERVED, f"{d.name}: reserved name"
    assert "<" not in name and ">" not in name, f"{d.name}: name contains XML tags"

    desc = meta["description"]
    assert desc, f"{d.name}: description must not be empty"
    assert len(desc) <= 1024, f"{d.name}: description exceeds 1024 characters"
    assert "<" not in desc and ">" not in desc, f"{d.name}: description contains XML tags"

    assert body.strip(), f"{d.name}: SKILL.md body is empty"


@pytest.mark.parametrize("d", skill_dirs(), ids=lambda p: p.name)
def test_description_states_what_and_when(d: Path):
    """The description is the only text an agent sees before loading a skill.

    It must say both what the skill does and when to apply it, or routing fails.
    """
    meta, _ = parse_frontmatter(d / "SKILL.md")
    desc = meta["description"].lower()
    assert len(desc) >= 40, f"{d.name}: description too terse to route on"
    assert any(k in desc for k in ("use when", "always active", "use for")), (
        f"{d.name}: description must state when to use the skill"
    )


@pytest.mark.parametrize("d", skill_dirs(), ids=lambda p: p.name)
def test_body_is_within_recommended_length(d: Path):
    """Anthropic recommends the body stay under 500 lines."""
    _, body = parse_frontmatter(d / "SKILL.md")
    assert len(body.splitlines()) < 500, f"{d.name}: body exceeds 500 lines"


def test_safety_skill_grants_no_tools():
    """The safety layer must not carry an allowed-tools grant.

    `allowed-tools` is a PRE-APPROVAL: it lets the agent use those tools without
    prompting. It is not a sandbox and removes no capability. Granting the
    always-active safety skill any tool would therefore *widen* the permission
    surface of every session, which is the opposite of what this skill is for.

    Restriction is `disallowed-tools` (Claude Code) or, portably, the policy
    engine in shesh-audit. Enforcement never lives in this file.
    """
    meta, _ = parse_frontmatter(SKILLS_DIR / "safety-governance" / "SKILL.md")
    assert "allowed-tools" not in meta, (
        "safety-governance must not pre-approve tools; allowed-tools grants "
        "permission, it does not restrict it"
    )


def test_safety_skill_declares_its_enforcement_dependency():
    """A skill cannot enforce itself. It must say what does."""
    meta, _ = parse_frontmatter(SKILLS_DIR / "safety-governance" / "SKILL.md")
    compat = meta.get("compatibility", "")
    assert "shesh-audit" in compat, (
        "safety-governance must declare that enforcement depends on the "
        "policy engine, so nobody mistakes advisory text for a control"
    )


@pytest.mark.parametrize("d", skill_dirs(), ids=lambda p: p.name)
def test_allowed_tools_are_minimal(d: Path):
    """A grant must be justified by the skill's own body.

    Because `allowed-tools` widens permissions, every entry is a decision.
    Nothing may pre-approve a blanket shell.
    """
    meta, _ = parse_frontmatter(d / "SKILL.md")
    tools = meta.get("allowed-tools", "")
    assert "Bash\n" not in tools + "\n" or "Bash(" in tools, (
        f"{d.name}: bare Bash pre-approves every command; scope it as Bash(cmd:*)"
    )


# ---- loader behaviour ------------------------------------------------------

def test_discover_finds_every_shipped_skill():
    from shesh_skills import skills as lib
    names = {s.name for s in lib.discover(SKILLS_DIR)}
    assert names == {d.name for d in skill_dirs()}


def test_body_is_read_lazily(tmp_path):
    """Listing skills must not read bodies; that is the point of disclosure."""
    from shesh_skills import skills as lib
    d = tmp_path / "demo"
    d.mkdir()
    (d / "SKILL.md").write_text(
        "---\nname: demo\ndescription: A demo skill. Use when testing.\n---\n\nBody text.\n"
    )
    s = lib.get("demo", tmp_path)
    assert s is not None and s.description.startswith("A demo skill")
    assert "Body text." not in s.as_dict()          # metadata only
    assert "Body text." in s.as_dict(include_body=True)["body"]


def test_invalid_skill_is_skipped_not_fatal(tmp_path):
    good = tmp_path / "good"
    good.mkdir()
    (good / "SKILL.md").write_text(
        "---\nname: good\ndescription: Fine. Use when testing.\n---\n\nok\n"
    )
    bad = tmp_path / "bad"
    bad.mkdir()
    (bad / "SKILL.md").write_text("no frontmatter here\n")

    from shesh_skills import skills as lib
    names = {s.name for s in lib.discover(tmp_path)}
    assert names == {"good"}, "one malformed skill must not hide the others"


def test_name_must_match_directory(tmp_path):
    from shesh_skills import skills as lib
    d = tmp_path / "alpha"
    d.mkdir()
    (d / "SKILL.md").write_text(
        "---\nname: beta\ndescription: Mismatched. Use when testing.\n---\n\nx\n"
    )
    with pytest.raises(lib.SkillError, match="does not match directory"):
        lib.load_skill(d)


def test_allowed_tools_parsed_from_space_delimited_list():
    from shesh_skills import skills as lib
    s = lib.get("coding", SKILLS_DIR)
    assert s is not None
    assert "Read" in s.allowed_tools and "Grep" in s.allowed_tools


def test_skill_without_allowed_tools_grants_nothing():
    """Absent allowed-tools means no pre-approval, not unrestricted access."""
    from shesh_skills import skills as lib
    s = lib.get("safety-governance", SKILLS_DIR)
    assert s is not None
    assert s.allowed_tools == ()
