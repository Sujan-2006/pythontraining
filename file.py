
import json

txt_data="I like pizza"
students={"s1":"naruto","s2":"sasuke","s3":"sakura","s4":"kakashi"}
file_path="C:/Users/Sujan/Desktop/test.json"
try:
    with open(file_path,"w") as file:            #To write an unexisted file
        json.dump(students,file,indent=4)                  #a-> to append an existing file
        print(f"json file '{file_path}' is created")
except FileExistsError:
    print("that file already exists")
