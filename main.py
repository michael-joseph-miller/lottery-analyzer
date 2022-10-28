#!/usr/bin/python3
"""
Starting point for Lottery Analyzer App
"""

import matplotlib.pyplot as plt

from game import Game
from game_db import load_games


async def main():
    """
    main function to run when this file is executed
    """
    games: list[Game] = []

    for game in load_games():
        temp_game = Game(game['name'], game['start_date'],
                                game['field_num_max'], game['bonus_ball_max'],
                                game['days_drawn'])
        await temp_game.init()
        games.append(temp_game)

    field_nums, draws_overdue = [],[]

    fig, ax = plt.subplots(2,1)
    fig.set_size_inches(12,6)
    print('------------------------------------------')
    fig.set_tight_layout(True)
    for i, game in enumerate(games):
        ax[i].bar(game.field_nums_overdue[0], game.field_nums_overdue[1])
        ax[i].set_title(f'{game.name} Overdue Ball Numbers')
        ax[i].set_facecolor('#222')
        ax[i].set_ylabel('# Drawings Overdue')
        ax[i].set_xlabel('Ball Number')
        
        cell_text, rows, cols = [],[],[]
        for num in game.field_nums_overdue:
            cell_text.append(num)
        
        nums = sorted(game.field_nums_overdue[0])
        print(f'{game.name} Overdue Numbers: {" ".join(nums)}')
        print(f'Last Draw Date: {game.last_draw_date}')
        print(f'Days Drawn: {", ".join(game.days_drawn)}')
        print('------------------------------------------')
        
    pyscript.write('plot', fig) # type: ignore - undefined variable

if __name__ == '__main__':
    await main() # type: ignore - await allowed only onside function
