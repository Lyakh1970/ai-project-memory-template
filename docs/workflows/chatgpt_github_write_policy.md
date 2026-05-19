# ChatGPT GitHub Write Policy

This policy defines how ChatGPT should write workflow files to GitHub when repository access is available.

## Allowed by default after human approval

ChatGPT may create or update:

- `.ai_workflow/tasks/active/*.md`
- `.ai_workflow/index.md`
- `.ai_workflow/reviews/*.md`
- `.ai_workflow/decisions_pending/*.md`
- `docs/decision_log.md` only when human explicitly approves the decision text
- `docs/adr/*.md` only when human explicitly approves the ADR text

## Not allowed without separate explicit permission

ChatGPT must not modify:

- application source code
- database migrations
- production configuration
- secret/config files
- CI/CD deployment workflows
- accepted ADRs
- old reports or historical logs

## Recommended branch policy

For important repositories, ChatGPT should write to a workflow branch or create a PR instead of writing directly to `main`.

Suggested branch names:

- `ai-workflow/tasks`
- `ai-workflow/YYYY-MM-DD-NNN-short-title`
