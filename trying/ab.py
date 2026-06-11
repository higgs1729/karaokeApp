from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

import bt1


class SongListWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def set_songs(self, songs: list[str]):
        self.clear()

        for song in songs:
            card = bt1.CardWidget()

            card_layout = QVBoxLayout(card)
            card_layout.addWidget(QLabel(song))

            self.layout.addWidget(card)

    def clear(self):
        while self.layout.count():
            item = self.layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()