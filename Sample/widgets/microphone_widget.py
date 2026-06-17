from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt


class MicrophoneWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MicrophoneWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        label = QLabel("エコー")
        label.setFixedWidth(80)
        self.echo_slider = QSlider(Qt.Horizontal)
        self.echo_slider.setRange(0, 100)
        self.echo_slider.setValue(30)

        row = QHBoxLayout()
        row.addWidget(label)
        row.addWidget(self.echo_slider)
        layout.addLayout(row)
