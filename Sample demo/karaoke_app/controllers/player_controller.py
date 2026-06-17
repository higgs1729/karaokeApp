"""
PlayerController

再生・一時停止・停止・歌いなおし・シークなど、再生全般のロジックを担う。
"""
from PySide6.QtCore import QObject, Signal


class PlayerController(QObject):
    """再生制御を担当するコントローラー。"""

    position_changed = Signal(int)  # シークバー更新用
    playback_finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: QMediaPlayer などの実際の再生バックエンドを保持する
        self._is_playing = False

    def play(self) -> None:
        self._is_playing = True

    def pause(self) -> None:
        self._is_playing = False

    def stop(self) -> None:
        self._is_playing = False

    def restart(self) -> None:
        """歌いなおし(曲の最初から再生し直す)。"""
        self.stop()
        self.play()

    def seek(self, position_ms: int) -> None:
        self.position_changed.emit(position_ms)
