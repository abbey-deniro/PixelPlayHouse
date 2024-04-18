import random
import string
from hangman_visual import lives_visual_dict


def main():
    welcome = ['\nWelcome to Hangman! A word will be chosen at random and',
            'you must try to guess the word correctly letter by letter',
            'before you run out of attempts. Good luck!']
    
    for line in welcome:
        print(line, sep="\n")

    play_again = True

    while play_again:

        words = ["whisper", "journey", "cascade", "rhythm", "twilight", "emerald",
                "melody", "phoenix", "nostalgia", "canvas", "labyrinth",
                "dunes", "crescent", "oasis", "flicker", "compass",
                "vista", "genesis", "ember", "prism", "wistful",
                "azure", "serene", "tranquil"] 

        word = random.choice(words).upper();
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        letters_guessed = set()

        lives = 7

        # get user input
        while len(word_letters) > 0 and lives > 0:
            print('\nYou have ', lives, ' lives left and you have used these letters: ', ' '.join(letters_guessed))

            word_list = [letter if letter in letters_guessed else '-' for letter in word]
            print(lives_visual_dict[lives])
            print('Current word: ', ' '.join(word_list))

            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - letters_guessed:
                letters_guessed.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('')

                else: lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')
            
            elif letters_guessed in letters_guessed:
                print('\nYou have already used that letter. Guess another letter.')
            
            else:
                print('\nThat is not a valid letter.')
        
        if lives == 0:
            play_again = False
            print(lives_visual_dict[lives])
            print("You died, sorry. The word was", word)
        else:
            print("YAY!!!! You guessed the word correctly. Word: ", word, "!!!")



if __name__ == "__main__":
    main();

