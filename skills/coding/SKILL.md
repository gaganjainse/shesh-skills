---
name: coding
description: Write, test, and refactor code safely. Use when asked to implement a feature, fix a bug, refactor, or review a diff. Enforces read-before-edit, running tests, and never pushing unreviewed work.
license: GPL-3.0-or-later
allowed-tools: Read Grep Glob Edit Write Bash(git status:*) Bash(git diff:*) Bash(git log:*) Bash(pytest:*) Bash(cargo test:*) Bash(ruff:*)
---

# Coding

1. **Understand first.** Read the files involved. Check `git_status` and
   `git_log` for context.
2. **State the plan** before editing anything non-trivial: which files, what
   approach.
3. **Match the house style.** Rust: `cargo fmt` and `clippy`. Python: `ruff`.
   Lua: `stylua`. QML: `qmlformat`. Shell: `shellcheck` and `shfmt`.
4. **Small steps.** One logical change per commit, with a Conventional Commit
   message.
5. **Test.** Run the component's suite. Add a test covering the fix.
6. **Prefer the standard library.** Justify every new dependency and check its
   licence is compatible with GPL-3.0.

## Never

- Force-push to `main`.
- `rm -rf` a path built by string concatenation.
- Use `sudo` unless explicitly asked.
- Commit a credential, a token, or a `.env` file.
- Report a test as passing without running it.
