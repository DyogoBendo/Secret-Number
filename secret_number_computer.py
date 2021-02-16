from random import randint as rd

if __name__ == '__main__':
    begin = int(input("From what number do you want to guess?"))
    end = int(input("To what number do you want to guess?"))
    secret_number = rd(begin, end)
    tries = 1
    number_of_tries = int(input("What is the number of tries?"))
    guessed = False
    while tries <= number_of_tries and not guessed:
        guess_number = int(input(f"Insert a number from {begin} to {end}: "))
        if guess_number < secret_number:
            print("Try a bigger number!")
        elif guess_number > secret_number:
            print("Try a smaller number!")
        else:
            guessed = True
            break
        tries += 1
    if guessed:
        print(f"Congratulations! You won in {tries} tries!")
    else:
        print("Oh no! Try a new game!")
