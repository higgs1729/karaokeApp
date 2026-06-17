"""
HeaderWidget

画面上部に表示するヘッダー。アプリ名を大きく表示する。
"""
from PySide6.QtWidgets import QHBoxLayout, QWidget

from karaoke_app.components.labels.title_label import TitleLabel


class HeaderWidget(QWidget):
    """アプリ名などを表示するヘッダー部分。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HeaderWidget")

        layout = QHBoxLayout(self)
        self.app_title_label = TitleLabel("カラオケAPP")
        layout.addWidget(self.app_title_label)

        # TODO: ユーザー情報表示エリア(画面右上)を実装する
        # self.user_info_label = QLabel("")
        # layout.addWidget(self.user_info_label)
