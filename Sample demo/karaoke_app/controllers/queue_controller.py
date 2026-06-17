"""
QueueController

予約曲一覧(Queueモデル)の追加・削除・順序変更を仲介するコントローラー。
"""
from typing import Optional

from karaoke_app.models.queue import Queue
from karaoke_app.models.song import Song


class QueueController:
    """予約キュー操作を担当するコントローラー。"""

    def __init__(self, queue: Optional[Queue] = None):
        self._queue = queue or Queue()

    @property
    def queue(self) -> Queue:
        return self._queue

    def reserve(self, song: Song) -> None:
        """曲を予約する(MusicNameWidgetの予約ボタンから呼ばれる想定)。"""
        self._queue.add(song)

    def cancel(self, index: int) -> None:
        """予約曲を削除する(QueueWidgetの曲削除)。"""
        self._queue.remove(index)

    def reorder(self, from_index: int, to_index: int) -> None:
        """予約曲の順番を変更する(QueueWidgetの曲順変更)。"""
        self._queue.move(from_index, to_index)
