from tkinter import *

window = Tk()
lb = Listbox(window, height=3)
lb.pack()
lb.insert (END, 'first entry')
lb.insert (END, 'second entry')
lb.insert (END, 'third entry')
lb.insert (END, 'fourth entry')

sb = Scrollbar(window, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)


