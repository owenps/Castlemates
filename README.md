# Castlemates
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev.

## Data
Games are parsed using the [python chess](https://python-chess.readthedocs.io/en/latest/) library. My findings scanned over 17 million games on the [Lichess game database](https://database.lichess.org/). 

| Date         | Games       | Size         | Castle Checkmates  |
|:-------------|:------------|:-------------|:-------------------|
| 2018 January | 17,945,784  | 38.27 GB     | -                  |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL |   
|:---|:----------|:----------|:-------------------|
| 1  | -         | -         | -                  |
| 2  | -         | -         | -                  |
| 3  | -         | -         | -                  |
| 4  | -         | -         | -                  |
| 5  | -         | -         | -                  |
| 6  | -         | -         | -                  |
| 7  | -         | -         | -                  |
| 8  | -         | -         | -                  |
| 9  | -         | -         | -                  |
| 10 | -         | -         | -                  |
| 11 | -         | -         | -                  |
| 12 | -         | -         | -                  |
| 13 | -         | -         | -                  |
| 14 | -         | -         | -                  |
| 15 | -         | -         | -                  |
| 16 | -         | -         | -                  |
| 17 | -         | -         | -                  |
| 18 | -         | -         | -                  |
| 19 | -         | -         | -                  |
| 20 | -         | -         | -                  |
| 21 | -         | -         | -                  |
| 22 | -         | -         | -                  |
| 23 | -         | -         | -                  |
| 24 | -         | -         | -                  |
| 25 | -         | -         | -                  |

## Executing The Script Yourself
Firstly, install [python-chess](https://python-chess.readthedocs.io/en/latest/) using the following command. 
```
pip install chess
```
Then to execute the script itself, you will need to an associated .pgn file (E.g. `example.pgn`) which will be passed in as a command line argument. 
```
python castlemates.py example.pgn
```
Optionally, you can set a minimum Elo parameter to only output games where both players are above a certain Elo ranking.
```
python castlemates.py example.pgn 2000
```
This parameter by default is `0`.
