from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget
)
from PySide6.QtCore import Qt
from components.buttons.primary_button import PrimaryButton
from components.buttons.secondary_button import SecondaryButton


class ScoringWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("ScoringWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(16)

        # Enable toggle
        self.enable_btn = PrimaryButton("採点 OFF")
        self.enable_btn.setCheckable(True)
        self.enable_btn.toggled.connect(self._on_toggled)
        layout.addWidget(self.enable_btn)

        # Score display
        score_row = QHBoxLayout()
        self.pitch_label = QLabel("音程: --")
        self.rhythm_label = QLabel("リズム: --")
        self.total_label = QLabel("得点: --")
        for lbl in [self.pitch_label, self.rhythm_label, self.total_label]:
            lbl.setAlignment(Qt.AlignCenter)
            score_row.addWidget(lbl)
        layout.addLayout(score_row)

        # History
        layout.addWidget(QLabel("採点履歴"))
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)

        back_btn = SecondaryButton("← ホームへ戻る")
        back_btn.clicked.connect(lambda: self.mw.navigate_to(0))
        layout.addWidget(back_btn)

    def _on_toggled(self, checked: bool):
        self.enable_btn.setText("採点 ON" if checked else "採点 OFF")
        # TODO: ScoringControllerと連携

    def update_score(self, total: float, pitch: float, rhythm: float):
        self.pitch_label.setText(f"音程: {pitch:.1f}")
        self.rhythm_label.setText(f"リズム: {rhythm:.1f}")
        self.total_label.setText(f"得点: {total:.1f}")

    def add_history(self, score):
        self.history_list.addItem(str(score))
