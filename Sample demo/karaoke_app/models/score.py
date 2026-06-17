"""
Score

採点結果(音程・リズム・得点・履歴)を管理するモデル。
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class ScoreEntry:
    """1回分の採点結果。"""

    song_id: str
    pitch_score: float = 0.0
    rhythm_score: float = 0.0
    total_score: float = 0.0


@dataclass
class ScoreHistory:
    """採点履歴を保持するモデル。"""

    entries: List[ScoreEntry] = field(default_factory=list)

    def add(self, entry: ScoreEntry) -> None:
        self.entries.append(entry)
