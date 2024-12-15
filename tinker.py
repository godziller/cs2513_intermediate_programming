from tkinter import Tk, Label, Button

def onClickButton():
    l1.config(text='Button was pressed')

root = Tk()
l1 = Label(root, text='Hello!')
l1.pack()

btn = Button(root, text='Dont press me!', command=onClickButton)
btn.pack()

root.mainloop()