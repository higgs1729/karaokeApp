from typing import List
from models.song import Song


class SearchController:
    """楽曲検索を管理するコントローラー"""

    def __init__(self, song_database: List[Song] = None):
        self._database: List[Song] = song_database or []

    def search(self, keyword: str) -> List[Song]:
        """キーワードで曲名・アーティスト名を検索する"""
        keyword = keyword.strip().lower()
        if not keyword:
            return []
        return [
            song for song in self._database
            if keyword in song.title.lower() or keyword in song.artist.lower()
        ]

    def search_by_genre(self, genre: str) -> List[Song]:
        return [s for s in self._database if s.genre == genre]

    def search_by_year(self, year: int) -> List[Song]:
        return [s for s in self._database if s.year == year]

    def get_popular(self, limit: int = 20) -> List[Song]:
        """人気曲を返す（実装時はスコアや再生回数で並べ替え）"""
        return self._database[:limit]

    def load_database(self, songs: List[Song]):
        self._database = songs
