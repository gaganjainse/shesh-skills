---
name: sandbox-run
description: Run an untrusted command inside a rootless container with no network. Use when executing code from the internet, testing something risky, or when the user asks to run something safely or in isolation.
license: GPL-3.0-or-later
---

# Sandboxed execution

## Tools

| Task | Call |
|---|---|
| Run isolated | `shesh-containers-mcp` → `run_sandboxed(argv)` |
| List images | `shesh-containers-mcp` → `list_container_images` |
| Pull an image | `shesh-containers-mcp` → `pull_image` |

## Defaults

Containers run rootless, with `--network=none`, `--cap-drop=ALL`, and are
removed on exit.

## When to use this

- Code from a web page, a paste, or an unreviewed repository.
- Anything the user calls untrusted.
- A command whose behaviour cannot be predicted from reading it.

## Rules

- **Never relax the defaults to make something work.** If a command needs the
  network, say so and let the user decide; do not enable it silently.
- Never mount the home directory. Mount the narrowest path needed.
- Never pass a credential into a sandbox.
- Report the exit status and output honestly, including failures.
