"""Module for loading and saving game data to json"""
import json


def load_game_info() -> list[dict]:
    """Load game info from games.json file"""
    with open('game_info.json', 'r', encoding="utf-8") as f:
        games = json.load(f)
    return games
