from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from b import SearchWidget
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Karaoke App")
        self.resize(480, 800)

        self.setCentralWidget(SearchWidget())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())