# Lottery Analyzer Outline

## Desired Outcomes/Functionality

1. Retrieve most current data from lottery database NYS sodapy
2. Analyze data for following outputs
   1. Number of drawings since last hit (int), no hit count
      1. last_drawing_date (game) - last_hit_date (ball #)
      2. OR increment no_hit_count for every drawing
   2. Hit frequency (int)
      1. #drawings since start date / #hits for ball number (round up)
   3. Overdue rate (int) - Number of drawings overdue
      1. Drawings since last hit(no_hit_count) - hit freq

## Inputs

1. Imports from NYS database
   1. Mega Millions
      1. draw_date (str) "YYYY-MM-DDT00:00:00.000"
      2. winning_numbers (str) "NN NN NN NN NN"
      3. mega_ball (str) "NN"
      4. multiplier (str) "NN"
   2. Powerball
      1. draw_date (str) "YYYY-MM-DDT00:00:00.000"
      2. winning_numbers (str) "NN NN NN NN NN PB"
      3. multiplier (str) "N"
2. Known/Const Data
   1. Mega Millions
      1. Start date "2017-10-31T00:00:00.000"
      2. Drawing days Tue, Fri
      3. Field # max 70
      4. Mega ball max 25
   2. Powerball
      1. Start date "2015-10-04T00:00:00.000"
      2. Drawing days Mon, Wed, Sat
      3. Field # max 69
      4. Powerball max 26

## Outputs

1. Game
   1. Total # drawings
   2. Each Ball number, field and bonus ball
      1. Number of total hits
      2. Last hit date
      3. Drawings since last hit, no_hit_count
      4. Hit freq
      5. Overdue

## Database Tables

### games

| game_name | start_date | last_draw_date | draw_days | field_num_max | bonus_ball_max |
| :-------: | :--------: | :------------: | :-------: | :-----------: | :------------: |
|    str    |  date str  |    date str    |    str    |      int      |      int       |

### analysis

| game_name | ball_num | total_num_hits | last_hit_date | no_hit_count | freq | draws_overdue |
| :-------: | :------: | :------------: | :-----------: | :----------: | :--: | :-----------: |
|    str    |   str    |      int       |   date str    |     int      | int  |      int      |

### drawings

| game_name | draw_date | field_nums | bonus_ball | multiplier |
| :-------: | :-------: | :--------: | :--------: | :--------: |
|    str    | date str  |    str     |    str     |    str     |
