from dataclasses import dataclass, field


@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str = ""
    year: int = 0
    lyrics_path: str = ""
    audio_path: str = ""
    jacket_path: str = ""
    opening_lyrics: str = ""  # 歌いだし

    def __str__(self):
        return f"{self.title} / {self.artist}"
