"""
Queue

予約曲一覧(再生待ちリスト)を管理するモデル。
"""
from dataclasses import dataclass, field
from typing import List

from karaoke_app.models.song import Song


@dataclass
class Queue:
    """予約曲のキューを表すモデル。"""

    songs: List[Song] = field(default_factory=list)

    def add(self, song: Song) -> None:
        """曲を予約に追加する。"""
        self.songs.append(song)

    def remove(self, index: int) -> None:
        """指定インデックスの曲を予約から削除する。"""
        if 0 <= index < len(self.songs):
            self.songs.pop(index)

    def move(self, from_index: int, to_index: int) -> None:
        """曲の予約順を変更する。"""
        if 0 <= from_index < len(self.songs) and 0 <= to_index < len(self.songs):
            song = self.songs.pop(from_index)
            self.songs.insert(to_index, song)
