"""Discovery and loading of Agent Skills.

Implements the progressive disclosure model from the Agent Skills
specification: only each skill's name and description are cheap to list, and
the full SKILL.md body is read on demand when a skill is selected.

Skills are resolved from, in order of precedence:
  1. $SHESH_SKILLS_DIR
  2. $XDG_DATA_HOME/shesh/skills (user-installed)
  3. the skills/ directory shipped with this package
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", re.S)
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

MAX_NAME = 64
MAX_DESCRIPTION = 1024


@dataclass(frozen=True)
class Skill:
    """A skill as declared by its SKILL.md."""

    name: str
    description: str
    path: Path
    license: str | None = None
    allowed_tools: tuple[str, ...] = ()

    def body(self) -> str:
        """Read the instruction body. Deferred until the skill is selected."""
        _meta, body = _parse(self.path.read_text(encoding="utf-8"), self.path)
        return body.strip()

    def as_dict(self, include_body: bool = False) -> dict:
        d = {
            "name": self.name,
            "description": self.description,
            "license": self.license,
            "allowed_tools": list(self.allowed_tools),
        }
        if include_body:
            d["body"] = self.body()
        return d


class SkillError(ValueError):
    """A SKILL.md that does not satisfy the specification."""


def _parse(text: str, path: Path) -> tuple[dict, str]:
    m = FRONTMATTER.match(text)
    if not m:
        raise SkillError(f"{path}: missing YAML frontmatter")
    meta: dict[str, str] = {}
    for line in m.group(1).split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, m.group(2)


def search_paths() -> list[Path]:
    """Directories searched for skills, in order of precedence."""
    paths: list[Path] = []
    env = os.environ.get("SHESH_SKILLS_DIR")
    if env:
        paths.append(Path(env).expanduser())
    xdg = os.environ.get("XDG_DATA_HOME") or "~/.local/share"
    paths.append(Path(xdg).expanduser() / "shesh" / "skills")
    paths.append(Path(__file__).resolve().parents[2] / "skills")
    return paths


def load_skill(directory: Path) -> Skill:
    """Load and validate one skill directory."""
    skill_file = directory / "SKILL.md"
    if not skill_file.is_file():
        raise SkillError(f"{directory}: no SKILL.md")

    meta, body = _parse(skill_file.read_text(encoding="utf-8"), skill_file)

    name = meta.get("name") or directory.name
    if name != directory.name:
        raise SkillError(f"{skill_file}: name {name!r} does not match directory")
    if len(name) > MAX_NAME or not NAME_RE.fullmatch(name):
        raise SkillError(f"{skill_file}: name must be kebab-case, <= {MAX_NAME} chars")

    description = meta.get("description", "").strip()
    if not description:
        raise SkillError(f"{skill_file}: description is required")
    if len(description) > MAX_DESCRIPTION:
        raise SkillError(f"{skill_file}: description exceeds {MAX_DESCRIPTION} chars")
    if not body.strip():
        raise SkillError(f"{skill_file}: body is empty")

    raw_tools = meta.get("allowed-tools", "")
    tools = tuple(t for t in re.split(r"[,\s]+", raw_tools) if t)

    return Skill(
        name=name,
        description=description,
        path=skill_file,
        license=meta.get("license"),
        allowed_tools=tools,
    )


def discover(root: Path | None = None) -> list[Skill]:
    """Return every valid skill, nearest search path winning on name collision.

    An invalid skill is skipped rather than raising, so one malformed directory
    cannot make every other skill unavailable.
    """
    roots = [root] if root is not None else search_paths()
    found: dict[str, Skill] = {}
    for r in roots:
        if not r or not r.is_dir():
            continue
        for d in sorted(p for p in r.iterdir() if p.is_dir()):
            try:
                skill = load_skill(d)
            except SkillError:
                continue
            found.setdefault(skill.name, skill)
    return sorted(found.values(), key=lambda s: s.name)


def get(name: str, root: Path | None = None) -> Skill | None:
    for s in discover(root):
        if s.name == name:
            return s
    return None
