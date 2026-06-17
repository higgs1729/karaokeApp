from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt
from components.buttons.secondary_button import SecondaryButton


class VolumeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("VolumeWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        self.main_slider = self._make_slider("メイン音量", layout)
        self.music_slider = self._make_slider("ミュージック音量", layout)
        self.mic_slider = self._make_slider("マイク音量", layout)

        self.mute_btn = SecondaryButton("🔇 ミュート")
        self.mute_btn.setCheckable(True)
        self.mute_btn.toggled.connect(self._on_mute_toggled)
        layout.addWidget(self.mute_btn)

    def _make_slider(self, label: str, parent_layout) -> QSlider:
        row = QHBoxLayout()
        lbl = QLabel(label)
        lbl.setFixedWidth(160)
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(80)
        row.addWidget(lbl)
        row.addWidget(slider)
        parent_layout.addLayout(row)
        return slider

    def _on_mute_toggled(self, checked: bool):
        # TODO: PlayerControllerと連携
        pass
