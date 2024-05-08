from pydantic import BaseModel, conint
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID


class BoardPoint(BaseModel):
    number: conint(ge=0, le=23)
    checkers_count: conint(ge=0, le=15)
    occupied_by: Optional[UUID] = None


class Board(BaseModel):
    bar_counts: Dict[UUID, int]
    points: List[BoardPoint]


class GameResultInput(BaseModel):
    board: Board
    start_position: Dict[UUID, conint(ge=0, le=23)]


class GameWinType(str, Enum):
    Oin = 'oin'
    Mars = 'mars'
    Koks = 'koks'


class GameResultOutput(BaseModel):
    points: conint(ge=0)
    win_type: GameWinType