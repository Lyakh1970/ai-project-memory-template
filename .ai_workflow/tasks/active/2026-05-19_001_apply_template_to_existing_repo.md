# Task 2026-05-19_001 — Apply project memory template to an existing repository

Status: approved_for_codex
Author: ChatGPT
Human reviewer: Mikhail Liakh
Task type: template application / repository scaffolding
Risk level: medium

## Goal

Apply the `ai-project-memory-template` structure to an existing working repository so that ChatGPT, Codex, and the Human reviewer can use a shared `.ai_workflow/` and project memory process.

This task is intended to be copied or adapted into a target working repository such as `world_support`, `BEAR_DOCS_HOUND`, `bear_outlook`, or another project repository.

## Core principle

Working project repository = source of truth.
Template repository = source of structure only.

After the template structure is applied, the target repository must maintain its own project-specific `AGENTS.md`, `docs/`, and `.ai_workflow/` files. The target repository must not depend on reading this template repository during normal work.

## Required reading in the target repository

Before making changes in the target repository, Codex must inspect:

1. existing `README.md`, if present;
2. existing `AGENTS.md`, if present;
3. existing `docs/`, if present;
4. existing `.github/`, if present;
5. existing project layout and language/tooling;
6. `.gitignore` and any obvious private-data folders.

## Scope

Codex may:

- create missing project memory files and folders;
- create `.ai_workflow/README.md` and `.ai_workflow/index.md`;
- create `.ai_workflow/tasks/active/`, `.ai_workflow/tasks/done/`, `.ai_workflow/tasks/rejected/`, `.ai_workflow/tasks/blocked/` using `.gitkeep` files if needed;
- create `.ai_workflow/reports/`, `.ai_workflow/reviews/`, `.ai_workflow/decisions_pending/` using `.gitkeep` files if needed;
- add or update `AGENTS.md` only if safe;
- create `docs/current_state.md`, `docs/architecture.md`, `docs/decision_log.md`, `docs/changelog.md`, `docs/glossary.md`, `docs/no_touch_zones.md`, and `docs/adr/` if missing;
- create templates under `docs/templates/` if missing;
- create or update a repository-specific report describing what was added and what was not changed.

## Out of scope

Codex must not:

- overwrite existing project-specific files without explicit approval;
- rewrite working code;
- change application behavior;
- refactor source files;
- add dependencies;
- move private data;
- copy raw exports, production dumps, media, credentials, tokens, cookies, or authentication state files;
- assume project facts that are not present in the repository.

## Merge behavior

If a target file already exists:

1. Do not overwrite it.
2. Compare it conceptually with the template purpose.
3. If safe, append a small compatible section.
4. If not clearly safe, create a merge proposal in `.ai_workflow/reviews/` instead of editing the file.

Especially careful files:

- `README.md`
- `AGENTS.md`
- `.gitignore`
- `.github/pull_request_template.md`
- existing documentation under `docs/`

## Required files/folders to ensure

```text
AGENTS.md
.ai_workflow/
  README.md
  index.md
  tasks/
    active/.gitkeep
    done/.gitkeep
    rejected/.gitkeep
    blocked/.gitkeep
  reports/.gitkeep
  reviews/.gitkeep
  decisions_pending/.gitkeep
docs/
  index.md
  current_state.md
  architecture.md
  decision_log.md
  changelog.md
  glossary.md
  no_touch_zones.md
  adr/.gitkeep
  templates/
    task_template.md
    codex_report_template.md
    gpt_review_request_template.md
    decision_proposal_template.md
    adr_template.md
  workflows/
    chatgpt_codex_loop.md
    apply_template_to_existing_repo.md
  security/
    data_safety_rules.md
```

## Required customization

Codex must adapt placeholders to the target repository only when facts are obvious from existing files.

If facts are not obvious, leave `TODO` markers instead of inventing details.

Examples:

```text
TODO: Fill project purpose.
TODO: Define no-touch zones.
TODO: Document current architecture.
```

## Required report

After completing the task, Codex must create:

```text
.ai_workflow/reports/2026-05-19_001_apply_template_report.md
```

The report must include:

1. Summary
2. Files created
3. Files updated
4. Files intentionally not changed
5. Existing files requiring human review
6. Safety concerns found
7. Recommended next task

## Definition of done

The task is complete only if:

- required workflow folders exist in the target repository;
- existing project-specific files were not overwritten;
- any conflicts or uncertainties are documented;
- no secrets or raw private data were copied;
- a report was created in `.ai_workflow/reports/`;
- `.ai_workflow/index.md` points either to the next approved task or explicitly says that no approved task is active.

## Suggested Codex launch prompt

```text
Read AGENTS.md first.
Then execute the current approved task from .ai_workflow/index.md.
Apply the project memory template structure to this repository without overwriting existing project-specific files.
If a file already exists and the safe merge is not obvious, create a review request instead of editing it.
When done, write the required report to .ai_workflow/reports/.
```
