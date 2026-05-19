# Workflow: Apply Template to Existing Repository

Use this when adding the project memory workflow to an existing repository.

## Goal

Add the template structure without overwriting existing project files.

## Codex instruction

```text
Apply the ai-project-memory-template structure to this existing repository.

Rules:
- Do not overwrite existing files.
- If a similar file already exists, create a merge proposal instead of replacing it.
- Create only missing folders and files.
- Preserve existing README, docs, code, tests, and project structure.
- Add .ai_workflow/ with README.md, index.md, tasks/, reports/, reviews/, decisions_pending/.
- Add AGENTS.md only if missing. If AGENTS.md exists, create AGENTS.template_merge_proposal.md.
- Add docs/current_state.md, docs/decision_log.md, docs/no_touch_zones.md only if missing.
- Add a report to .ai_workflow/reports/ describing what was added and what was skipped.
```

## After applying

Human should review:

- `AGENTS.md`
- `.ai_workflow/README.md`
- `.ai_workflow/index.md`
- `docs/no_touch_zones.md`
- generated report
