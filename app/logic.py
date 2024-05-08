from typing import List
from app.models import GameResultInput, GameResultOutput, GameWinType, BoardPoint


def determine_winner_and_points(game_data: GameResultInput) -> GameResultOutput:
    board = game_data.board
    start_position = game_data.start_position

    # players id
    player_ids = list(start_position.keys())
    winner_id, loser_id = player_ids[0], player_ids[1]

    # bar count
    loser_bar_count = board.bar_counts.get(loser_id, 0)

    loser_points_on_board: List[BoardPoint] = [
        point for point in board.points if point.occupied_by == loser_id
    ]

    loser_points = sum(point.checkers_count for point in loser_points_on_board)

    # which win
    if loser_points == 0 and loser_bar_count == 0:
        return GameResultOutput(points=1, win_type=GameWinType.Oin)

    # nothing on bar
    all_in_home = all(p.number >= 18 for p in loser_points_on_board)
    if loser_bar_count == 0 and not all_in_home:
        # 'Mars' win
        return GameResultOutput(points=2, win_type=GameWinType.Mars)

    any_in_first_quarter = any(p.number < 6 for p in loser_points_on_board)
    if loser_bar_count > 0 or any_in_first_quarter:
        # 'Kok's' win
        return GameResultOutput(points=3, win_type=GameWinType.Koks)

    # oin
    return GameResultOutput(points=0, win_type=GameWinType.Oin)