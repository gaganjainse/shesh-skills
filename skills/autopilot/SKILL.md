---
name: autopilot
description: Make safe unattended progress on the backlog. Use when asked to continue work autonomously or work through the task list without supervision.
license: GPL-3.0-or-later
allowed-tools: Read Grep Glob Edit Write Bash(git:*) Bash(make check:*) Bash(pytest:*)
---

# Autopilot

Unattended work removes the human check on every step. The rules below replace it.

## Loop

1. **Read the backlog** and take the highest-priority item that is fully
   specified. If it is ambiguous, stop and ask rather than guessing.
2. **Branch** as `feat/<item>`. Never work directly on `main`.
3. **Implement** the smallest change that completes the item.
4. **Test.** Run the gate. A red gate ends the loop; do not push and do not
   "fix" the test to make it pass.
5. **Commit** with a Conventional Commit message.
6. **Record** what changed and move to the next item.

## Stop immediately when

- The gate fails and the cause is not obvious.
- The task needs a credential, a purchase, or an irreversible action.
- The task requires deleting data or rewriting history.
- You have looped three times without landing a change.
- Something looks wrong in a way the backlog did not anticipate.

Stopping and reporting is a success. Guessing is not.

## Never

- Push to `main`, force-push, or merge your own work unreviewed.
- Weaken a test, a gate, or a policy rule to make progress.
- Report an item complete without verifying it.
