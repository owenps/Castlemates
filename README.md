# Castlemates ♔♖ ♚♜
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev. 

If you enjoy the project and wish to show your support, leaving a ⭐ on the repository would really mean a lot!

<a href="https://lichess.org/CW7va6EJ" target="_blank"><img src="exampleCastlemate.gif" width=300></a>

## Data
Unfortunately parsing games using the [python chess](https://python-chess.readthedocs.io/en/latest/) library is quite slow. So `castlemates.py` contains a simplified-lightweight version designed specifically to find games which end in a castle checkmate. My findings scanned over 490 million games on the [Lichess game database](https://database.lichess.org/). Notable players include: [GM Elier Miranda](https://lichess.org/7mOvUS5L), [GM Alder Escobar](https://lichess.org/PayfUL11), [IM Vincent Rothuis](https://lichess.org/qmq5jjLs), [IM Martin Neyhebaver](https://lichess.org/ymm4Bysd), [IM Linus Johansson](https://lichess.org/PayfUL11).

| Date                                                                                  | Games           | Size         | Castle Checkmates |
|:--------------------------------------------------------------------------------------|:----------------|:-------------|:------------------|
| *More Games Coming Soon!*                                                             | -               | -            | -                 |
| [2021 June](https://github.com/owenps/Castlemates/blob/main/results/2021-06.txt)      | 92,190,803      | 206.53 GB    | 950               |
| [2021 May](https://github.com/owenps/Castlemates/blob/main/results/2021-05.txt)       | 101,011,629     | 232.21 GB    | 1,120             |
| [2021 Apirl](https://github.com/owenps/Castlemates/blob/main/results/2021-04.txt)     | 99,184,138      | 212.30 GB    | 1,096             |
| [2021 March](https://github.com/owenps/Castlemates/blob/main/results/2019-01.txt)     | 100,023,791     | 229.34 GB    | 1,092             |
| [2020 January](https://github.com/owenps/Castlemates/blob/main/results/2019-01.txt)   | 46,800,709      | 98.80 GB     | 387               |
| [2019 January](https://github.com/owenps/Castlemates/blob/main/results/2019-01.txt)   | 33,886,899      | 71.79 GB     | 352               |
| [2018 January](https://github.com/owenps/Castlemates/blob/main/results/2018-01.txt)   | 17,945,784      | 38.27 GB     | 181               |
| **Total**                                                                             | **491,043,753** | **1.089 TB** | **5,178**         |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL           |   
|:---|:----------|:----------|:-----------------------------|
| 1  | 2703      | 2732      | https://lichess.org/UUji58Ob | <!-- 5435 -->
| 2  | 2670      | 2700      | https://lichess.org/DEbahVgE | <!-- 5370 -->
| 3  | 2663      | 2572      | https://lichess.org/kDPj9PSW | <!-- 5235 -->
| 4  | 2615      | 2612      | https://lichess.org/PayfUL11 | <!-- 5227 -->
| 5  | 2620      | 2534      | https://lichess.org/ymm4Bysd | <!-- 5154 -->
| 6  | 2862      | 2248      | https://lichess.org/qmq5jjLs | <!-- 5110 -->
| 7  | 2609      | 2491      | https://lichess.org/k72rG9AE | <!-- 5100 -->
| 8  | 2506      | 2495      | https://lichess.org/Cebuf8nh | <!-- 5001 -->
| 9  | 2555      | 2435      | https://lichess.org/DdUehQfh | <!-- 4990 -->
| 10 | 2565      | 2420      | https://lichess.org/VLy0IkZE | <!-- 4985 -->
| 11 | 2702      | 2216      | https://lichess.org/XYZzw71J | <!-- 4918 -->
| 12 | 2574      | 2323      | https://lichess.org/Q1PxXkdJ | <!-- 4897 -->
| 13 | 2410      | 2481      | https://lichess.org/Ugty2Ekd | <!-- 4891 -->
| 14 | 2283      | 2602      | https://lichess.org/wXlHlbvG | <!-- 4885 -->
| 15 | 2514      | 2367      | https://lichess.org/7mOvUS5L | <!-- 4881 -->
| 16 | 2363      | 2517      | https://lichess.org/c5KIcUCa | <!-- 4880 -->
| 17 | 2411      | 2469      | https://lichess.org/iGBXYTk4 | <!-- 4880 --> 
| 18 | 2433      | 2422      | https://lichess.org/kVE2ra4W | <!-- 4855 -->
| 19 | 2375      | 2435      | https://lichess.org/FpZIl5Mb | <!-- 4810 -->
| 20 | 2479      | 2326      | https://lichess.org/ZvlnHkhn | <!-- 4805 --> 
| 21 | 2352      | 2447      | https://lichess.org/8aFwXeYF | <!-- 4799 -->
| 22 | 2403      | 2379      | https://lichess.org/UwTxNNuz | <!-- 4782 -->
| 23 | 2341      | 2431      | https://lichess.org/WhcAk9EO | <!-- 4772 --> 
| 24 | 2375      | 2391      | https://lichess.org/ddhQZ1ag | <!-- 4766 -->
| 25 | 2383      | 2375      | https://lichess.org/hmc9VOHT | <!-- 4758 --> 

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
