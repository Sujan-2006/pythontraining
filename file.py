import json

file_path="C:/Users/Sujan/Desktop/test.json"
try:
    with open(file_path,"r") as file:
        content=json.load(file)
        print(content["s4"])
except FileNotFoundError:
    print("that file is not found")
except PermissionError:
    print("you don't have permission to this file")