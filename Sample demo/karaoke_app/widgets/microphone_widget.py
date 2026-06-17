"""
MicrophoneWidget

マイクのエコー(リバーブ)量を調整する画面。
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QSlider, QWidget


class MicrophoneWidget(QWidget):
    """マイク設定画面。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MicrophoneWidget")

        layout = QFormLayout(self)
        self.echo_slider = QSlider(Qt.Orientation.Horizontal)
        layout.addRow("エコー", self.echo_slider)
