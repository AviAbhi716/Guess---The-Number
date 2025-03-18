import random
logo =r"""
   ________                                      __   .__                  _______    ____ ___        ___.                    
 /  _____/  __ __   ____    ______  ______    _/  |_ |  |__    ____       \      \  |    |   \ _____ \_ |__    ____ _______  
/   \  ___ |  |  \_/ __ \  /  ___/ /  ___/    \   __\|  |  \ _/ __ \      /   |   \ |    |   //     \ | __ \ _/ __ |\_  __ \ 
\    \_\  \|  |  /\  ___/  \___ \  \___ \      |  |  |   Y  |\  ___/     /    |    \|    |  /|  Y Y  \| \_\ |\  ___/ |  | \/ 
 \______  /|____/  \___  >/____  >/____  >     |__|  |___|  / \___  >    \____|__  /|______/ |__|_|  /|___  / \___  >|__|    
        \/             \/      \/      \/                 \/      \/             \/                \/     \/      \/       """
print(logo)
print("Let us guess the number between 1 to 50")
EASY=10
HARD=5
num=random.randint(1,50)
def difficulty(l):
    if l=='easy':
        return EASY
    elif l=='hard':
        return HARD
    else:
        print("Enter correct difficulty level")
        guess()
def loop(att):
    while att!=0:
        choose = int(input("Make a Guess:"))
        att=game(choose,att)
        if att==0:
            print("You are out of guesses...You lose")
            return
        elif att==-1:
            return
        else:
            print(f"You have {att} attempts remaining to guess the number!")
            print("Guess again")

def game(choose1,val):
    if num==choose1:
        print("You win")
        val=-1
        return val
    elif choose1<num:
        print("Your guess was too low")
        return val-1
    else:
        print("You guess was too high")
        return val-1
def guess():
    level=input("Choose level of difficulty.....Type 'easy' or 'hard':").lower()
    attempts=difficulty(level)
    print(f"You have {attempts} attempts remaining to guess the number!")
    loop(attempts)
guess()
