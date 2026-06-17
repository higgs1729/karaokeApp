"""
SerchresultsWidget

検索決定ボタンを押した後に表示される検索結果一覧画面。

(注) ファイル名・クラス名は README.md の表記("serchresult_widget.py" /
"SerchresultsWidget")をそのまま使用しています。"search_result" のtypoの
可能性があるため、必要であれば後から rename してください。
"""
from PySide6.QtWidgets import QVBoxLayout, QWidget

from karaoke_app.widgets.song_list_widget import SongListWidget


class SerchresultsWidget(QWidget):
    """検索結果一覧画面。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SerchresultsWidget")

        layout = QVBoxLayout(self)
        self.song_list_widget = SongListWidget()
        layout.addWidget(self.song_list_widget)
