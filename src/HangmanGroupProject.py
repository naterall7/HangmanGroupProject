def main():
    played = input("Welcome Player 1, have you ever played hangman before (yes/no)? ")
    if played == "yes":
        ready = print("Are you ready to play(yes/no)? ")
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

main()