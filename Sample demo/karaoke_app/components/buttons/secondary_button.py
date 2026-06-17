"""
SecondaryButton

プライマリボタンほど強調しない、画面遷移などに使う標準ボタン。
"""
from PySide6.QtWidgets import QPushButton


class SecondaryButton(QPushButton):
    """標準(セカンダリ)ボタン。"""

    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self.setObjectName("SecondaryButton")
        self._apply_style()

    def _apply_style(self) -> None:
        # TODO: resources/styles 配下のQSSを読み込んで適用する
        pass
