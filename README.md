# Castlemates ♔♖ ♚♜
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev. 

If you enjoy the project and wish to show your support, leaving a ⭐ on the repository would really mean a lot!

<a href="https://lichess.org/CW7va6EJ" target="_blank"><img src="exampleCastlemate.gif" width=300></a>

## Data
Unfortunately parsing games using the [python chess](https://python-chess.readthedocs.io/en/latest/) library is quite slow. So `castlemates.py` contains a simplified-lightweight version designed specifically to find games which end in a castle checkmate. My findings scanned over 17 million games on the [Lichess game database](https://database.lichess.org/). Notable players include: [GM Elier Miranda](https://lichess.org/7mOvUS5L), [IM Vincent Rothuis](https://lichess.org/qmq5jjLs), [IM Martin Neyhebaver](https://lichess.org/ymm4Bysd).

| Date                                                                                | Games       | Size         | Castle Checkmates  |
|:------------------------------------------------------------------------------------|:------------|:-------------|:-------------------|
| **More Games Coming Soon!**                                                         | -           | -            | -                  |
| [2021 June](https://github.com/owenps/Castlemates/blob/main/results/2021-06.txt)    | 92,190,803  | 206.53 GB    | 950                |
| [2021 May](https://github.com/owenps/Castlemates/blob/main/results/2021-05.txt)     | 101,011,629 | 232.21 GB    | 1,120             |
| [2018 January](https://github.com/owenps/Castlemates/blob/main/results/2018-01.txt) | 17,945,784  | 38.27 GB     | 181                |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL           |   
|:---|:----------|:----------|:-----------------------------|
| 1  | 2670      | 2700      | https://lichess.org/DEbahVgE | <!-- 5370 -->
| 2  | 2663      | 2572      | https://lichess.org/kDPj9PSW | <!-- 5235 -->
| 3  | 2620      | 2534      | https://lichess.org/ymm4Bysd | <!-- 5154 -->
| 4  | 2862      | 2248      | https://lichess.org/qmq5jjLs | <!-- 5110 -->
| 5  | 2609      | 2491      | https://lichess.org/k72rG9AE | <!-- 5100 -->
| 6  | 2514      | 2367      | https://lichess.org/7mOvUS5L | <!-- 4881 -->
| 7  | 2363      | 2517      | https://lichess.org/c5KIcUCa | <!-- 4880 --> 
| 8  | 2433      | 2422      | https://lichess.org/kVE2ra4W | <!-- 4855 -->
| 9  | 2479      | 2326      | https://lichess.org/ZvlnHkhn | <!-- 4805 --> 
| 10 | 2352      | 2447      | https://lichess.org/8aFwXeYF | <!-- 4799 -->
| 11 | 2403      | 2379      | https://lichess.org/UwTxNNuz | <!-- 4782 -->
| 12 | 2341      | 2431      | https://lichess.org/WhcAk9EO | <!-- 4772 --> 
| 13 | 2383      | 2375      | https://lichess.org/hmc9VOHT | <!-- 4758 --> 
| 14 | 2323      | 2431      | https://lichess.org/j4vAQo7Q | <!-- 4754 --> 
| 15 | 2364      | 2384      | https://lichess.org/zT0ppPlZ | <!-- 4748 -->
| 16 | 2351      | 2346      | https://lichess.org/NYofWmre | <!-- 4697 -->
| 17 | 2352      | 2334      | https://lichess.org/mM7hrE10 | <!-- 4686 -->
| 18 | 2272      | 2400      | https://lichess.org/ml7lk7mc | <!-- 4672 --> 
| 19 | 2355      | 2304      | https://lichess.org/VCnhX6iV | <!-- 4659 -->
| 20 | 2373      | 2273      | https://lichess.org/5gIqCeWe | <!-- 4646 -->
| 21 | 2394      | 2240      | https://lichess.org/ngPK1tfl | <!-- 4634 -->
| 22 | 2335      | 2294      | https://lichess.org/arTrZnep | <!-- 4629 -->
| 23 | 2227      | 2393      | https://lichess.org/ghto7CJY | <!-- 4620 -->
| 24 | 2390      | 2224      | https://lichess.org/TJJxBOME | <!-- 4614 -->
| 25 | 2314      | 2296      | https://lichess.org/UUnM71YG | <!-- 4610 -->

## Executing The Script Yourself
To execute the script `castlemates.py`, you will need to an associated .pgn file which will be passed in as a command line argument. 
```
python castlemates.py example.pgn
```
Optionally, you can set a batch parameter to output a progress message of what game is currently being analyzed. This can give you an idea of how fast the program is running and how many games have been processed. The following outputs a message every 500 games. 
```
python castlemates.py example.pgn 500
> Progress Update: Game #500
> Progress Update: Game #1,000
```
This parameter by default is set to `1e6`. To disable the progress update messages, set the parameter to `0`.
