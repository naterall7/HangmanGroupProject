# importing tkinter
import tkinter as tk

import random

# window = tk.Tk()
# window.title("Hangman")

# frame = tk.Frame(master=window, relief="sunken", width=100, height=100)
# frame.pack()
# label = tk.Label(master=frame, text="")
# label.pack()

# def submit_guess():
#     print(label["text"])

# button = tk.Button(master=frame, relief="raised", text="Submit", bg="red", fg="white", width=5, height=5, command=submit_guess)
# button.pack()

# def update(label, text):
#     label.config(text=text)

# def handle_keypress(event):
#     key = event.char
#     update(label, key)

# window.bind("<Key>", handle_keypress)
# window.mainloop()

def intro():
    while True:
        played = input("Welcome Player 1, have you ever played hangman before (yes/no)? ")
        if played == "yes":
            while True:
                ready = input("Are you ready to play(yes/no)? ")
                if ready == "yes":
                    print("Great, let's play!")
                    hangman()
                    break
                elif ready == "no":
                    closing1()
                    break
                else:
                    print("Please type 'yes' or 'no'!")
                    continue
            break
        elif played == "no":
            print("Don't worry, it's easy! There will be a secret word picked from a list of words.") 
            print("You, the player, must guess the secret word, letter by letter.")
            print("For each wrong letter guessed, there will be a part of a drawing of a man.")
            print("If the drawing of the man is completed before the word is guessed, you lose.")
            print("If the word is guessed before the drawing is completed, you win!")
            while True:
                ready_now = input("Are you ready to play now (yes/no)? ")
                if ready_now == "yes":
                    print("Great, let's play!")
                    hangman()
                    break
                elif ready_now == "no":
                    closing1()
                    break
                else:
                    print("Please type 'yes' or 'no'!")
                    continue
            break
        else:
            print("Please type 'yes' or 'no'!")
            continue

def closing1():
    print("Alright, I'll be here when you're ready!")
    print("*silently waves goodbye*")

def closing2():
    print("Thanks for playing!")
    while True:
        again = input("Would you like to play again (yes/no)? ")
        if again == "yes":
            print("Great, let's play!")
            hangman()
            break
        elif again == "no":
            print("Alright, see you next time!")
            print("*silently waves goodbye*")
            break
        else:
            print("Please type 'yes' or 'no'!")
            continue

word_bank = ["prettiest","close","massive","hollow","cultured","seashore","explode","dizzy","minister","competent",
"thoughtful","harbor","tidy","dance","children","zesty","clean","ball","nostalgic","plan","week","strap","board",
"slope","bat","steep","mourn","cat","girl","ancient","street","mice","dare","wasteful","tub","limping","whimsical",
"eager","eggs","detail","experience","beds","train","place","cows","admit","rare","respect","loose","group","enjoy",
"internal","macabre","imported","crooked","confused","hug","unkempt","coal","meddle","hapless","country","zealous",
"sick","pray","lake","tiny","key","empty","labored","delirious","ants","need","omniscient","onerous","damp","subtract",
"sack","connection","toad","gather","record","new","trashy","flow","river","sparkling","kneel","daughter","glue",
"allow","raspy","eminent","weak","wrong","pretend","receipt","celery","plain","fire","heal","damaging","honorable",
"foot","ignorant","substance","crime","giant","learned","itchy","smoke","station","jaded","innocent"]

def select_random_word():
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def letter_guess(word):
    guessed_letters = set()
    while True:
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print("Good job! You guessed a letter correctly.")
        else:
            print("Sorry, that letter is not in the word.")
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

def hangman():
    selected_word = select_random_word()
    print("The word has", len(selected_word), "letters.")
    letter_guess(selected_word)
    closing2()