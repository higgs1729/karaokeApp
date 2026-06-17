"""
TextInput

曲名・キーワード入力など、テキスト入力全般で使う共通コンポーネント。
"""
from PySide6.QtWidgets import QLineEdit


class TextInput(QLineEdit):
    """共通テキスト入力欄。"""

    def __init__(self, placeholder: str = "", parent=None):
        super().__init__(parent)
        self.setObjectName("TextInput")
        if placeholder:
            self.setPlaceholderText(placeholder)
