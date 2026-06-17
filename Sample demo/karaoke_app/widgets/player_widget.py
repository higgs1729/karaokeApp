"""
PlayerWidget

再生・一時停止・停止・歌いなおし・シークバー・再生時間表示を行う。
"""
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSlider, QVBoxLayout, QWidget

from karaoke_app.components.buttons.icon_button import IconButton
from karaoke_app.controllers.player_controller import PlayerController


class PlayerWidget(QWidget):
    """再生コントロール画面。"""

    def __init__(self, controller: Optional[PlayerController] = None, parent=None):
        super().__init__(parent)
        self.setObjectName("PlayerWidget")
        self._controller = controller or PlayerController()

        root_layout = QVBoxLayout(self)

        controls_row = QHBoxLayout()
        self.play_button = IconButton(tooltip="再生")
        self.pause_button = IconButton(tooltip="一時停止")
        self.stop_button = IconButton(tooltip="停止")
        self.restart_button = IconButton(tooltip="歌いなおし")
        for button in (
            self.play_button,
            self.pause_button,
            self.stop_button,
            self.restart_button,
        ):
            controls_row.addWidget(button)
        root_layout.addLayout(controls_row)

        seek_row = QHBoxLayout()
        self.seek_bar = QSlider(Qt.Orientation.Horizontal)
        self.time_label = QLabel("00:00 / 00:00")
        seek_row.addWidget(self.seek_bar)
        seek_row.addWidget(self.time_label)
        root_layout.addLayout(seek_row)

        self.play_button.clicked.connect(self._controller.play)
        self.pause_button.clicked.connect(self._controller.pause)
        self.stop_button.clicked.connect(self._controller.stop)
        self.restart_button.clicked.connect(self._controller.restart)
