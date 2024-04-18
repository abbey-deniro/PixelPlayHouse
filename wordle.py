import random

five_letter_words = [
    "apple", "blast", "crisp", "dwarf", "eagle", "flask", "grasp", "hover", "ideal", "jolly",
    "knoll", "light", "mirth", "night", "ocean", "pride", "quilt", "rover", "swarm", "tiger",
    "umbra", "vivid", "woven", "xerox", "yacht", "zebra", "query", "jumps", "vocal", "lunch",
    "boxer", "young", "watch", "virus", "ulcer", "token", "ridge", "quick", "pluck", "opera",
    "nylon", "mossy", "lemon", "kneel", "image", "humor", "globe", "fever", "elbow", "dodge"
]

def check_word(five_letter_words):
    wordle = random.choice(five_letter_words)
    attempt = 6
    while attempt > 0:
        guess = str(input("\nGuess the word: "))
        word_dic = []
        if guess == wordle:
            print("YAY! you guess the word correctly!!")
            break
        else:
            attempt = attempt - 1
            for char, word in zip(wordle, guess):
                if word in wordle and word in char:
                    # print(f"\u001b[32m {word} \u001b[0m")
                    word_dic.append((word, "green"))
                elif word in wordle:
                    word_dic.append((word, "white"))
                else:
                    word_dic.append((word, "red"))
        
        for key, value in word_dic:
            if value == "green":
                print(f"\u001b[32m{key}\u001b[0m", end=" ")
            elif value == "white":
                print(f"\u001b[0m{key}\u001b[0m", end=" ")
            elif value == "red":
                print(f"\u001b[31m{key}\u001b[0m", end=" ")
        print(f"\nYou have {attempt} attempt(s) left")
    print(f"Oh no! You did'nt guess the word. The secret word was {wordle}")


def welcome():
    print("Welcome to PyWordle! Your goal is to guess a secret 5 letter word in 6 tries or less!\n" +
        "After each guess, you will receive feedback in the form of colored tiles, indicating how close your guess was to the word")
    print("\nGreen: A letter is exactly right, both in value and position.")
    print("Yellow: A letter is correct but in the wrong position.")
    print("White: A letter is not in the word in any spot.")

def wordle():
    welcome()
    check_word(five_letter_words)



if __name__ == "__main__":
    wordle()

