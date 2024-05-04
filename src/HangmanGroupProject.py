import tkinter as tk
window1 = tk.Tk()
window1.title("Hangman")

canvas = tk.Canvas(borderwidth=4, relief="ridge", height=200, width=300, bg="white")
canvas.pack()


def keypress(event):
    key = event.char
    entry_box.config(text=key)

def submit_letter(): 
    letter = entry_box["text"]
    return letter

def enter(event): #just to make sure keyboard and window button do same thing
    submit_letter()

def delete(event):
    entry_box.config(text="")
def deletion():
    entry_box.config(text="")

def window_keypress(letter):
    entry_box.config(text=letter)

window1.bind("<Key>", keypress)
window1.bind("<Return>", enter)
window1.bind("<BackSpace>", delete)

top_post = canvas.create_line(75,20,125,20, fill="black", width=2)
head_connect = canvas.create_line(125,20,125,40, fill="black", width=2)
pole = canvas.create_line(75,20,75,200, fill="black", width=2)
base = canvas.create_line(60,200,90,200, fill="black", width=2)

# head = canvas.create_oval(105,40,145,80, outline="black", fill="white", width=2)
# body = canvas.create_line(125,80,125,140, fill="black", width=2)
# left_leg = canvas.create_line(125,140,105,160, fill="black", width=2)
# right_leg = canvas.create_line(125,140,145,160, fill="black", width=2)
# left_arm = canvas.create_line(125,90,100,110, fill="black", width=2)
# right_arm = canvas.create_line(125,90,150,110, fill="black", width=2)
# mouth = canvas.create_line(115,70,135,70, fill="black", width=2)
# #   The following make up the left eye
# canvas.create_line(113,50,123,60, fill="black", width=2)
# canvas.create_line(123,50,113,60, fill="black", width=2)
# #   The following make up the right eye
# canvas.create_line(137,50,127,60, fill="black", width=2)
# canvas.create_line(127,50,137,60, fill="black", width=2)

# loss = canvas.create_text(230,30, text="YOU LOSE!", font=40, fill="red")
# canvas.create_text(195,70, text="W", font=30, fill="red")
# canvas.create_text(225,70, text="P", font=30, fill="red")
# canvas.create_text(255,70, text="U", font=30, fill="red")
# canvas.create_text(195,100, text="A", font=30, fill="red")
# canvas.create_text(225,100, text="D", font=30, fill="red")
# canvas.create_text(255,100, text="L", font=30, fill="red")
# canvas.create_text(195,130, text="H", font=30, fill="red")
# canvas.create_text(225,130, text="F", font=30, fill="red")
# canvas.create_text(255,130, text="I", font=30, fill="red")

word_label = tk.Label(text="", relief="ridge", borderwidth=4, bg="white", width=17)
word_label.pack()

entry_box = tk.Label(text="", borderwidth=4, bg="white", relief="ridge", width=17)
entry_box.pack()

keyboard = tk.Frame(height=95, width=300, bg="black", borderwidth=4, relief="ridge")
keyboard.pack()

Qbutton = tk.Button(master=keyboard, text="Q", height=1, width=2, command=lambda: window_keypress("q"))
Qbutton.place(x=12, y=1)
Wbutton = tk.Button(master=keyboard, text="W", height=1, width=2, command=lambda: window_keypress("w"))
Wbutton.place(x=39, y=1)
Ebutton = tk.Button(master=keyboard, text="E", height=1, width=2, command=lambda: window_keypress("e"))
Ebutton.place(x=66, y=1)
Rbutton = tk.Button(master=keyboard, text="R", height=1, width=2, command=lambda: window_keypress("r"))
Rbutton.place(x=93, y=1)
Tbutton = tk.Button(master=keyboard, text="T", height=1, width=2, command=lambda: window_keypress("t"))
Tbutton.place(x=120, y=1)
Ybutton = tk.Button(master=keyboard, text="Y", height=1, width=2, command=lambda: window_keypress("y"))
Ybutton.place(x=147, y=1)
Ubutton = tk.Button(master=keyboard, text="U", height=1, width=2, command=lambda: window_keypress("u"))
Ubutton.place(x=174, y=1)
Ibutton = tk.Button(master=keyboard, text="I", height=1, width=2, command=lambda: window_keypress("i"))
Ibutton.place(x=201, y=1)
Obutton = tk.Button(master=keyboard, text="O", height=1, width=2, command=lambda: window_keypress("o"))
Obutton.place(x=228, y=1)
Pbutton = tk.Button(master=keyboard, text="P", height=1, width=2, command=lambda: window_keypress("p"))
Pbutton.place(x=255, y=1)

