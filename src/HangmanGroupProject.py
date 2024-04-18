# importing tkinter
import tkinter as tk


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