"""
ScoringWidget

採点有効化、音程判定・リズム判定の表示、得点表示、採点履歴表示を行う。
"""
from typing import Optional

from PySide6.QtWidgets import QCheckBox, QLabel, QListWidget, QVBoxLayout, QWidget

from karaoke_app.controllers.scoring_controller import ScoringController


class ScoringWidget(QWidget):
    """採点機能画面。"""

    def __init__(self, controller: Optional[ScoringController] = None, parent=None):
        super().__init__(parent)
        self.setObjectName("ScoringWidget")
        self._controller = controller or ScoringController()

        layout = QVBoxLayout(self)

        self.enable_checkbox = QCheckBox("採点を有効にする")
        self.pitch_label = QLabel("音程判定: -")
        self.rhythm_label = QLabel("リズム判定: -")
        self.score_label = QLabel("得点: -")
        self.history_list = QListWidget()

        for widget in (
            self.enable_checkbox,
            self.pitch_label,
            self.rhythm_label,
            self.score_label,
            self.history_list,
        ):
            layout.addWidget(widget)

        self.enable_checkbox.toggled.connect(self._controller.set_enabled)
