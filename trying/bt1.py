from PySide6.QtWidgets import (
    QPushButton,QLineEdit,QFrame
)


class PrimaryButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)

        self.setMinimumHeight(40)

        self.setStyleSheet("""
            QPushButton {
                background-color: #1E88E5;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1976D2;
            }

            QPushButton:pressed {
                background-color: #1565C0;
            }
        """)

class TextInput(QLineEdit):
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)

        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(40)

        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid #DADADA;
                border-radius: 8px;
                padding: 0 12px;
                background: white;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 2px solid #1E88E5;
            }
        """)

class CardWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 12px;
                border: 1px solid #E5E5E5;
            }
        """)