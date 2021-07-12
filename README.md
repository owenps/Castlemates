# Castlemates ♔♖ ♚♜
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev. 

<a href="https://lichess.org/CW7va6EJ" target="_blank"><img src="exampleCastlemate.gif" width=300></a>

## Data
Unfortunately parsing games using the [python chess](https://python-chess.readthedocs.io/en/latest/) library is quite slow. So `castlemates.py` contains a simplified-lightweight version designed specifically to find games which end in a castle checkmate. My findings scanned over 17 million games on the [Lichess game database](https://database.lichess.org/). Notable players include: [IM Vincent Rothuis](https://lichess.org/qmq5jjLs).

| Date                                                                                | Games       | Size         | Castle Checkmates  |
|:------------------------------------------------------------------------------------|:------------|:-------------|:-------------------|
| **More Games Coming Soon!**                                                         | -           | -            | -                  |
| [2021 June](https://github.com/owenps/Castlemates/blob/main/results/2021-06.txt)    | 92,190,803  | 206.53 GB    | 950                |
| [2018 January](https://github.com/owenps/Castlemates/blob/main/results/2018-01.txt) | 17,945,784  | 38.27 GB     | 181                |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL           |   
|:---|:----------|:----------|:-----------------------------|
| 1  | 2862      | 2248      | https://lichess.org/qmq5jjLs | <!-- 5110 -->
| 2  | 2514      | 2367      | https://lichess.org/7mOvUS5L | <!-- 4881 -->
| 3  | 2363      | 2517      | https://lichess.org/c5KIcUCa | <!-- 4880 --> 
| 4  | 2479      | 2326      | https://lichess.org/ZvlnHkhn | <!-- 4805 --> 
| 5  | 2352      | 2447      | https://lichess.org/8aFwXeYF | <!-- 4799 -->
| 6  | 2403      | 2379      | https://lichess.org/UwTxNNuz | <!-- 4782 -->
| 7  | 2341      | 2431      | https://lichess.org/WhcAk9EO | <!-- 4772 --> 
| 8  | 2383      | 2375      | https://lichess.org/hmc9VOHT | <!-- 4758 --> 
| 9  | 2323      | 2431      | https://lichess.org/j4vAQo7Q | <!-- 4754 --> 
| 10 | 2352      | 2334      | https://lichess.org/mM7hrE10 | <!-- 4686 --> 
| 11 | 2355      | 2304      | https://lichess.org/VCnhX6iV | <!-- 4659 -->
| 12 | 2335      | 2294      | https://lichess.org/arTrZnep | <!-- 4629 -->
| 13 | 2390      | 2224      | https://lichess.org/TJJxBOME | <!-- 4614 -->
| 14 | 2278      | 2328      | https://lichess.org/Oiy2Qrk5 | <!-- 4606 --> 
| 15 | 2500      | 2065      | https://lichess.org/miVmJFLE | <!-- 4565 -->
| 16 | 2264      | 2291      | https://lichess.org/NmuOry9E | <!-- 4555 -->
| 17 | 2172      | 2380      | https://lichess.org/91zlk8It | <!-- 4552 --> 
| 18 | 2294      | 2214      | https://lichess.org/jispyDUg | <!-- 4508 --> 
| 19 | 2240      | 2237      | https://lichess.org/PfpjpSEN | <!-- 4477 -->
| 20 | 2204      | 2273      | https://lichess.org/TJBgaLd8 | <!-- 4477 --> 
| 21 | 2292      | 2171      | https://lichess.org/yg4Wy7hg | <!-- 4463 -->
| 22 | 1871      | 2584      | https://lichess.org/cNXzfQZw | <!-- 4455 -->
| 23 | 2171      | 2281      | https://lichess.org/mnf9OrU7 | <!-- 4452 -->
| 24 | 2234      | 2187      | https://lichess.org/RiKaLX1J | <!-- 4421 --> 
| 25 | 2213      | 2199      | https://lichess.org/LsBtdUyD | <!-- 4412 -->   

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
