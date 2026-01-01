import random
import sys

def ask_confirm(msg = "are you sure?"):
    print(msg)
    print("please input yes or no")
    answer = input("")
    if answer.lower() == "yes" or answer.lower() == "y":
        return main()
    else :
        sys.exit()

def main () :
    print("Hi! lest go playing guess a number")
    low = int(input("please bind lower number "))
    high = int(input("please bind higher number "))
    if low > high:
        print("please bind high number higher than low number")
    number = random.randint(low, high)
    change = 3
    while change > 0 :
        guess = int(input("please input guess number "))
        if guess == number:
            print("you guessed right")
            break
        elif guess >= number :
            change = change - 1
            print(f"your number to high your change is {change}")
        else :
            change = change - 1
            print(f"your number to low your change is {change}")
    print(f"right number is {number}")
while True:
    main()
    ask_confirm("want to play again")