file_path="C:/Users/Sujan/Desktop/test.txt"
try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("that file is not found")
except PermissionError:
    print("you don't have permission to this file")