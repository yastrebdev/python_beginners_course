from tkinter import *

window = Tk()
window.geometry('420x420')
window.title('First app')

icon = PhotoImage(file='resources.png')
window.iconphoto(True, icon)
window.config(background='white')

window.mainloop()