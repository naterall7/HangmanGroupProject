import tkinter as tk
window1 = tk.Tk()
window1.title("Hangman")

canvas = tk.Canvas(borderwidth=4, relief="ridge", height=200, width=300, bg="white")
canvas.pack()

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

def letter_blanks(length):
    for x in range(0,length):
        current_text = word_label["text"]
        word_label.config(text=current_text+" __")
length = len("Word")
letter_blanks(length)

entry = tk.Entry(borderwidth=4, bg="white", relief="ridge", width=20)
entry.pack()

keyboard = tk.Frame(height=95, width=300, bg="black", borderwidth=4, relief="ridge")
keyboard.pack()

Qbutton = tk.Button(master=keyboard, text="Q", height=1, width=2)
Qbutton.place(x=12, y=1)
Wbutton = tk.Button(master=keyboard, text="W", height=1, width=2)
Wbutton.place(x=39, y=1)
Ebutton = tk.Button(master=keyboard, text="E", height=1, width=2)
Ebutton.place(x=66, y=1)
Rbutton = tk.Button(master=keyboard, text="R", height=1, width=2)
Rbutton.place(x=93, y=1)
Tbutton = tk.Button(master=keyboard, text="T", height=1, width=2)
Tbutton.place(x=120, y=1)
Ybutton = tk.Button(master=keyboard, text="Y", height=1, width=2)
Ybutton.place(x=147, y=1)
Ubutton = tk.Button(master=keyboard, text="U", height=1, width=2)
Ubutton.place(x=174, y=1)
Ibutton = tk.Button(master=keyboard, text="I", height=1, width=2)
Ibutton.place(x=201, y=1)
Obutton = tk.Button(master=keyboard, text="O", height=1, width=2)
Obutton.place(x=228, y=1)
Pbutton = tk.Button(master=keyboard, text="P", height=1, width=2)
Pbutton.place(x=255, y=1)

Abutton = tk.Button(master=keyboard, text="A", height=1, width=2)
Abutton.place(x=26, y=30)
Sbutton = tk.Button(master=keyboard, text="S", height=1, width=2)
Sbutton.place(x=53, y=30)
Dbutton = tk.Button(master=keyboard, text="D", height=1, width=2)
Dbutton.place(x=80, y=30)
Fbutton = tk.Button(master=keyboard, text="F", height=1, width=2)
Fbutton.place(x=107, y=30)
Gbutton = tk.Button(master=keyboard, text="G", height=1, width=2)
Gbutton.place(x=134, y=30)
Hbutton = tk.Button(master=keyboard, text="H", height=1, width=2)
Hbutton.place(x=161, y=30)
Jbutton = tk.Button(master=keyboard, text="J", height=1, width=2)
Jbutton.place(x=188, y=30)
Kbutton = tk.Button(master=keyboard, text="K", height=1, width=2)
Kbutton.place(x=215, y=30)
Lbutton = tk.Button(master=keyboard, text="L", height=1, width=2)
Lbutton.place(x=242, y=30)

Enterbutton = tk.Button(master=keyboard, text="Enter", height=1, width=4)
Enterbutton.place(x=12, y=59)
Zbutton = tk.Button(master=keyboard, text="Z", height=1, width=2)
Zbutton.place(x=53, y=59)
Xbutton = tk.Button(master=keyboard, text="X", height=1, width=2)
Xbutton.place(x=80, y=59)
Cbutton = tk.Button(master=keyboard, text="C", height=1, width=2)
Cbutton.place(x=107, y=59)
Vbutton = tk.Button(master=keyboard, text="V", height=1, width=2)
Vbutton.place(x=134, y=59)
Bbutton = tk.Button(master=keyboard, text="B", height=1, width=2)
Bbutton.place(x=161, y=59)
Nbutton = tk.Button(master=keyboard, text="N", height=1, width=2)
Nbutton.place(x=188, y=59)
Mbutton = tk.Button(master=keyboard, text="M", height=1, width=2)
Mbutton.place(x=215, y=59)
Deletebutton = tk.Button(master=keyboard, text="Delete", height=1, width=4)
Deletebutton.place(x=242, y=59)

window1.mainloop()

def consequence(incorrect_guess, letter):
    if incorrect_guess == 1:
        head = canvas.create_oval(155,40,195,80, outline="black", fill="white", width=2)
        canvas.create_text(195,70, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 2:
        body = canvas.create_line(175,80,175,140, fill="black", width=2)
        canvas.create_text(225,70, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 3:
        left_leg = canvas.create_line(175,140,155,160, fill="black", width=2)
        canvas.create_text(255,70, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 4:
        right_leg = canvas.create_line(175,140,195,160, fill="black", width=2)
        canvas.create_text(195,100, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 5:
        left_arm = canvas.create_line(175,90,150,110, fill="black", width=2)
        canvas.create_text(225,100, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 6:
        right_arm = canvas.create_line(175,90,200,110, fill="black", width=2)
        canvas.create_text(255,100, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 7:
        canvas.create_line(163,50,173,60, fill="black", width=2)
        canvas.create_line(173,50,163,60, fill="black", width=2)
        canvas.create_text(195,130, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 8:
        canvas.create_line(187,50,177,60, fill="black", width=2)
        canvas.create_line(177,50,187,60, fill="black", width=2)
        canvas.create_text(225,130, text=f"{letter}", font=30, fill="red")
    if incorrect_guess == 9:
        mouth = canvas.create_line(165,70,185,70, fill="black", width=2)
        canvas.create_text(255,130, text=f"{letter}", font=30, fill="red")
        #   reveal word, no longer allow inputs, can start again?
        loss = canvas.create_text(65,30, text="YOU LOSE!", font=30)