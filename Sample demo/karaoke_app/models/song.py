"""
Song

楽曲データを表すモデル。
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:
    """1曲分の情報を保持するデータクラス。"""

    song_id: str
    title: str
    artist: str
    genre: str = ""
    release_year: Optional[int] = None
    jacket_path: str = ""
    lyrics_path: str = ""
    opening_lyrics: str = ""  # 歌いだし表示用(MusicNameWidgetで使用)
