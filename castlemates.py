import sys
import chess.pgn

# Handling command arguments
fn = ""
try:
    fn = sys.argv[1]
except IndexError:
    print("Parameter Missing: no parameter found. The script expects a .pgn file")
    exit()

if '.pgn' not in fn:
    print('Parameter Error: the parameter '+sys.argv[1]+' is invalid. A .pgn file is expected')
    exit()

min_elo = 0
try: 
    min_elo = int(sys.argv[2])
except ValueError:
    print("Invalid Parameter: The minimum Elo parameter must be a integer value")
    exit()
except IndexError: 
    pass

# Parse pgn files
pgn = open(fn)
game = chess.pgn.read_game(pgn)
castlemates = []
while game is not None:
    lastmove = game.end().san()
    if lastmove == 'O-O#' or lastmove == 'O-O-O#':
        castlemates.append(game)
    game = chess.pgn.read_game(pgn)

# Print results
for game in castlemates:
    wElo, bElo = game.headers['WhiteElo'], game.headers['BlackElo']
    if (wElo != '?' or bElo != '?'):
        if (min(int(wElo),int(bElo)) > min_elo):
            print('White Elo: '+wElo+' | Black Elo: '+bElo+' | URL: '+game.headers['Site'])
    elif (min_elo == 0): # show all games
        print('White Elo: '+wElo+' | Black Elo: '+bElo+' | URL: '+game.headers['Site'])
print('In total there were '+str(len(castlemates))+' game(s) which ended in a castle-mate')
    

        