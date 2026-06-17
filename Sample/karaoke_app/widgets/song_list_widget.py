from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel
from models.song import Song
from typing import List


class SongListWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("SongListWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel("曲一覧")
        layout.addWidget(self.label)

        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self._on_song_selected)
        layout.addWidget(self.list_widget)

    def set_songs(self, songs: List[Song]):
        self.list_widget.clear()
        for song in songs:
            item = QListWidgetItem(f"{song.title}  /  {song.artist}")
            item.setData(256, song)  # Qt.UserRole = 256
            self.list_widget.addItem(item)

    def _on_song_selected(self, item: QListWidgetItem):
        song: Song = item.data(256)
        if song:
            # TODO: MusicNameWidgetへ遷移して曲情報を表示
            pass
