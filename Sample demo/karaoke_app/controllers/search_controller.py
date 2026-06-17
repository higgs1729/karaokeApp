"""
SearchController

曲名・キーワード・ジャンル・年代などの条件で楽曲を検索するロジックを担う。
"""
from typing import List, Optional

from karaoke_app.models.song import Song


class SearchController:
    """検索処理を担当するコントローラー。"""

    def __init__(self, song_repository: Optional[List[Song]] = None):
        # TODO: data/songs から楽曲データを読み込むリポジトリに差し替える
        self._songs: List[Song] = song_repository or []

    def search_by_keyword(self, keyword: str) -> List[Song]:
        """キーワード(曲名・アーティスト名)で検索する。"""
        keyword = keyword.lower()
        return [
            song for song in self._songs
            if keyword in song.title.lower() or keyword in song.artist.lower()
        ]

    def search_by_genre(self, genre: str) -> List[Song]:
        """ジャンルで検索する(簡易検索)。"""
        return [song for song in self._songs if song.genre == genre]

    def search_by_year(self, year: int) -> List[Song]:
        """年代で検索する(簡易検索)。"""
        return [song for song in self._songs if song.release_year == year]
