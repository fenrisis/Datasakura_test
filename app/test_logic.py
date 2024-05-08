from app.logic import determine_winner_and_points
from app.models import GameResultInput, Board, BoardPoint, GameResultOutput, GameWinType
from uuid import UUID


def generate_uuid(string):
    return UUID(string)


# "oin" scenario
def test_oin_victory():
    board = Board(
        bar_counts={
            generate_uuid("3fa85f64-5717-4562-b3fc-2c963f66afa6"): 0,
            generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12"): 0
        },
        points=[
            BoardPoint(number=23, checkers_count=0, occupied_by=None)
        ]
    )
    start_position = {
        generate_uuid("3fa85f64-5717-4562-b3fc-2c963f66afa6"): 23,
        generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12"): 0
    }

    input_data = GameResultInput(board=board, start_position=start_position)
    expected_output = GameResultOutput(points=1, win_type=GameWinType.Oin)
    assert determine_winner_and_points(input_data) == expected_output


#  "Mars" scenario
def test_mars_victory():
    board = Board(
        bar_counts={
            generate_uuid("3fa85f64-5717-4562-b3fc-2c963f66afa6"): 0,
            generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12"): 0
        },
        points=[
            BoardPoint(number=10, checkers_count=3, occupied_by=generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12")),
            BoardPoint(number=23, checkers_count=0, occupied_by=None)
        ]
    )
    start_position = {
        generate_uuid("3fa85f64-5717-4562-b3fc-2c963f66afa6"): 23,
        generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12"): 10
    }

    input_data = GameResultInput(board=board, start_position=start_position)
    expected_output = GameResultOutput(points=2, win_type=GameWinType.Mars)
    assert determine_winner_and_points(input_data) == expected_output


# "koks" scenario
def test_koks_victory():
    board = Board(
        bar_counts={
            generate_uuid("3fa85f64-5717-4562-b3fc-2c963f66afa6"): 0,
            generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12"): 1
        },
        points=[
            BoardPoint(number=5, checkers_count=1, occupied_by=generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12")),
            BoardPoint(number=23, checkers_count=0, occupied_by=None)
        ]
    )
    start_position = {
        generate_uuid("3fa85f64-5717-4562-b3fc-2c963f66afa6"): 23,
        generate_uuid("ecf0e70e-7096-4493-a5fc-35e116d66e12"): 5
    }

    input_data = GameResultInput(board=board, start_position=start_position)
    expected_output = GameResultOutput(points=3, win_type=GameWinType.Koks)
    assert determine_winner_and_points(input_data) == expected_output