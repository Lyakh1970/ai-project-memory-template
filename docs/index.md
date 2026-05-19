# Project Memory Index

This file is the map of the project memory. It should tell agents and humans where to look before loading unnecessary context.

## Core project context

- `docs/current_state.md` — current implementation and project state.
- `docs/architecture.md` — architecture overview.
- `docs/decision_log.md` — accepted decisions and their reasons.
- `docs/changelog.md` — chronological record of completed changes.
- `docs/glossary.md` — project terms, abbreviations, entities, and domain language.
- `docs/no_touch_zones.md` — sensitive areas and forbidden changes.

## Architecture decisions

- `docs/adr/` — Architecture Decision Records.

## Workflows

- `docs/workflows/chatgpt_codex_loop.md`
- `docs/workflows/review_gate.md`
- `docs/workflows/apply_template_to_existing_repo.md`

## Security

- `docs/security/secrets_and_private_data.md`
- `docs/security/external_review_bundle_policy.md`

## Operational exchange

- `.ai_workflow/index.md` — current task pointer.
- `.ai_workflow/tasks/` — tasks for Codex.
- `.ai_workflow/reports/` — Codex reports.
- `.ai_workflow/reviews/` — review requests/results.
- `.ai_workflow/decisions_pending/` — decision drafts.

## Do not load by default

List heavy/private/project-specific folders here after applying the template.

Example:

- `data/raw_exports/`
- `data/private/`
- `media/`
- `backups/`
