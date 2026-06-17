from PySide6.QtWidgets import QFrame, QVBoxLayout


class CardWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("CardWidget")
        self.setFrameShape(QFrame.StyledPanel)
        self._layout = QVBoxLayout(self)

    def add_widget(self, widget):
        self._layout.addWidget(widget)
