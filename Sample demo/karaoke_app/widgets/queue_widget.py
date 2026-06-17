"""
QueueWidget

予約曲一覧の表示、曲の削除、曲順変更を行う画面。
"""
from typing import Optional

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from karaoke_app.controllers.queue_controller import QueueController


class QueueWidget(QWidget):
    """予約管理画面。"""

    def __init__(self, queue_controller: Optional[QueueController] = None, parent=None):
        super().__init__(parent)
        self.setObjectName("QueueWidget")
        self._controller = queue_controller or QueueController()

        self._layout = QVBoxLayout(self)
        self.refresh()

    def refresh(self) -> None:
        """予約曲一覧の表示を更新する。"""
        while self._layout.count():
            item = self._layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for index, song in enumerate(self._controller.queue.songs):
            # TODO: 曲名表示・削除ボタン・並べ替え操作を持つ専用の行ウィジェットに差し替える
            self._layout.addWidget(QLabel(f"{index + 1}. {song.title} - {song.artist}"))
