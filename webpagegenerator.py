import webbrowser
import os
import tkinter as Tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        # Window sizing and title
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(485, 200))
        self.master.title('Web Generator')

        self.lblTxtBox = Label(self.master, text='Set the body of the text')
        self.lblTxtBox.grid(row=1, column=0, padx=(15, 5), pady=(15, 5), sticky=NW)

        # Creates variable to hold entered text from 'textEntry'
        self.newEntry = StringVar() 

        self.textEntry = Entry(self.master, text=self.newEntry, width=75)
        self.textEntry.grid(row=2, column=0, columnspan=2, padx=(15, 5), sticky=NE)

        self.btnSubmit = Button(self.master, text='Submit & Launch', width=15, command=self.submit)
        self.btnSubmit.grid(row=3, column=0, padx=(15, 5), pady=(20, 0), sticky=NE)

        self.btnClear = Button(self.master, text='Clear', width=15, command=self.clear)
        self.btnClear.grid(row=4, column=0, padx=(15, 5), pady=(10, 0), sticky=NE)

        self.btnQuit = Button(self.master, text='Quit', width=15, command=root.destroy)
        self.btnQuit.grid(row=5, column=0, padx=(15, 5), pady=(10, 0), sticky=NE)


    # Clears any existing text within 'textEntry'
    def clear(self):
        self.textEntry.delete(0, 'end')        


    def submit(self):
        
        # Establishes base html content, utilizes a wildcard to insert new content
        base = '''
        <html>
            <body>
                <h1>
            Stay tuned for our amazing summer sale!
                </h1>
                <p>
            {}
                </p>
            </body>
        </html>
        '''

        # Creates finalized text content
        text = base.format(self.newEntry.get())

        p = open('index.html', 'w')
        p.write(text)  # Overrides existing text with new
        p.close()

        # Opens html file
        filename = 'file:///'+ os.getcwd() +'/' + 'index.html'
        webbrowser.open(filename)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()