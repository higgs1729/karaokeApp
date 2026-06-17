"""
SongListWidget

曲一覧を表示する共通ウィジェット。SearchWidget や SerchresultsWidget から利用される。
"""
from typing import List

from PySide6.QtWidgets import QVBoxLayout, QWidget

from karaoke_app.components.cards.card_widget import CardWidget
from karaoke_app.models.song import Song


class SongListWidget(QWidget):
    """曲一覧を表示するウィジェット。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SongListWidget")
        self._layout = QVBoxLayout(self)

    def set_songs(self, songs: List[Song]) -> None:
        """一覧表示する曲を更新する。"""
        while self._layout.count():
            item = self._layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for song in songs:
            card = CardWidget()
            # TODO: カード内に曲名・アーティスト名・ジャケットを表示する
            self._layout.addWidget(card)
