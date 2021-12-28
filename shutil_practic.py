import shutil
import os
from datetime import datetime, timedelta
from tkinter import *
from tkinter import filedialog as fd
from schedule import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(485, 165))
        self.master.title('Check Files')

        self.btnBrowse1 = Button(self.master, text='Watch Folder...', width=12, command=self.browse)
        self.btnBrowse1.grid(row=1, column=1, padx=(15, 5), pady=(30, 0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text='Send Folder...', width=12, command=self.browse2)
        self.btnBrowse2.grid(row=2, column=1, padx=(15, 5), pady=(10, 0), sticky=NE)

        self.btnCheck = Button(self.master, text='Check Files', command=self.checkFiles, width=12, height=2)
        self.btnCheck.grid(row=3, column=1, padx=(15, 5), pady=(10, 0), sticky=NE)

        self.btnCancel = Button(self.master, text='Close Program', width=12, height=2)
        self.btnCancel.grid(row=3, column=2, padx=(15, 0), pady=(10, 0), sticky=SE)

        self.browseText1 = StringVar()
        self.browseText2 = StringVar()

        # Connects entry to entire window
        self.fileOne = Entry(self.master, text=self.browseText1, width=55)  #the entry widget used to hold the file path
        self.fileOne.grid(row=1, column=2, padx=(20, 0), pady=(30, 0))

        # Connects entry to entire window
        self.fileTwo = Entry(self.master, text=self.browseText2, width=55)
        self.fileTwo.grid(row=2, column=2, padx=(20, 0), pady=(10, 0))
    
    # Lets user select directory, removes any existing choices and replaces with new
    def browse(self):
        self.browse = fd.askdirectory()
        self.fileOne.delete(0, 'end')
        self.fileOne.insert(END, self.browse)

    def browse2(self):
        self.browse2 = fd.askdirectory()
        self.fileTwo.delete(0, 'end')
        self.fileTwo.insert(END, self.browse2)

    def checkFiles(self):
        # Checks entries for empty values
        if not self.fileOne.get():
            self.browse()
        if not self.fileTwo.get():
            self.browse2()
 
        # iterates through all files
        files = os.listdir(self.browseText1.get())
        for i in files:

            # grabs directory, concatenates with file name
            x = (str(self.browseText1.get()) + "\\"+ i)

            # grabs modified time from selected file path
            y = datetime.datetime.fromtimestamp(os.stat(x).st_mtime)

            # grabs directory of destination folder
            z = str(self.browseText2.get())

            # if the modified time is less than one day, moves file to desitation folder
            if (datetime.datetime.utcnow() - y) < timedelta(1):
                shutil.move(x, z)
                print("New File, Moved to: " + z)
            else:
                print("Old File - Not Moved")

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


