from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl


class PlayerController(QObject):
    """音楽再生を管理するコントローラー"""

    position_changed = Signal(int)   # ms
    duration_changed = Signal(int)   # ms
    playback_state_changed = Signal(str)  # "playing" | "paused" | "stopped"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._player = QMediaPlayer(self)
        self._audio_output = QAudioOutput(self)
        self._player.setAudioOutput(self._audio_output)

        self._player.positionChanged.connect(self.position_changed)
        self._player.durationChanged.connect(self.duration_changed)

    def load(self, audio_path: str):
        self._player.setSource(QUrl.fromLocalFile(audio_path))

    def play(self):
        self._player.play()
        self.playback_state_changed.emit("playing")

    def pause(self):
        self._player.pause()
        self.playback_state_changed.emit("paused")

    def stop(self):
        self._player.stop()
        self.playback_state_changed.emit("stopped")

    def restart(self):
        self._player.setPosition(0)
        self._player.play()
        self.playback_state_changed.emit("playing")

    def seek(self, position_ms: int):
        self._player.setPosition(position_ms)

    def set_volume(self, volume: float):
        """0.0 〜 1.0"""
        self._audio_output.setVolume(volume)

    def set_muted(self, muted: bool):
        self._audio_output.setMuted(muted)
