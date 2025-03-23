import random as r

numOfDigits = int(input("Enter how many digits you want in your password: "))

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
SpecialChar = ["!","@","#","$"]
num = ["1","2","3","4","5","6","7","8","9","0"]
all = [letters,SpecialChar,num]
result =""
for i in range(numOfDigits):
    choise = r.choice(all)   
    if choise == letters:
        letterchoice = r.choice(letters)
    elif choise == num:
        numchoice = r.choice(num)
        result += numchoice
    else:
        SpecialCharchoice = r.choice(SpecialChar)
        result += str(SpecialCharchoice)

print("the strongset password is",result)
