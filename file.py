import os

file="File1/test1.txt"    #C:/Users/Sujan/Desktop
if os.path.exists(file):
    print(f"the location '{file}' exists")
    if os.path.isfile(file):
        print("that is a file")
    elif os.path.isdir(file):
        print("that is a directory")
else:
    print("that location doesn't exists")