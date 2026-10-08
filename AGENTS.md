# Agent Guidelines

## Project

This project is a class-based Python application for creating Sudoku puzzles,
with the eventual goal of distributing it as a standalone executable.

## Working Approach

- Read existing code and project configuration before making changes.
- Keep changes focused on the requested task and follow established conventions.
- Prefer simple, readable solutions over speculative abstractions.
- Do not add dependencies or choose a UI framework without discussing the options
  with the user first. Once a choice is agreed, use it consistently.
- Update documentation when setup instructions or application behavior changes.

## Class Design

- Give each class a clear responsibility and keep methods focused.
- Use classes for related state and behavior; use functions for stateless helpers.
- Prefer composition over deep inheritance hierarchies.
- Pass dependencies explicitly rather than relying on global mutable state.
- Use dataclasses for simple data containers where appropriate.
- Keep constructors lightweight; avoid starting the UI or performing file I/O in
  constructors unless required by the selected framework.

## Application Structure

- Separate puzzle models and rules from UI, persistence, and export code.
- Keep Sudoku validation and generation logic independent of the UI framework so
  it can be tested without opening a window.
- Keep UI callbacks small and delegate application logic to dedicated classes.
- Use a clear application entry point and an `if __name__ == "__main__":` guard
  where appropriate. Importing modules should not launch the application.
- Introduce modules and packages as needed; do not create empty architectural
  layers in advance.

## Python Conventions

- Follow PEP 8 and any formatter or linter settings already in the repository.
- Use `PascalCase` for classes, `snake_case` for functions, methods, and variables,
  and `UPPER_SNAKE_CASE` for constants.
- Add type hints to public interfaces and nontrivial functions.
- Write concise docstrings for public classes and methods when their purpose or
  contract is not obvious.
- Use `pathlib.Path` for filesystem paths and context managers for resources.
- Catch specific exceptions, provide useful error messages, and do not silently
  suppress failures.
- Use the standard `logging` module for diagnostic output.
- Never hard-code secrets, machine-specific paths, or user-specific settings.

## Tests and Verification

- Follow the existing test tooling; if none is configured, prefer `unittest`
  from the standard library until another choice is agreed.
- Test meaningful behavior, especially Sudoku rules, invalid inputs, and puzzle
  serialization round trips as those features are implemented.
- Keep core logic tests independent of UI windows, network access, and user files.
- Run checks relevant to the change and report the results. If a check could not
  run, state that clearly rather than claiming success.

## Dependencies and Distribution

- Use a project-local virtual environment and record dependencies in the chosen
  project configuration; do not commit the environment itself.
- Keep application resources separate from generated output and resolve their
  paths deliberately so packaged builds can locate them.
- Choose packaging tooling when distribution work begins, and document build
  commands and supported operating systems.
- Do not commit build artifacts, caches, secrets, or generated executables.
