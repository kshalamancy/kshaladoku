# Kshaladoku

A class-based Python desktop application for setting Sudoku puzzles, using
PySide6 (Qt Widgets). The initial skeleton opens a blank, resizable window.

## Setup and run (Windows PowerShell)

Use Python 3.10 or newer with a compatible PySide6 wheel. From the project root:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

If `.venv` already exists, skip the first command. Activation is not required.

## Structure

- `main.py`: application setup and event loop; importing it does not launch a UI.
- `kshaladoku/main_window.py`: the `MainWindow` class and its blank workspace.
- `requirements.txt`: runtime dependencies.

Puzzle models and constraint logic will be independent of the UI. Planned
features include a global library of reusable constraint definitions, enabling
constraints for a puzzle, and placing instances such as lines on selected cells.
These features are not implemented yet.

The startup structure follows the [Qt Widgets tutorial](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgets.html).

## Optional Windows executable

With PyInstaller installed in the virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install pyinstaller
.\.venv\Scripts\python.exe -m PyInstaller --windowed --onedir --name Kshaladoku main.py
```

Launch `dist\Kshaladoku\Kshaladoku.exe`. Distribute the entire
`dist\Kshaladoku` folder, including its supporting files. Recipients do not need
Python installed. Build on Windows for Windows; other platforms need their own
builds. See the [PyInstaller documentation](https://pyinstaller.org/en/stable/).
