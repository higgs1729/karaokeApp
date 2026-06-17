from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from widgets.player_widget import PlayerWidget
from widgets.volume_widget import VolumeWidget
from widgets.microphone_widget import MicrophoneWidget
from widgets.lyrics_widget import LyricsWidget
from components.buttons.secondary_button import SecondaryButton


class KaraokeWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("KaraokeWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        # Lyrics (main area)
        self.lyrics_widget = LyricsWidget()
        layout.addWidget(self.lyrics_widget, stretch=3)

        # Controls via tabs
        tabs = QTabWidget()
        self.player_widget = PlayerWidget()
        self.volume_widget = VolumeWidget()
        self.mic_widget = MicrophoneWidget()
        tabs.addTab(self.player_widget, "▶ 再生")
        tabs.addTab(self.volume_widget, "🔊 音量")
        tabs.addTab(self.mic_widget, "🎤 マイク")
        layout.addWidget(tabs, stretch=1)

        back_btn = SecondaryButton("← ホームへ戻る")
        back_btn.clicked.connect(lambda: self.mw.navigate_to(0))
        layout.addWidget(back_btn)
