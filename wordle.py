import time
import random
import sys

import database as db

class wordle:

    def __init__(self, word_length=5, dictionary="words5.txt"):
        self.dictionary = db.database(word_length, dictionary)
        self.guesses_count = word_length
        self.word_length = word_length
        self.wordle_template = []
        for i in range(word_length):
            self.wordle_template.append("___ " * word_length)
        self.player_guesses = []
        self.selected_word = ""
        self.red = []
        self.green = []
        self.yellow = []

    def animate_intro(self):
        title = "\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Wordle!"
        description = f"\t\t\t\t\t\t\tYou have {self.word_length} chances to guess the word.\n\t\tAfter each guess, you will be told which letters are not in the word,\n\twhich letters are in correct position, and which letters are in good position.\n\n\t\t\t\t\t\t\t\t\t\t\t\tGood luck!"
        for i in range(len(title)):
            print(title[i], end="", flush=True)
            # time.sleep(0.1)
        print()
        for i in range(len(description)):
            print(description[i], end="", flush=True)
            # time.sleep(0.05)
    
    def select_random_word(self):
        l = len(self.dictionary.search_database)
        self.selected_word = self.dictionary.search_database[random.randint(0, l-1)]
    
    def print_framework(self):
        print("\n\n")
        for i in range(self.word_length):
            print(self.wordle_template[i])
        print(f"\nYou have {self.guesses_count} guesses left.\n")

    def get_guess(self):
        print(f"Enter a {self.word_length} letter word: ", end="")
        guess = input().lower()
        if(len(guess) != self.word_length):
            print("Invalid guess. Try again.")
            return self.get_guess()
        if(guess in self.player_guesses):
            print("You already guessed that word. Try again.")
            return self.get_guess()
        if(self.valid(guess) == False):
            print("Not a real word. Try again.")
            return self.get_guess()
        
        self.player_guesses.append(guess)
        return guess

    def valid(self, guess):
        hash_num = self.dictionary.hash_number(guess)
        if guess in self.dictionary.database[hash_num]:
            return True
        else:
            return False

    def check_guess(self, guess):
        word = self.selected_word
        i = 0

        if(guess == word):
            return self.win()
        else:
            for w in guess:
                if w in word:
                    if w == word[i]:
                        if w not in self.green:
                            self.green.append(w)
                        if w in self.yellow:
                            self.yellow.remove(w)
                    else:
                        if w not in self.yellow and w not in self.green:
                            self.yellow.append(w)
                    word = word.replace(w, " ", 1)
                elif w not in word:
                    if w not in self.red:
                        self.red.append(w)
                i +=1
    
    def incorporate_guess(self, guess):
        j = 0
        for line in self.wordle_template:
            if line == "___ " * self.word_length:
                for i in range(self.word_length):
                    line = line.replace("___ ", "_" + guess[i] + "_ ", 1)
                self.wordle_template[j] = line
                break
            j += 1

    def win(self):
        print("You win!")
        print(f"The word was {self.selected_word}")
        sys.exit()
    
    def lose(self):
        print("You lose!")
        print(f"The word was {self.selected_word}")
        sys.exit()
    

def main():

    if(len(sys.argv) > 1):
        dictionary = sys.argv[1]
        word_length = int(sys.argv[2])
        game = wordle(word_length, dictionary)
    else:
        game = wordle()
    
    game.animate_intro()

    game.select_random_word()

    print(game.selected_word)

    while(game.guesses_count > 0):
        game.print_framework()
        guess = game.get_guess()
        game.check_guess(guess)
        print(f"\nLetters in word at correct position: {game.green}")
        print(f"Letters in wrong position: {game.yellow}")
        print(f"Letters not in word: {game.red}")
        game.guesses_count -= 1
        game.incorporate_guess(guess)
    game.lose()


if __name__ == "__main__":
    main()
