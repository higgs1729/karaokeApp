from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt
from components.buttons.primary_button import PrimaryButton
from components.buttons.secondary_button import SecondaryButton


class PlayerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PlayerWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        # Seek bar
        self.seek_bar = QSlider(Qt.Horizontal)
        self.seek_bar.setRange(0, 1000)
        layout.addWidget(self.seek_bar)

        # Time label
        time_row = QHBoxLayout()
        self.current_time_label = QLabel("0:00")
        self.total_time_label = QLabel("0:00")
        time_row.addWidget(self.current_time_label)
        time_row.addStretch()
        time_row.addWidget(self.total_time_label)
        layout.addLayout(time_row)

        # Playback buttons
        btn_row = QHBoxLayout()
        self.play_btn = PrimaryButton("▶ 再生")
        self.pause_btn = SecondaryButton("⏸ 一時停止")
        self.stop_btn = SecondaryButton("⏹ 停止")
        self.restart_btn = SecondaryButton("↩ 歌いなおし")

        self.play_btn.clicked.connect(self._on_play)
        self.pause_btn.clicked.connect(self._on_pause)
        self.stop_btn.clicked.connect(self._on_stop)
        self.restart_btn.clicked.connect(self._on_restart)

        btn_row.addWidget(self.restart_btn)
        btn_row.addWidget(self.play_btn)
        btn_row.addWidget(self.pause_btn)
        btn_row.addWidget(self.stop_btn)
        layout.addLayout(btn_row)

    def _on_play(self):
        # TODO: PlayerControllerと連携
        pass

    def _on_pause(self):
        pass

    def _on_stop(self):
        pass

    def _on_restart(self):
        pass

    def update_position(self, position_ms: int, duration_ms: int):
        if duration_ms > 0:
            self.seek_bar.setValue(int(position_ms / duration_ms * 1000))
        self.current_time_label.setText(self._ms_to_str(position_ms))
        self.total_time_label.setText(self._ms_to_str(duration_ms))

    @staticmethod
    def _ms_to_str(ms: int) -> str:
        s = ms // 1000
        return f"{s // 60}:{s % 60:02d}"
