"""
VolumeWidget

メイン音量・ミュージック音量・マイク音量の調整、ミュート切り替えを行う。
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout, QSlider, QWidget

from karaoke_app.components.buttons.icon_button import IconButton


class VolumeWidget(QWidget):
    """音量調整画面。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("VolumeWidget")

        layout = QFormLayout(self)

        self.main_volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.music_volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.mic_volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.mute_button = IconButton(tooltip="ミュート")

        layout.addRow("メイン音量", self.main_volume_slider)
        layout.addRow("ミュージック音量", self.music_volume_slider)
        layout.addRow("マイク音量", self.mic_volume_slider)
        layout.addRow("", self.mute_button)
