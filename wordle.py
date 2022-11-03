import time
import random
import sys

class wordle:

    dictionary = "words5.txt"   # default
    word_length = 5             # default

    def animate_intro():
        title = "Welcome to Wordle!"
        description = "\t\t\t\t\t\t\tYou have 5 chances to guess the word.\n\t\tAfter each guess, you will be told which letters are not in the word,\n\twhich letters are in correct position, and which letters are in good position.\n\n\t\t\t\t\t\t\t\tGood luck!"
        for i in range(len(title)):
            print(title[i], end="", flush=True)
            time.sleep(0.1)
        print()
        for i in range(len(description)):
            print(description[i], end="", flush=True)
            time.sleep(0.05)

    def load_database():
        dictionary = database(word_length, dictionary)
    
    def select_random_word():
        h = random.randint(0, 26*26*26)
        if(len(dictionary.database[h]) == 0):
            select_random_word()
        word = dictionary.database[h][random.randint(0, len(dictionary.database[h])-1)]
        return word

    
def main():
    if(len(sys.argv) > 1):
        dictionary = sys.argv[1]
        word_length = int(sys.argv[2])
    
    wordle.animate_intro()

    wordle.load_database()

    selected_word = wordle.select_random_word()

    print(selected_word)


if __name__ == "__main__":
    main()
