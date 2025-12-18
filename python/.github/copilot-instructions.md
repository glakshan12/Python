Purpose
This repository is a collection of small, self-contained Python example scripts and exercises (no build system, no tests). The goal for AI coding agents: make safe, minimal edits that preserve the learning value of single-file examples and avoid breaking the repo's informal structure.

Quick repo overview
- Structure: many top-level example files and topic folders (Array/, Function/, Lists/, strings/, Tuples/, recursion/, problems/, patterns/, Typehint/). See examples like [Function/functions.py](Function/functions.py#L1) and [Array/numpyarray.py](Array/numpyarray.py#L1).
- Style: each file is typically an executable script demonstrating a concept rather than a package module. Many filenames include spaces (e.g., `Type conversion.py`) — avoid turning these into importable modules without renaming.
- Dependencies: most examples use only the standard library. Notable exception: [Array/numpyarray.py](Array/numpyarray.py#L1) which uses `numpy`.

What to do and what to avoid
- Run scripts directly: prefer `python path/to/script.py` when validating changes — do not assume a test harness exists.
- Preserve single-file examples: keep changes minimal and pedagogical; when refactoring, keep the original script runnable as a script and include a small example invocation at the bottom if appropriate.
- Avoid renaming files with spaces unless explicitly instructed — renames break users' local workflows and imports.
- If you add shared utilities, put them into a new `lib/` or `utils/` folder and update a short README describing usage.

Developer workflows (concrete commands)
- Create a venv (recommended):
  - PowerShell: `python -m venv .venv` then `.
.venv\\Scripts\\Activate.ps1`
  - Install numpy if needed: `pip install numpy`
- Run examples: `python Lists/Practice.py` or `python Function/functions.py`

Patterns and project-specific conventions
- Single-purpose scripts: most files illustrate one concept (e.g., [recursion/recursive.py](recursion/recursive.py#L1)). Keep functions small and focused.
- Naming: filenames vary widely (spaces, mixed case). When creating new files, prefer lower_snake_case without spaces.
- Minimal dependencies: assume standard library only; explicitly document third-party needs (e.g., `numpy`) in a short `requirements.txt` if you add more.

Integration points & external dependencies
- There are no web services, CI configs, or packaging targets discovered. Treat this as an examples-only repo.
- If adding external deps, modify or add `requirements.txt` at repo root and mention install steps in this file.

Examples of safe edits
- Fixing a bug inside `strings/methods.py`: update only that function and run the script to confirm output.
- Converting a long example into a small reusable function: keep the original example runnable and add a new helper in `utils/` if reused by multiple files.

When to escalate to the human maintainer
- Large refactors (renaming files, introducing packages, adding CI) — ask before proceeding.
- Changes that alter the pedagogical intent of an example — explain why and get approval.

Contact & iteration
After making changes, open a short PR description that explains the pedagogical benefit and lists the files you changed. Ask reviewers whether they prefer file renames when you propose them.

If anything in these instructions is unclear or too terse, tell me which areas you'd like expanded (examples, commands, or file references) and I'll iterate.
