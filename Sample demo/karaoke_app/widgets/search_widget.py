"""
SearchWidget

曲名・キーワード・アーティスト名での検索、および簡易検索(ジャンル・年代)を行う画面。
"""
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from karaoke_app.components.buttons.primary_button import PrimaryButton
from karaoke_app.components.inputs.text_input import TextInput
from karaoke_app.widgets.song_list_widget import SongListWidget


class SearchWidget(QWidget):
    """検索画面。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SearchWidget")

        root_layout = QVBoxLayout(self)

        search_row = QHBoxLayout()
        self.keyword_input = TextInput(placeholder="曲名・アーティスト名で検索")
        self.search_button = PrimaryButton("検索")
        search_row.addWidget(self.keyword_input)
        search_row.addWidget(self.search_button)
        root_layout.addLayout(search_row)

        # TODO: ジャンル・年代などの簡易検索一覧UIを実装する
        # self.quick_filter_widget = ...

        self.song_list_widget = SongListWidget()
        root_layout.addWidget(self.song_list_widget)
