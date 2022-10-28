"""Module for loading and saving game data to json"""
import json


def load_games() -> list[dict]:
    """Load game info from games.json file"""
    with open('games.json', 'r', encoding="utf-8") as f:
        games = json.load(f)
    return games
