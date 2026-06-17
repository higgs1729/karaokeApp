from PySide6.QtCore import QObject, Signal
from models.score import Score
from models.song import Song
from typing import List
import random


class ScoringController(QObject):
    """採点機能を管理するコントローラー"""

    score_updated = Signal(float, float, float)  # total, pitch, rhythm

    def __init__(self, parent=None):
        super().__init__(parent)
        self._enabled = False
        self._history: List[Score] = []
        self._current_song: Song | None = None

    def enable(self, enabled: bool):
        self._enabled = enabled

    def is_enabled(self) -> bool:
        return self._enabled

    def start_scoring(self, song: Song):
        self._current_song = song

    def update_score(self, pitch: float, rhythm: float):
        """リアルタイム採点更新（マイク入力から呼び出す）"""
        if not self._enabled:
            return
        total = (pitch * 0.6 + rhythm * 0.4)
        self.score_updated.emit(total, pitch, rhythm)

    def finalize(self) -> Score | None:
        if not self._current_song:
            return None
        # TODO: 実際のマイク解析結果を使用する
        pitch = random.uniform(60, 100)
        rhythm = random.uniform(60, 100)
        total = pitch * 0.6 + rhythm * 0.4
        score = Score(
            song=self._current_song,
            total_score=total,
            pitch_score=pitch,
            rhythm_score=rhythm,
        )
        self._history.append(score)
        return score

    def get_history(self) -> List[Score]:
        return list(self._history)
