"""
CardWidget

曲情報(ジャケット・曲名・アーティスト名など)をカード形式で
まとめて表示するための共通コンポーネント。
人気曲欄や検索結果一覧、曲一覧などで使用する想定。
"""
from PySide6.QtWidgets import QFrame, QVBoxLayout


class CardWidget(QFrame):
    """カード型コンテナ。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("CardWidget")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self._layout = QVBoxLayout(self)

    def layout(self) -> QVBoxLayout:  # type: ignore[override]
        return self._layout
