import csv

file_path="C:/Users/Sujan/Desktop/test.csv"
try:
    with open(file_path,"r") as file:
        content=csv.reader(file)
        for i in content:
            print(i[2])
except FileNotFoundError:
    print("that file is not found")
except PermissionError:
    print("you don't have permission to this file")