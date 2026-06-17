from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from components.buttons.secondary_button import SecondaryButton
from models.song import Song


class SearchResultWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("SearchResultWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        self.result_label = QLabel("検索結果")
        layout.addWidget(self.result_label)

        self.result_list = QListWidget()
        self.result_list.itemDoubleClicked.connect(self._on_song_selected)
        layout.addWidget(self.result_list)

        back_btn = SecondaryButton("← 検索へ戻る")
        back_btn.clicked.connect(lambda: self.mw.navigate_to(1))
        layout.addWidget(back_btn)

    def search(self, keyword: str):
        # TODO: SearchControllerと連携する
        self.result_label.setText(f'"{keyword}" の検索結果')
        self.result_list.clear()
        # placeholder
        self.result_list.addItem("（検索結果はここに表示されます）")

    def search_by_genre(self, genre: str):
        self.result_label.setText(f"ジャンル: {genre}")
        self.result_list.clear()
        self.result_list.addItem("（検索結果はここに表示されます）")

    def _on_song_selected(self, item: QListWidgetItem):
        # TODO: 曲詳細画面(MusicNameWidget)へ遷移
        pass
