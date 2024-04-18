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