"""
KaraokeWidget

カラオケ再生中の画面。PlayerWidget・VolumeWidget・MicrophoneWidget・
LyricsWidget をまとめて表示する。
"""
from PySide6.QtWidgets import QVBoxLayout, QWidget

from karaoke_app.widgets.lyrics_widget import LyricsWidget
from karaoke_app.widgets.microphone_widget import MicrophoneWidget
from karaoke_app.widgets.player_widget import PlayerWidget
from karaoke_app.widgets.volume_widget import VolumeWidget


class KaraokeWidget(QWidget):
    """カラオケ再生画面。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("KaraokeWidget")

        layout = QVBoxLayout(self)

        self.lyrics_widget = LyricsWidget()
        self.player_widget = PlayerWidget()
        self.volume_widget = VolumeWidget()
        self.microphone_widget = MicrophoneWidget()

        layout.addWidget(self.lyrics_widget)
        layout.addWidget(self.player_widget)
        layout.addWidget(self.volume_widget)
        layout.addWidget(self.microphone_widget)
