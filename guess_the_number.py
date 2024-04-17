import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Hint: too low!')
        elif guess > random_number:
            print('Sorry, guess again. Hint: too high!')
    
    print(f'Yay, congratulations! You guess the {random_number} correctly!')

def choose_diff():

    level = input("Choose a Difficulty: Easy | Medium | Hard: \n")

    if level.lower().__contains__("easy"):
        guess(10)
    elif level.lower().__contains__("medium"):
        guess(100)
    elif level.lower().__contains__("hard"):
        guess(1000)
    else:
        print("Sorry, choose a level.")

if __name__ == "__main__":
    choose_diff()