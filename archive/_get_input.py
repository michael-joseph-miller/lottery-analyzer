from game import Game


def game_info() -> list[Game]:
    """
    Get lottery game information from user input

    Returns:
        list[Game]: Array of Game objects
    """
    games = []
    add_another = 'Y'

    while add_another.lower() == 'y' or add_another == '':
        # Get data from user.
        game_name = input('Game name (all lower, no spaces): ')
        field_num_max = int(input('Field number max (numer only): '))
        bonus_ball_max = int(input('Bonus ball max (numbers only): '))
        drawing_days = input('Drawing days of the week (eg. ddd,ddd,ddd): ')
        drawing_time = input('Drawing time (HH:MM EST, 24hr): ')
        analysis_start_date = input(
            'Analysis start date (YYYY-MM-DDT00:00:00.000): ')

        game = Game(game_name, field_num_max, bonus_ball_max, drawing_days,
                    drawing_time, analysis_start_date)
        games.append(game)

        add_another = input('Add another? (Y/n): ')

    # games_df = pd.DataFrame.from_records(games, index='game_name')
    return games
