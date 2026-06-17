from PySide6.QtCore import QObject, Signal
from models.queue import Queue
from models.song import Song


class QueueController(QObject):
    """予約キューを管理するコントローラー"""

    queue_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._queue = Queue()

    def add_song(self, song: Song):
        self._queue.add(song)
        self.queue_changed.emit()

    def remove_song(self, index: int):
        self._queue.remove(index)
        self.queue_changed.emit()

    def move_song(self, from_index: int, to_index: int):
        self._queue.move(from_index, to_index)
        self.queue_changed.emit()

    def next_song(self) -> Song | None:
        song = self._queue.next()
        self.queue_changed.emit()
        return song

    def get_all(self):
        return self._queue.all()

    def is_empty(self) -> bool:
        return self._queue.is_empty()
