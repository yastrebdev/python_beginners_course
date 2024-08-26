from tkinter import *

def order():
    if x.get() == 0:
        print('Pizaa')
    elif x.get() == 1:
        print('Hamburger')
    elif x.get() == 2:
        print('Hotdog')
    else:
        print('hah?')

food = ['pizza', 'hamburger', 'hotdog']

window = Tk()

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(
        window,
        text=food[i],
        variable=x,
        value=i,
        # indicatoron=0
        command=order
    )
    radio_button.pack(anchor=W)

window.mainloop()