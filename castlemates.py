import sys

# Handling command arguments
fn = ""
try:
    fn = sys.argv[1]
except IndexError:
    print("Parameter Missing: no parameter found. The script expects a .pgn file")
    exit()

if '.pgn' not in fn:
    print('Parameter Error: the parameter {} is invalid. A .pgn file is expected'.format(sys.argv[1]))
    exit()

batch = 1e6
try: 
    batch = int(sys.argv[2])
except ValueError:
    print("Invalid Parameter: The batch parameter must be a integer value")
    exit()
except IndexError: 
    pass

# Parse pgn files
pgn = open(fn)
game = castlemates = 0
while True: 
    line = pgn.readline()
    if not line: # eof
        break
    # Collect meta data from game
    if line[0] == '1': # Game Moves
        if 'O-O#' in line: # Castlemate found!
            castlemates += 1
            print('Castlemate Found! Game #{:,}'.format(game))
            print('White Elo: {} | Black Elo: {} | URL: {}'.format(wElo,bElo,site))
    elif line[:2] == '[S': # Site tag
        site = line[7:-3]
    elif line[:3] == '[Ev': # New Game
        game += 1
        site = wElo = bElo = None # Reset metadata
        if batch != 0 and game % batch == 0:
            print('Progress Update: Game #{:,}'.format(game))
    elif line[:7] == '[WhiteE': # WhiteElo tag 
        wElo = line[11:-3]
    elif line[:7] == '[BlackE': # BlackElo tag
        bElo = line[11:-3]

pgn.close()
print('-- Script Complete! --\nIn total there were {:,} game(s) from {} that ended in a castle-mate.'.format(castlemates,fn))