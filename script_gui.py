from tkinter import *
from tkinter import filedialog as fd


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(485, 165))
        self.master.title('Check Files')

        self.btnBrowse1 = Button(self.master, text='Browse...', width=12, command=self.browse)
        self.btnBrowse1.grid(row=1, column=1, padx=(15, 5), pady=(30, 0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text='Browse...', width=12, command=self.browse2)
        self.btnBrowse2.grid(row=2, column=1, padx=(15, 5), pady=(10, 0), sticky=NE)

        self.btnCheck = Button(self.master, text='Manual File Check', width=12, height=2)
        self.btnCheck.grid(row=3, column=1, padx=(15, 5), pady=(10, 0), sticky=NE)

        self.btnSet = Button(self.master, text='Set Daily Check', width=12, height=2)
        self.btnSet.grid(row=3, column=2, padx=(15, 0), pady=(10,0), sticky=W)

        self.btnCancel = Button(self.master, text='Close Program', width=12, height=2)
        self.btnCancel.grid(row=3, column=2, padx=(15, 0), pady=(10, 0), sticky=SE)

        self.browseText1 = StringVar()
        self.browseText2 = StringVar()

        # Connects to entire window
        self.fileOne = Entry(self.master, text=self.browseText1, width=55)  #the entry widget used to hold the file path
        self.fileOne.grid(row=1, column=2, padx=(20, 0), pady=(30, 0))

        # Connects to entire window
        self.fileTwo = Entry(self.master, text=self.browseText2, width=55)
        self.fileTwo.grid(row=2, column=2, padx=(20, 0), pady=(10, 0))
    
    def browse(self):
        x = fd.askdirectory()
        self.fileOne.delete(0, 'end')
        self.fileOne.insert(END, x)
        print(x)

    def browse2(self):
        x = fd.askdirectory()
        self.fileTwo.delete(0, 'end')
        self.fileTwo.insert(END, x)
        print(x)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
