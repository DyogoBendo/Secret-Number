from random import randint as rd
from time import sleep

if __name__ == '__main__':
    begin = int(input("From what number do you want the computer to guess? "))
    end = int(input("To what number do you want the computer to guess? "))
    secret_number = int(input("Please, insert your secret number: "))
    tries = 1
    number_of_tries = int(input("How many tries will the computer have? "))
    guessed = False
    while tries <= number_of_tries and not guessed:
        guess_number = rd(begin, end)
        print(f"This is the try number {tries}")
        print(f"The computer range is from {begin} to {end}")
        print(f"The computer guess was: {guess_number}")
        print("-" * 30)
        if guess_number < secret_number:
            if begin < guess_number:
                begin = guess_number
        elif guess_number > secret_number:
            if end > guess_number:
                end = guess_number
        else:
            guessed = True
            break
        tries += 1
        sleep(2)
    if not guessed:
        print(f"Congratulations! You beated the computer!!")
    else:
        print("Oh no! Try a new game!")
