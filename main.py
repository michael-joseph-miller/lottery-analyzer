#!/usr/bin/python3
"""
Starting point for Lottery Analyzer App
"""
# import os

# from dotenv import load_dotenv

# import get_input as get

# import FieldNumbers as fn
# import lottery_analyzer_db as db
# import lottery_data_api as api

# load_dotenv()  # Get environment variables from .env file


def main():
    """
    main function to run when this file is executed
    """
    # db.updateDrawingsHistory(['powerball', 'mega_millions'])

    import game
    game = game.Game()


if __name__ == '__main__':
    main()
