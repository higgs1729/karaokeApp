from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class LyricsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LyricsWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        self.lyrics_label = QLabel("（歌詞がここに表示されます）")
        self.lyrics_label.setObjectName("LyricsLabel")
        self.lyrics_label.setAlignment(Qt.AlignCenter)
        self.lyrics_label.setWordWrap(True)
        layout.addWidget(self.lyrics_label)

    def set_lyrics(self, text: str):
        self.lyrics_label.setText(text)

    def highlight_line(self, line_index: int):
        """現在歌っている行をハイライトする（実装予定）"""
        pass