Abutton = tk.Button(master=keyboard, text="A", height=1, width=2, command=lambda: window_keypress("a"))
Abutton.place(x=26, y=30)
Sbutton = tk.Button(master=keyboard, text="S", height=1, width=2, command=lambda: window_keypress("s"))
Sbutton.place(x=53, y=30)
Dbutton = tk.Button(master=keyboard, text="D", height=1, width=2, command=lambda: window_keypress("d"))
Dbutton.place(x=80, y=30)
Fbutton = tk.Button(master=keyboard, text="F", height=1, width=2, command=lambda: window_keypress("f"))
Fbutton.place(x=107, y=30)
Gbutton = tk.Button(master=keyboard, text="G", height=1, width=2, command=lambda: window_keypress("g"))
Gbutton.place(x=134, y=30)
Hbutton = tk.Button(master=keyboard, text="H", height=1, width=2, command=lambda: window_keypress("h"))
Hbutton.place(x=161, y=30)
Jbutton = tk.Button(master=keyboard, text="J", height=1, width=2, command=lambda: window_keypress("j"))
Jbutton.place(x=188, y=30)
Kbutton = tk.Button(master=keyboard, text="K", height=1, width=2, command=lambda: window_keypress("k"))
Kbutton.place(x=215, y=30)
Lbutton = tk.Button(master=keyboard, text="L", height=1, width=2, command=lambda: window_keypress("l"))
Lbutton.place(x=242, y=30)

Enterbutton = tk.Button(master=keyboard, text="Enter", height=1, width=4, command=submit_letter)
Enterbutton.place(x=12, y=59)
Zbutton = tk.Button(master=keyboard, text="Z", height=1, width=2, command=lambda: window_keypress("z"))
Zbutton.place(x=53, y=59)
Xbutton = tk.Button(master=keyboard, text="X", height=1, width=2, command=lambda: window_keypress("x"))
Xbutton.place(x=80, y=59)
Cbutton = tk.Button(master=keyboard, text="C", height=1, width=2, command=lambda: window_keypress("c"))
Cbutton.place(x=107, y=59)
Vbutton = tk.Button(master=keyboard, text="V", height=1, width=2, command=lambda: window_keypress("v"))
Vbutton.place(x=134, y=59)
Bbutton = tk.Button(master=keyboard, text="B", height=1, width=2, command=lambda: window_keypress("b"))
Bbutton.place(x=161, y=59)
Nbutton = tk.Button(master=keyboard, text="N", height=1, width=2, command=lambda: window_keypress("n"))
Nbutton.place(x=188, y=59)
Mbutton = tk.Button(master=keyboard, text="M", height=1, width=2, command=lambda: window_keypress("m"))
Mbutton.place(x=215, y=59)
Deletebutton = tk.Button(master=keyboard, text="Delete", height=1, width=4, command=deletion)
Deletebutton.place(x=242, y=59)

def consequence(incorrect_guess, letter):
    if incorrect_guess == 1:
        head = canvas.create_oval(105,40,145,80, outline="black", fill="white", width=2) #195-->145
        letter1 = canvas.create_text(195,70, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 2:
        body = canvas.create_line(125,80,125,140, fill="black", width=2)
        letter2 = canvas.create_text(225,70, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 3:
        left_leg = canvas.create_line(125,140,105,160, fill="black", width=2)
        letter3 = canvas.create_text(255,70, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 4:
        right_leg = canvas.create_line(125,140,145,160, fill="black", width=2)
        letter4 = canvas.create_text(195,100, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 5:
        left_arm = canvas.create_line(125,90,100,110, fill="black", width=2)
        letter5 = canvas.create_text(225,100, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 6:
        right_arm = canvas.create_line(125,90,150,110, fill="black", width=2)
        letter6 = canvas.create_text(255,100, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 7:
        eye1 = canvas.create_line(113,50,123,60, fill="black", width=2)
        eye2 = canvas.create_line(123,50,113,60, fill="black", width=2)
        letter7 = canvas.create_text(195,130, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 8:
        eye3 = canvas.create_line(137,50,127,60, fill="black", width=2)
        eye4 = canvas.create_line(127,50,137,60, fill="black", width=2)
        letter8 = canvas.create_text(225,130, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 9:
        mouth = canvas.create_line(115,70,135,70, fill="black", width=2)
        letter9 = canvas.create_text(255,130, text=f"{letter}", font=30, fill="red")

import random

class Player:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome, " + self.name + "!")

name = input("What is your name? ")
Player_1 = Player(name)
window1.title(f"Hangman - {name}")

def intro():
    Player_1.welcome()
    while True:
        played = input("Have you ever played hangman before (yes/no)? ")
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
            canvas.delete("all")
            canvas.pack()
            top_post = canvas.create_line(75,20,125,20, fill="black", width=2)
            head_connect = canvas.create_line(125,20,125,40, fill="black", width=2)
            pole = canvas.create_line(75,20,75,200, fill="black", width=2)
            base = canvas.create_line(60,200,90,200, fill="black", width=2)
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
            word_label.config(text=displayed_word)
        else:
            displayed_word += "__ "
            word_label.config(text=displayed_word)
    return displayed_word.strip()

def letter_guess(word):
    incorrect_guess = 0
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
            incorrect_guess += 1
            consequence(incorrect_guess, guess)
        if incorrect_guess == 9:
            loss = canvas.create_text(225,30, text="YOU LOSE!", font=30)
            print("Sorry, game lost.")
            break
        if all(letter in guessed_letters for letter in word):
            win = canvas.create_text(225,30, text="YOU WIN!", font=30)
            print("Congratulations! You've guessed the word:", word)
            display_word(word, guessed_letters)
            break

def hangman():
    selected_word = select_random_word()
    print("The word has", len(selected_word), "letters.")
    letter_guess(selected_word)
    closing2()

intro()

window1.mainloop()