---
name: calendar-check
description: Read the calendar and report what is scheduled. Use when the user asks about their day, their next meeting, whether a time is free, or what is coming up.
license: GPL-3.0-or-later
---

# Calendar

## Tools

| Task | Call |
|---|---|
| Upcoming events | `shesh-calendar-mcp` → `upcoming_events` |
| Search | `shesh-calendar-mcp` → `search_calendar` |
| List calendars | `shesh-calendar-mcp` → `list_calendars` |
| Sync state | `shesh-calendar-mcp` → `calendar_status` |

## Procedure

1. Check `calendar_status` before reporting a free slot. Stale data produces a
   wrong answer with full confidence.
2. Report times in the user's local timezone with the timezone named if it is
   ambiguous.
3. Give the next event and the gap before it, not a raw dump.

## Rules

- This skill is read-only. Creating, moving, or cancelling an event is not
  supported; say so rather than pretending.
- If the calendar has not synced recently, state the sync time alongside the
  answer.
- Event titles can be sensitive. Do not repeat them into a channel the user did
  not ask for.
