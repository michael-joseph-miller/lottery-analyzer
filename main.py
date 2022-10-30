#!/usr/bin/python3
"""
Starting point for Lottery Analyzer App
"""

import matplotlib.pyplot as plt

from game import init_games
from game_info_db import load_game_info


async def main():
    """
    main function to run when this file is executed
    """
    games = await init_games()
        
    # Create Plots and display
    fig, ax = plt.subplots(2,1)
    fig.set_size_inches(12,12)
    fig.set_tight_layout(True)
    print('------------------------------------------')
    for i, game in enumerate(games):
        field_nums_overdue = game.get_field_nums_overdue()
        id = game.name.lower().replace(' ', '_')
        
        ax[i].bar(field_nums_overdue[0], field_nums_overdue[1])
        ax[i].set_title(f'{game.name} Overdue Ball Numbers')
        ax[i].set_ylabel('# Drawings Overdue')
        ax[i].set_xlabel('Ball Number')
        pyscript.write('plot', fig) # type: ignore - undefined variable
        
        num_picks = []
        for i in range(0,len(field_nums_overdue[0]),5):
            num_picks.append(field_nums_overdue[0][i:i+5])
        print(f'{game.name}')
        print('------------------------------------------')
        print(f'Last Draw Date: {game.last_draw_date}')
        print(f'Days Drawn: {", ".join(game.days_drawn)}')
        print('Picks:')
        for el in num_picks:
            print(' '.join(el))
        print('------------------------------------------')

if __name__ == '__main__':
    await main() # type: ignore - await allowed only onside function
