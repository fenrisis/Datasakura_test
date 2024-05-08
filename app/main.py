from fastapi import FastAPI
from app.models import GameResultInput, GameResultOutput
from app.logic import determine_winner_and_points

app = FastAPI()


@app.post("/calculate_result", response_model=GameResultOutput)
def calculate_result(input_data: GameResultInput):
    return determine_winner_and_points(input_data)