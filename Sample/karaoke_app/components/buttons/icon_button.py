from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon


class IconButton(QPushButton):
    def __init__(self, icon: QIcon = None, tooltip: str = "", parent=None):
        super().__init__(parent)
        if icon:
            self.setIcon(icon)
        self.setToolTip(tooltip)
        self.setObjectName("IconButton")
