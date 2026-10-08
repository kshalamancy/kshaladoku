"""Launch the Kshaladoku desktop application."""

import sys

from PySide6.QtWidgets import QApplication

from kshaladoku.main_window import MainWindow


def main() -> int:
    """Create the application and run its event loop."""
    app = QApplication(sys.argv)
    app.setApplicationName("Kshaladoku")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
