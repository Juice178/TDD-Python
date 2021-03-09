from dataclasses import dataclass, field
from typing import cast


@dataclass()
class Pair:
    _source: str = field(default_factory=str)
    _to: str = field(default_factory=str)

    def __eq__(self, obj: object) -> bool:
        pair = cast(Pair, obj)
        return self._source == pair._source and self._to == pair._to

    def __hash__(self) -> int:
        return 0