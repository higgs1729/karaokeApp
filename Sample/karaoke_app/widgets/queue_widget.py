from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLabel
)
from components.buttons.primary_button import PrimaryButton
from components.buttons.secondary_button import SecondaryButton
from models.song import Song


class QueueWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mw = main_window
        self.setObjectName("QueueWidget")
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        layout.addWidget(QLabel("予約曲一覧"))

        self.queue_list = QListWidget()
        layout.addWidget(self.queue_list)

        # Action buttons
        btn_row = QHBoxLayout()
        self.delete_btn = SecondaryButton("🗑 削除")
        self.up_btn = SecondaryButton("↑ 上へ")
        self.down_btn = SecondaryButton("↓ 下へ")
        self.delete_btn.clicked.connect(self._delete_selected)
        self.up_btn.clicked.connect(self._move_up)
        self.down_btn.clicked.connect(self._move_down)
        btn_row.addWidget(self.delete_btn)
        btn_row.addWidget(self.up_btn)
        btn_row.addWidget(self.down_btn)
        layout.addLayout(btn_row)

        back_btn = SecondaryButton("← ホームへ戻る")
        back_btn.clicked.connect(lambda: self.mw.navigate_to(0))
        layout.addWidget(back_btn)

    def refresh(self, songs):
        self.queue_list.clear()
        for i, song in enumerate(songs):
            self.queue_list.addItem(f"{i + 1}. {song.title} / {song.artist}")

    def _delete_selected(self):
        row = self.queue_list.currentRow()
        if row >= 0:
            # TODO: QueueControllerと連携
            self.queue_list.takeItem(row)

    def _move_up(self):
        row = self.queue_list.currentRow()
        if row > 0:
            item = self.queue_list.takeItem(row)
            self.queue_list.insertItem(row - 1, item)
            self.queue_list.setCurrentRow(row - 1)

    def _move_down(self):
        row = self.queue_list.currentRow()
        if row < self.queue_list.count() - 1:
            item = self.queue_list.takeItem(row)
            self.queue_list.insertItem(row + 1, item)
            self.queue_list.setCurrentRow(row + 1)
