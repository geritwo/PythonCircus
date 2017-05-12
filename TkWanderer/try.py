# Various methods I'm trying to work out on the workbench

from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300, bg='red')
canvas.pack()

message = 'Hajdihó!'


def szovegeles(message):
    text = Text(root, width=70, height=2, bg='white', fg='black', font='Helvetica 14', wrap=WORD)
    text.insert(INSERT, message + '\nPress Space!')
    text.pack()

    #text.update_idletasks()

    root.bind('<Key>', message_updater)

def message_updater(event):
    text.destroy()
    message = 'Ezt a gombot nyomtad meg, nyomi: ' + str(event.keysym)
    szovegeles(message)

szovegeles(message)
root.mainloop()
