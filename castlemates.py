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

minElo = 0
try: 
    minElo = int(sys.argv[2])
except ValueError:
    print("Invalid Parameter: The minimum Elo parameter must be a integer value")
    exit()
except IndexError: 
    pass

# Parse pgn files
pgn = open(fn)
game = chess.pgn.read_game(pgn)
castlemates = 0
count = 1
while game is not None:
    if count % 1e6 == 0:
        print('Progress Update: Game #'+str(count))
    lastmove = None
    try:
        lastmove = game.end().san()
    except AttributeError: # root node
        pass
    if lastmove == 'O-O#' or lastmove == 'O-O-O#': # Castle-mate found
        wElo, bElo = game.headers['WhiteElo'], game.headers['BlackElo']
        if (min(int(wElo),int(bElo)) >= minElo):
            castlemates += 1
            print('Castlemate Found! Game #'+str(count))
            print('White Elo: '+wElo+' | Black Elo: '+bElo+' | URL: '+game.headers['Site'])
    game = chess.pgn.read_game(pgn)
    count += 1
print('-- Scan Complete --')
print('In total there were '+str(castlemates)+' game(s) which ended in a castle-mate')
    

        