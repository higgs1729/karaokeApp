from typing import List
from models.song import Song


class Queue:
    def __init__(self):
        self._items: List[Song] = []

    def add(self, song: Song):
        self._items.append(song)

    def remove(self, index: int):
        if 0 <= index < len(self._items):
            self._items.pop(index)

    def move(self, from_index: int, to_index: int):
        if 0 <= from_index < len(self._items) and 0 <= to_index < len(self._items):
            song = self._items.pop(from_index)
            self._items.insert(to_index, song)

    def next(self) -> Song | None:
        return self._items.pop(0) if self._items else None

    def peek(self) -> Song | None:
        return self._items[0] if self._items else None

    def all(self) -> List[Song]:
        return list(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)
