from tkinter import *

window = Tk()

scale = Scale(
    window,
    from_=0,
    to=100,
    length=300,
    orient=HORIZONTAL,
    tickinterval=10
)
scale.set(5)
scale.pack()

window.mainloop()