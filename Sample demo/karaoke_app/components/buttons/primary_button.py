"""
PrimaryButton

強調したいアクション(検索決定・予約・再生など)に使う主要ボタン。
"""
from PySide6.QtWidgets import QPushButton


class PrimaryButton(QPushButton):
    """アプリ全体で使う主要(プライマリ)ボタン。"""

    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self.setObjectName("PrimaryButton")
        self._apply_style()

    def _apply_style(self) -> None:
        # TODO: resources/styles 配下のQSSを読み込んで適用する
        pass
