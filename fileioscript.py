import os
import time

path = 'C:\\Users\\taylo\\OneDrive\Documents\\GitHub\\Python-Projects\\Test Directory'

dirs = os.listdir(path)

for file in dirs:
    if file.endswith('.txt'):
        print(os.path.join(path, file))
        print(time.ctime(os.path.getmtime(path)))
