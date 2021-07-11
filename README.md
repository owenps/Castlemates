# Castlemates  👑
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev. 

<a href="https://lichess.org/CW7va6EJ" target="_blank"><img src="exampleCastlemate.gif" width=300></a>

## Data
Unfortunately parsing games using the [python chess](https://python-chess.readthedocs.io/en/latest/) library is quite slow. So `castlemates.py` contains a simplified-lightweight version designed specifically to find games which end in a castle checkmate. My findings scanned over 17 million games on the [Lichess game database](https://database.lichess.org/). Notable players include: [IM Vincent Rothuis](https://lichess.org/qmq5jjLs).

| Date                                                                                | Games       | Size         | Castle Checkmates  |
|:------------------------------------------------------------------------------------|:------------|:-------------|:-------------------|
| [2018 January](https://github.com/owenps/Castlemates/blob/main/results/2018-01.txt) | 17,945,784  | 38.27 GB     | 181                |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL           |   
|:---|:----------|:----------|:-----------------------------|
| 1  | 2862      | 2248      | https://lichess.org/qmq5jjLs | <!-- 5110 -->
| 2  | 2390      | 2224      | https://lichess.org/TJJxBOME | <!-- 4614 -->
| 3  | 2292      | 2171      | https://lichess.org/yg4Wy7hg | <!-- 4463 -->
| 4  | 2310      | 2022      | https://lichess.org/rv8qttCj | <!-- 4332 -->
| 5  | 2214      | 2048      | https://lichess.org/UbbXiVX2 | <!-- 4262 -->
| 6  | 2103      | 2158      | https://lichess.org/nu3USCaC | <!-- 4261 -->
| 7  | 2087      | 2143      | https://lichess.org/CW7va6EJ | <!-- 4230 -->
| 8  | 2014      | 2184      | https://lichess.org/t4wLU7Jz | <!-- 4198 -->
| 9  | 2249      | 1918      | https://lichess.org/gMueyvzT | <!-- 4167 -->
| 10 | 2071      | 2022      | https://lichess.org/IUD2Dc5k | <!-- 4093 -->
| 11 | 2008      | 2066      | https://lichess.org/TpgQBtmO | <!-- 4074 -->
| 12 | 1998      | 2029      | https://lichess.org/eBOkhMgh | <!-- 4027 -->
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
To execute the script `castlemates.py`, you will need to an associated .pgn file which will be passed in as a command line argument. 
```
python castlemates.py example.pgn
```
Optionally, you can set a batch parameter to output a progress message of what game is currently being analyzed. This can give you an idea of how fast the program is running and how many games remain. The following outputs a message every 500 games. 
```
python castlemates.py example.pgn 500
> Progress Update: Game #500
> Progress Update: Game #1,000
```
This parameter by default is set to `1e6`. To disable the progress update messages, set the parameter to `0`.
