from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt


class HeaderWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HeaderWidget")
        self.setFixedHeight(60)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 0, 20, 0)

        title = QLabel("カラオケAPP")
        title.setObjectName("AppTitle")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
