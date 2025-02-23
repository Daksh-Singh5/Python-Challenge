Game = {"7":"","8":"","9":"",
        "4":"","5":"","6":"",
        "1":"","2":"","3":"",
        }


gamekey = []

for key in Game:
    gamekey.append(key)

def makegame(Game):
    
    print(Game["7"],"|",Game["8"],"|",Game["9"],)
    print("+-+-+-")
    print(Game["4"],"|",Game["5"],"|",Game["6"])
    print("+-+-+-")
    print(Game["1"],"|",Game["2"],"|",Game["3"])
def play():
    turn="X"
    chances = 0
    for i in range(10):

        makegame(Game)
        print("which place do u want to play at")
        place = input()
        
        if Game[place]=="":
            Game[place]=turn
            chances +=1
        else:
            print("The place is already filled try again")
            continue
        
        if chances >=5:
            if Game["7"]==Game["8"]==Game["9"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["4"]==Game["5"]==Game["6"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["1"]==Game["2"]==Game["3"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["7"]==Game["4"]==Game["1"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["2"]==Game["5"]==Game["8"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["3"]==Game["6"]==Game["9"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["1"]==Game["5"]==Game["9"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
            elif Game["3"]==Game["5"]==Game["7"]!="":
                makegame(Game)
                print("Game over ")
                print("*****",turn,"won*****")
                break
        if chances == 9:
            print("game over it a tie")    
        if turn == "X":
            turn =="O"
        else:
            turn =="X"

play()