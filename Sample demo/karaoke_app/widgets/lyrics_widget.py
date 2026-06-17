"""
LyricsWidget

再生中の曲の歌詞を表示する。
"""
from PySide6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget


class LyricsWidget(QWidget):
    """歌詞表示画面。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LyricsWidget")

        layout = QVBoxLayout(self)
        self.lyrics_label = QLabel()
        self.lyrics_label.setWordWrap(True)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.lyrics_label)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

    def set_lyrics(self, text: str) -> None:
        """表示する歌詞テキストを更新する。"""
        self.lyrics_label.setText(text)
