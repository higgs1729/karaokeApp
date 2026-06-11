from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from bt1 import TextInput,PrimaryButton
from ab import SongListWidget


class SearchWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.search_input = TextInput("曲名を入力")
        self.search_button = PrimaryButton("検索")

        self.song_list = SongListWidget()

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        layout = QVBoxLayout(self)

        layout.addLayout(search_layout)
        layout.addWidget(self.song_list)

        self.search_button.clicked.connect(self.search)

    def search(self):

        keyword = self.search_input.text()

        songs = [
            f"{keyword} Song A",
            f"{keyword} Song B",
            f"{keyword} Song C",
        ]

        self.song_list.set_songs(songs)