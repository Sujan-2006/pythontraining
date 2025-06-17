txt_data="I like pizza"
students=["naruto","sasuke","sakura","kakashi"]
file_path="C:/Users/Sujan/Desktop/test.txt"
try:
    with open(file_path,"w") as file:            #To write an unexisted file
        for student in students:
            file.write(student+"\n")                   #a-> to append an existing file
        print(f"txt file '{file_path}' is created")
except FileExistsError:
    print("that file already exists")
