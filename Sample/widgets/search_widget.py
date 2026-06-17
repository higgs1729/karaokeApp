from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel
)
from components.inputs.text_input import TextInput
from components.buttons.primary_button import PrimaryButton
from components.buttons.secondary_button import SecondaryButton


QUICK_SEARCH_CATEGORIES = ["J-POP", "演歌", "アニソン", "洋楽", "90年代", "2000年代", "2010年代"]


class SearchWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("SearchWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(16)

        # Search bar
        search_row = QHBoxLayout()
        self.search_input = TextInput("曲名・アーティスト名を入力")
        self.search_btn = PrimaryButton("検索")
        self.search_btn.clicked.connect(self._on_search)
        search_row.addWidget(self.search_input)
        search_row.addWidget(self.search_btn)
        layout.addLayout(search_row)

        # Quick search categories
        cat_label = QLabel("カテゴリから検索")
        layout.addWidget(cat_label)

        cat_row = QHBoxLayout()
        for cat in QUICK_SEARCH_CATEGORIES:
            btn = SecondaryButton(cat)
            btn.clicked.connect(lambda checked, c=cat: self._on_quick_search(c))
            cat_row.addWidget(btn)
        layout.addLayout(cat_row)

        # Song list area
        from widgets.song_list_widget import SongListWidget
        self.song_list = SongListWidget(self.mw)
        layout.addWidget(self.song_list)

        # Back button
        back_btn = SecondaryButton("← ホームへ戻る")
        back_btn.clicked.connect(lambda: self.mw.navigate_to(0))
        layout.addWidget(back_btn)

    def _on_search(self):
        keyword = self.search_input.text()
        self.mw.navigate_to(2)
        self.mw.search_result_widget.search(keyword)

    def _on_quick_search(self, category: str):
        self.mw.navigate_to(2)
        self.mw.search_result_widget.search_by_genre(category)
