from dataclasses import dataclass, field
from datetime import datetime
from models.song import Song


@dataclass
class Score:
    song: Song
    total_score: float = 0.0
    pitch_score: float = 0.0
    rhythm_score: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f"{self.song.title}: {self.total_score:.1f}点"
