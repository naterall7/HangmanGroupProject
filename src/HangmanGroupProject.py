# importing tkinter
import tkinter as tk


#guessing system


import random
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

hangman()


# introductory code
def intro():
    played = input("Welcome Player 1, have you ever played hangman before (yes/no)? ")
    if played == "yes":
        ready = input("Are you ready to play(yes/no)? ")
        if ready == "yes":
            print("Great, let's play!")
        if ready == "no":
            print("Too bad!")
    if played == "no":
        print("Don't worry, it's easy! There will be a secret word picked from a list of words.") 
        print("You, the player, must guess the secret word, letter by letter.")
        print("For each wrong letter guessed, there will be a part of a drawing of a man.")
        print("If the drawing of the man is completed before the word is guessed, you lose.")
        print("If the word is guessed before the drawing is completed, you win!")
        ready_now = input("Are you ready to play now (yes/no)? ")
        if ready_now == "yes":
            print("Great, let's play!")
        if ready_now == "no":
            print("Too bad!")

intro()

# keypress functions
window = tk.Tk()
window.title("Hangman")

frame = tk.Frame(master=window, relief="sunken", width=100, height=100)
frame.pack()
label = tk.Label(master=frame, text="")
label.pack()

def submit_guess():
    print(label["text"])

button = tk.Button(master=frame, relief="raised", text="Submit", bg="red", fg="white", width=5, height=5, command=submit_guess)
button.pack()

def update(label, text):
    label.config(text=text)

def handle_keypress(event):
    key = event.char
    update(label, key)

window.bind("<Key>", handle_keypress)
window.mainloop()

import tkinter as tk
window1 = tk.Tk()

canvas = tk.Canvas(borderwidth=4, relief="ridge", height=200, width=300, bg="white")
canvas.pack()
head = canvas.create_oval(150,30,250,130, outline = "black", fill = "white", width = 2)

keyboard = tk.Frame(height=250, width=300, bg="black", borderwidth=4, relief="ridge")
keyboard.pack()
Qbutton = tk.Button(master=keyboard, text="Q", height=1, width=1)
Qbutton.place(x=1, y=1)
Wbutton = tk.Button(master=keyboard, text="W", height=1, width=1)
Wbutton.place(x=21, y=1)
Ebutton = tk.Button(master=keyboard, text="E", height=1, width=1)
Ebutton.place(x=41, y=1)
Rbutton = tk.Button(master=keyboard, text="R", height=1, width=1)
Rbutton.place(x=61, y=1)
Tbutton = tk.Button(master=keyboard, text="T", height=1, width=1)
Tbutton.place(x=81, y=1)
Ybutton = tk.Button(master=keyboard, text="Y", height=1, width=1)
Ybutton.place(x=101, y=1)
Ubutton = tk.Button(master=keyboard, text="U", height=1, width=1)
Ubutton.place(x=121, y=1)
Ibutton = tk.Button(master=keyboard, text="I", height=1, width=1)
Ibutton.place(x=141, y=1)
Obutton = tk.Button(master=keyboard, text="O", height=1, width=1)
Obutton.place(x=161, y=1)
Pbutton = tk.Button(master=keyboard, text="P", height=1, width=1)
Pbutton.place(x=181, y=1)

Abutton = tk.Button(master=keyboard, text="A", height=1, width=1)
Abutton.place(x=11, y=30)
Sbutton = tk.Button(master=keyboard, text="S", height=1, width=1)
Sbutton.place(x=31, y=30)
Dbutton = tk.Button(master=keyboard, text="D", height=1, width=1)
Dbutton.place(x=51, y=30)
Fbutton = tk.Button(master=keyboard, text="F", height=1, width=1)
Fbutton.place(x=71, y=30)
Gbutton = tk.Button(master=keyboard, text="G", height=1, width=1)
Gbutton.place(x=91, y=30)
Hbutton = tk.Button(master=keyboard, text="H", height=1, width=1)
Hbutton.place(x=111, y=30)
Jbutton = tk.Button(master=keyboard, text="J", height=1, width=1)
Jbutton.place(x=131, y=30)
Kbutton = tk.Button(master=keyboard, text="K", height=1, width=1)
Kbutton.place(x=151, y=30)
Lbutton = tk.Button(master=keyboard, text="L", height=1, width=1)
Lbutton.place(x=171, y=30)

Enterbutton = tk.Button(master=keyboard, text="Submit", height=1, width=2)
Enterbutton.place(x=1, y=59)
Zbutton = tk.Button(master=keyboard, text="Z", height=1, width=1)
Zbutton.place(x=31, y=59)

window1.mainloop()