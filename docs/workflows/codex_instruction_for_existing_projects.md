# Codex Instruction: Apply Project Memory Workflow to Existing Project

Use this prompt when asking Codex to add the template workflow to an existing repository.

```text
You are working in an existing repository.
Your task is to add the project-memory AI workflow structure based on ai-project-memory-template.

Critical rules:
- Do not overwrite existing files.
- Do not modify working application code.
- Do not change project behavior.
- Do not add secrets or private data.
- If a file already exists with similar purpose, create a merge proposal instead of replacing it.

Create missing structure:
- AGENTS.md, only if missing
- docs/index.md, only if missing
- docs/current_state.md, only if missing
- docs/architecture.md, only if missing
- docs/decision_log.md, only if missing
- docs/changelog.md, only if missing
- docs/glossary.md, only if missing
- docs/no_touch_zones.md, only if missing
- docs/adr/ADR-0000-template.md, only if missing
- .ai_workflow/README.md
- .ai_workflow/index.md
- .ai_workflow/tasks/active/
- .ai_workflow/tasks/done/
- .ai_workflow/tasks/rejected/
- .ai_workflow/tasks/blocked/
- .ai_workflow/reports/
- .ai_workflow/reviews/
- .ai_workflow/decisions_pending/
- docs/templates/task_template.md
- docs/templates/codex_report_template.md
- docs/templates/review_request_template.md

After adding files, create a report:
- .ai_workflow/reports/YYYY-MM-DD_000_apply_template_report.md

The report must include:
1. Files created
2. Files skipped because they already existed
3. Merge proposals created
4. Any risks or open questions
5. Recommended next step
```
