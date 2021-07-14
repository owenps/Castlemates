# Castlemates ♔♖ ♚♜
![Python Badge](https://img.shields.io/badge/Python-007396?style=for-the-badge&labelColor=black&logo=Python&logoColor=white) 

Castlemates is a python script which scrapes .pgn files for chess games ending in a checkmates from castling. This project was largely inspired by International Chess Master [Eric Rosen](https://twitter.com/im_rosen?lang=en) and the [Chessfactory Hall Of Fame](https://github.com/mark-dev/chessfactory-hall-of-fame) by Mark-Dev. 

If you enjoy the project and wish to show your support, leaving a ⭐ on the repository would really mean a lot!

<a href="https://lichess.org/CW7va6EJ" target="_blank"><img src="exampleCastlemate.gif" width=300></a>

## Data
Unfortunately parsing games using the [python chess](https://python-chess.readthedocs.io/en/latest/) library is quite slow. So `castlemates.py` contains a simplified-lightweight version designed specifically to find games which end in a castle checkmate. My findings scanned over 915 million games on the [Lichess game database](https://database.lichess.org/). 

Notable players include: [GM Aram Hakobyan](https://lichess.org/Liodos75), [GM Elier Miranda](https://lichess.org/7mOvUS5L), [GM Alder Escobar](https://lichess.org/PayfUL11), [GM Amin Tabatabaei](https://lichess.org/Liodos75), [GM Maxim Novik](https://lichess.org/RUbMpAYp), [GM Michael Hoffmann](https://lichess.org/fcuq5ZKc) [IM Vincent Rothuis](https://lichess.org/qmq5jjLs), [IM Martin Neyhebaver](https://lichess.org/ymm4Bysd), [IM Linus Johansson](https://lichess.org/PayfUL11), [IM Alexander Gutenev](https://lichess.org/QMGRl9em), [IM Thorbjorn Bromann](https://lichess.org/iY5epLL4), and more.

| Date                                                                                  | Games           | Size         | Castle Checkmates |
|:--------------------------------------------------------------------------------------|:----------------|:-------------|:------------------|
| [2021 June](https://github.com/owenps/Castlemates/blob/main/results/2021-06.txt)      | 92,190,803      | 206.53 GB    | 950               |
| [2021 May](https://github.com/owenps/Castlemates/blob/main/results/2021-05.txt)       | 101,011,629     | 232.21 GB    | 1,120             |
| [2021 Apirl](https://github.com/owenps/Castlemates/blob/main/results/2021-04.txt)     | 99,184,138      | 212.30 GB    | 1,096             |
| [2021 March](https://github.com/owenps/Castlemates/blob/main/results/2021-03.txt)     | 100,023,791     | 229.34 GB    | 1,092             |
| [2021 February](https://github.com/owenps/Castlemates/blob/main/results/2021-02.txt)  | 89,892,001      | 190.89 GB    | 995               |
| [2021 January](https://github.com/owenps/Castlemates/blob/main/results/2021-01.txt)   | 95,853,038      | 203.83 GB    | 996               |
| [2020 December](https://github.com/owenps/Castlemates/blob/main/results/2020-12.txt)  | 89,422,803      | 175.60 GB    | 902               |
| [2020 November](https://github.com/owenps/Castlemates/blob/main/results/2020-11.txt)  | 78,268,317      | 153.97 GB    | 811               |
| [2020 October](https://github.com/owenps/Castlemates/blob/main/results/2020-10.txt)   | 70,572,373      | 139.32 GB    | 679               |
| [2020 January](https://github.com/owenps/Castlemates/blob/main/results/2020-01.txt)   | 46,800,709      | 98.80 GB     | 387               |
| [2019 January](https://github.com/owenps/Castlemates/blob/main/results/2019-01.txt)   | 33,886,899      | 71.79 GB     | 352               |
| [2018 January](https://github.com/owenps/Castlemates/blob/main/results/2018-01.txt)   | 17,945,784      | 38.27 GB     | 181               |
| **Total**                                                                             | **915,052,285** | **1.952 TB** | **9,561**         |

## Highest Rated Games

| #  | White ELO | Black ELO | Game Reference URL           |   
|:---|:----------|:----------|:-----------------------------|
| 1  | 2914      | 2783      | https://lichess.org/Liodos75 | <!-- 5697 -->
| 2  | 2703      | 2732      | https://lichess.org/UUji58Ob | <!-- 5435 -->
| 3  | 2670      | 2700      | https://lichess.org/DEbahVgE | <!-- 5370 -->
| 4  | 2564      | 2680      | https://lichess.org/QMGRl9em | <!-- 5244 -->
| 5  | 2663      | 2572      | https://lichess.org/kDPj9PSW | <!-- 5235 -->
| 6  | 2615      | 2612      | https://lichess.org/PayfUL11 | <!-- 5227 -->
| 7  | 2620      | 2534      | https://lichess.org/ymm4Bysd | <!-- 5154 -->
| 8  | 2578      | 2541      | https://lichess.org/YTWwOiiq | <!-- 5119 -->
| 9  | 2541      | 2576      | https://lichess.org/Ba2j9nD6 | <!-- 5117 -->
| 10 | 2862      | 2248      | https://lichess.org/qmq5jjLs | <!-- 5110 -->
| 11 | 2609      | 2491      | https://lichess.org/k72rG9AE | <!-- 5100 -->
| 12 | 2608      | 2411      | https://lichess.org/fcuq5ZKc | <!-- 5019 -->
| 13 | 2506      | 2495      | https://lichess.org/Cebuf8nh | <!-- 5001 -->
| 14 | 2555      | 2435      | https://lichess.org/DdUehQfh | <!-- 4990 -->
| 15 | 2565      | 2420      | https://lichess.org/VLy0IkZE | <!-- 4985 -->
| 16 | 2431      | 2517      | https://lichess.org/TYM2NBeY | <!-- 4948 -->
| 17 | 2471      | 2462      | https://lichess.org/RUbMpAYp | <!-- 4933 -->
| 18 | 2464      | 2459      | https://lichess.org/Gtfook1c | <!-- 4923 -->
| 19 | 2484      | 2434      | https://lichess.org/iY5epLL4 | <!-- 4918 -->
| 20 | 2702      | 2216      | https://lichess.org/XYZzw71J | <!-- 4918 -->
| 21 | 2501      | 2410      | https://lichess.org/9npaIURi | <!-- 4911 -->
| 22 | 2574      | 2323      | https://lichess.org/Q1PxXkdJ | <!-- 4897 -->
| 23 | 2424      | 2470      | https://lichess.org/2NQ9q80H | <!-- 4894 -->
| 24 | 2410      | 2481      | https://lichess.org/Ugty2Ekd | <!-- 4891 -->
| 25 | 2283      | 2602      | https://lichess.org/wXlHlbvG | <!-- 4885 -->

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
