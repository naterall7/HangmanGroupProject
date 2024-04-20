import tkinter as tk
window1 = tk.Tk()

canvas = tk.Canvas(borderwidth=4, relief="ridge", height=200, width=300, bg="white")
canvas.pack()
top_post = canvas.create_line(125,20,175,20, fill="black", width=2)
head_connect = canvas.create_line(175,20,175,40, fill="black", width=2)
pole = canvas.create_line(125,20,125,200, fill="black", width=2)
base = canvas.create_line(110,200,140,200, fill="black", width=2)

head = canvas.create_oval(155,40,195,80, outline="black", fill="white", width=2)
body = canvas.create_line(175,80,175,140, fill="black", width=2)
left_leg = canvas.create_line(175,140,155,160, fill="black", width=2)
right_leg = canvas.create_line(175,140,195,160, fill="black", width=2)
left_arm = canvas.create_line(175,90,150,110, fill="black", width=2)
right_arm = canvas.create_line(175,90,200,110, fill="black", width=2)
mouth = canvas.create_line(165,70,185,70, fill="black", width=2)
#   The following make up the left eye
canvas.create_line(163,50,173,60, fill="black", width=2)
canvas.create_line(173,50,163,60, fill="black", width=2)
#   The following make up the right eye
canvas.create_line(187,50,177,60, fill="black", width=2)
canvas.create_line(177,50,187,60, fill="black", width=2)

loss = canvas.create_text(65,30, text="YOU LOSE!", font=30)

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
Xbutton = tk.Button(master=keyboard, text="X", height=1, width=1)
Xbutton.place(x=51, y=59)
Cbutton = tk.Button(master=keyboard, text="C", height=1, width=1)
Cbutton.place(x=71, y=59)
Vbutton = tk.Button(master=keyboard, text="V", height=1, width=1)
Vbutton.place(x=91, y=59)
Bbutton = tk.Button(master=keyboard, text="B", height=1, width=1)
Bbutton.place(x=111, y=59)
Nbutton = tk.Button(master=keyboard, text="N", height=1, width=1)
Nbutton.place(x=131, y=59)
Mbutton = tk.Button(master=keyboard, text="M", height=1, width=1)
Mbutton.place(x=151, y=59)
Deletebutton = tk.Button(master=keyboard, text="Delete", height=1, width=2)
Deletebutton.place(x=171, y=59)

window1.mainloop()

#   Use Accumulator Pattern. An incorrect guess will add 1 to the value of "incorrect_guess"
#   and that variable gets sent through the consequence(incorrect_guess) function
def consequence(incorrect_guess):
    if incorrect_guess == 1:
        head = canvas.create_oval(155,40,195,80, outline="black", fill="white", width=2)
    if incorrect_guess == 2:
        body = canvas.create_line(175,80,175,140, fill="black", width=2)
    if incorrect_guess == 3:
        left_leg = canvas.create_line(175,140,155,160, fill="black", width=2)
    if incorrect_guess == 4:
        right_leg = canvas.create_line(175,140,195,160, fill="black", width=2)
    if incorrect_guess == 5:
        left_arm = canvas.create_line(175,90,150,110, fill="black", width=2)
    if incorrect_guess == 6:
        right_arm = canvas.create_line(175,90,200,110, fill="black", width=2)
    if incorrect_guess == 7:
        canvas.create_line(163,50,173,60, fill="black", width=2)
        canvas.create_line(173,50,163,60, fill="black", width=2)
    if incorrect_guess == 8:
        canvas.create_line(187,50,177,60, fill="black", width=2)
        canvas.create_line(177,50,187,60, fill="black", width=2)
    if incorrect_guess == 9:
        mouth = canvas.create_line(165,70,185,70, fill="black", width=2)
        #   reveal word, no longer allow inputs, can start again?
        loss = canvas.create_text(65,30, text="YOU LOSE!", font=30)