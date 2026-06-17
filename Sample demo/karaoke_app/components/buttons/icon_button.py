"""
IconButton

アイコンのみ(または アイコン+ツールチップ)を表示するボタン。
再生/一時停止/停止/ミュートなど、視覚的に分かりやすいUIに使用する。
"""
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton


class IconButton(QPushButton):
    """アイコン表示用ボタン。"""

    def __init__(self, icon_path: str = "", tooltip: str = "", parent=None):
        super().__init__(parent)
        self.setObjectName("IconButton")
        if icon_path:
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(24, 24))
        if tooltip:
            self.setToolTip(tooltip)
