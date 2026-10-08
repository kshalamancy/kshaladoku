"""The application's main desktop window."""

from PySide6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):
    """Provide the blank workspace for the future puzzle editor."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Kshaladoku")
        self.resize(1000, 720)
        self.setMinimumSize(640, 480)
        self.setCentralWidget(QWidget(self))
