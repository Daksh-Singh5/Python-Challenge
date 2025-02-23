Game = {"7":"","8":"","9":"",
        "4":"","5":"","6":"",
        "1":"","2":"","3":"",
        }


gamekey = []

for key in Game:
    gamekey.append(key)

def makegame():
    
    print(Game["7"],"|",Game["8"],"|",Game["9"],"|")
    print("+-+-+-+-+")
    print(Game["4"],"|",Game["5"],"|",Game["6"],"|")
    print("+-+-+-+-+")
    print(Game["1"],"|",Game["2"],"|",Game["3"],"|")

makegame()


