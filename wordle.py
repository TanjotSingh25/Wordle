import time
import random
import sys

import database as db

class wordle:

    dictionary = "words5.txt"           # default
    word_length = 5                     # default
    Guesses = ["___ ___ ___ ___ ___\n", "___ ___ ___ ___ ___\n", "___ ___ ___ ___ ___\n", "___ ___ ___ ___ ___\n", "___ ___ ___ ___ ___\n"]      # default

    def animate_intro():
        title = "\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Wordle!"
        description = "\t\t\t\t\t\t\tYou have 5 chances to guess the word.\n\t\tAfter each guess, you will be told which letters are not in the word,\n\twhich letters are in correct position, and which letters are in good position.\n\n\t\t\t\t\t\t\t\t\t\t\t\tGood luck!"
        for i in range(len(title)):
            print(title[i], end="", flush=True)
            # time.sleep(0.1)
        print()
        for i in range(len(description)):
            print(description[i], end="", flush=True)
            # time.sleep(0.05)

    def load_database():
        wordle.dictionary = db.database(wordle.word_length, wordle.dictionary)
        return wordle.dictionary
    
    def select_random_word(dictionary):
        l = len(dictionary.search_database)
        return dictionary.search_database[random.randint(0, l-1)]
    
    def print_framework():
        print("\n\n")
        for i in range(5):
            print(wordle.Guesses[i], end="")
        print("")
        print(f"You have {wordle.guess_count} guesses left.\n")

    def get_guess(old_guesses, database):
        print(f"Enter a {wordle.word_length} letter word: ", end="")
        guess = input()
        if(len(guess) != wordle.word_length):
            print("Invalid guess. Try again.")
            return wordle.get_guess()
        if(guess in old_guesses):
            print("You already guessed that word. Try again.")
            return wordle.get_guess()
        if(wordle.valid(database, guess) == False):
            print("Not a real word. Try again.")
            return wordle.get_guess()
        
        return guess

    def valid(database, word):
        hash_num = database.hash_number(word)
        if word in database.database[hash_num]:
            return True
        else:
            return False

    def check_guess(guess, word):
        word_temp = word
        red = ""
        green = ""
        yellow = ""
        i = 0

        if(guess == word):
            return True
        else:
            for w in guess:
                if w in word:
                    if w == word[i]:
                        green += w
                    else:
                        yellow += w
                    word = word.replace(w, "", 1)
                if w not in word_temp:
                    red += w
                i +=1
        return red, green, yellow

def main():

    imput_guesses = []

    if(len(sys.argv) > 1):
        wordle.dictionary = sys.argv[1]
        wordle.word_length = int(sys.argv[2])
    
    wordle.animate_intro()

    database = wordle.load_database()

    selected_word = wordle.select_random_word(database)

    wordle.print_framework()

    




    



if __name__ == "__main__":
    main()
