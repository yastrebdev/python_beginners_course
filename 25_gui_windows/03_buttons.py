from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

button = Button(
    window,
    text='click me!',
    command=click,
    font=('Comic Sans', 16),
    fg='red',
    bg='black',
    activeforeground='green',
    activebackground='blue',
    # state="disabled",

)
button.pack()

window.mainloop()