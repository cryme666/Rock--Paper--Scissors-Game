import random
from utils import CHOICES
RESULTS = {"🪨": {"📄": -1, "✂️": 1},
           "📄": {"🪨": 1, "✂️": -1},
           "✂️": {"🪨": -1, "📄": 1}}

def play_game(human_choice):
    computer_choice = random.choice(CHOICES)
    result = RESULTS[human_choice].get(computer_choice, 0)
    return result, computer_choice

