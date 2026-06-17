"""
TitleLabel

画面タイトルやセクション見出しなど、大きめのテキスト表示に使う。
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class TitleLabel(QLabel):
    """見出し用ラベル。"""

    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self.setObjectName("TitleLabel")
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
