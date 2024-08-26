from tkinter import *

window = Tk()

photo = PhotoImage(file='resources.png')

label = Label(
    window,
    text = 'Hello Python',
    font = ('Arial', 16, 'bold'),
    fg = 'red',
    bg = 'black',
    relief = "raised",
    bd = 10,
    padx = 20,
    pady = 20,
    image = photo,
    compound='top'
)
# label.pack()
label.place(x=10, y=10)

window.mainloop()