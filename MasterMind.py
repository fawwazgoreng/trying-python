import  random
import sys

print("hello! lets go playing master mind game")

life = 0
result = ['']
right_number = ''

def initiate():
    global life , right_number , result
    life = 5
    result = ["x", "x", "x", "x"]
    right_number = str(random.randint(1000, 9999))
    print(right_number)

def play_again():
    global life , result , right_number
    ask = input("want to play again? y/n : ")
    if ask.lower() == "y":
        initiate()
        return True
    else:
        print("thank you for playing")
        sys.exit()

def main():
    global life
    if life > 0:
        print("guest number ")
        clue = ""
        for index in range(0, 4):
            clue = clue + " " + str(result[index]).upper()
        print("you have " + str(life) + " change")
        print(clue)
        guess_number = str(input("enter your guess : "))
        life -= 1
        if len(guess_number) != 4:
            print("please input valid number")
        else :
            if guess_number == right_number:
                print("you win")
                play_again()
            else :
                for index in range(0, 4):
                    if guess_number[index] == right_number[index]:
                        result[index] = str(guess_number[index])
    else:
        play_again()

initiate()
while True :
    main()
