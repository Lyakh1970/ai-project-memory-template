# Runbook: Create a New Codex Task

1. Discuss the task with ChatGPT.
2. Ask ChatGPT to create a structured task file.
3. Review the task as human owner.
4. If accepted, set:

```text
Status: approved_for_codex
```

5. Save it under:

```text
.ai_workflow/tasks/active/YYYY-MM-DD_NNN_short_title.md
```

6. Update `.ai_workflow/index.md` to point to it.
7. Run Codex with the standard launch prompt.
8. Review Codex report.
