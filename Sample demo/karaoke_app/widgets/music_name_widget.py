"""
MusicNameWidget

選択した曲の詳細(曲名・アーティスト名・ジャケット・歌いだし)を表示し、
予約ボタンから QueueWidget への予約を行う画面。

(注) README.md の「フォルダ構成」には music_name_widget.py の記載が
ありませんでしたが、「画面・機能設計」に MusicNameWidget の定義が
あるため、本スキャフォルドで追加しています。
"""
from typing import Optional

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from karaoke_app.components.buttons.primary_button import PrimaryButton
from karaoke_app.models.song import Song


class MusicNameWidget(QWidget):
    """曲詳細・予約画面。"""

    def __init__(self, song: Optional[Song] = None, parent=None):
        super().__init__(parent)
        self.setObjectName("MusicNameWidget")

        layout = QVBoxLayout(self)

        self.jacket_label = QLabel()  # TODO: ジャケット画像を表示する
        self.title_label = QLabel()
        self.artist_label = QLabel()
        self.opening_lyrics_label = QLabel()  # 歌いだし表示
        self.reserve_button = PrimaryButton("予約する")

        for widget in (
            self.jacket_label,
            self.title_label,
            self.artist_label,
            self.opening_lyrics_label,
            self.reserve_button,
        ):
            layout.addWidget(widget)

        if song:
            self.set_song(song)

    def set_song(self, song: Song) -> None:
        """表示内容を指定した曲の情報で更新する。"""
        self.title_label.setText(song.title)
        self.artist_label.setText(song.artist)
        self.opening_lyrics_label.setText(song.opening_lyrics)
        # TODO: song.jacket_path から画像を読み込み jacket_label にセットする
