from tkinter import *

def display():
    if x.get() == 1:
        print('I check')
    else:
        print('I uncheck')

window = Tk()

x = IntVar()

check_button = Checkbutton(
    window,
    text='Check me',
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display
)
check_button.pack()

window.mainloop()