# Castlemates
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev.

<a href="https://lichess.org/CW7va6EJ" target="_blank"><img src="exampleCastlemate.gif" width=300></a>

## Data
Games are parsed using the [python chess](https://python-chess.readthedocs.io/en/latest/) library. My findings scanned over 17 million games on the [Lichess game database](https://database.lichess.org/). 

| Date         | Games       | Size         | Castle Checkmates  |
|:-------------|:------------|:-------------|:-------------------|
| 2018 January | 17,945,784  | 38.27 GB     | -                  |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL           |   
|:---|:----------|:----------|:-----------------------------|
| 1  | 2390      | 2224      | https://lichess.org/TJJxBOME | <!-- 4614 -->
| 2  | 2292      | 2171      | https://lichess.org/yg4Wy7hg | <!-- 4463 -->
| 3  | 2310      | 2022      | https://lichess.org/rv8qttCj | <!-- 4332 -->
| 4  | 2103      | 2158      | https://lichess.org/nu3USCaC | <!-- 4261 -->
| 5  | 2087      | 2143      | https://lichess.org/CW7va6EJ | <!-- 4230 -->
| 6  | 2014      | 2184      | https://lichess.org/t4wLU7Jz | <!-- 4198 -->
| 7  | 2071      | 2022      | https://lichess.org/IUD2Dc5k | <!-- 4093 -->
| 8  | 1998      | 2029      | https://lichess.org/eBOkhMgh | <!-- 4027 -->
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
This parameter by default is set to `0`.
