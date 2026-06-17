"""
ScoringController

採点機能(音程判定・リズム判定・得点算出・履歴記録)のロジックを担う。
"""
from typing import Optional

from karaoke_app.models.score import ScoreEntry, ScoreHistory


class ScoringController:
    """採点処理を担当するコントローラー。"""

    def __init__(self, history: Optional[ScoreHistory] = None):
        self._enabled = False
        self._history = history or ScoreHistory()

    @property
    def enabled(self) -> bool:
        return self._enabled

    def set_enabled(self, enabled: bool) -> None:
        """採点有効化ボタンから呼ばれる。"""
        self._enabled = enabled

    def evaluate_pitch(self) -> float:
        """音程判定結果を返す。"""
        # TODO: マイク入力と楽曲の音程データを比較するロジックを実装
        return 0.0

    def evaluate_rhythm(self) -> float:
        """リズム判定結果を返す。"""
        # TODO: 入力タイミングと楽曲のリズムを比較するロジックを実装
        return 0.0

    def finalize_score(self, song_id: str) -> ScoreEntry:
        """採点を確定し、履歴に追加する。"""
        entry = ScoreEntry(
            song_id=song_id,
            pitch_score=self.evaluate_pitch(),
            rhythm_score=self.evaluate_rhythm(),
        )
        entry.total_score = (entry.pitch_score + entry.rhythm_score) / 2
        self._history.add(entry)
        return entry
