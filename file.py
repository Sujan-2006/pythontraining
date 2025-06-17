
import csv

txt_data="I like pizza"
students=[["name","age","gender"],
          ["SUJAN",19,"male"],
          ["MATHEW",20,"male"],
          ["RESHMA",19,"female"],
          ["VIDULA",18,"female"]]
file_path="C:/Users/Sujan/Desktop/test.csv"
try:
    with open(file_path,"w",newline="") as file:            #To write an unexisted file
        writer=csv.writer(file)          
        for row in students:
            writer.writerow(row)        #a-> to append an existing file
        print(f"csv file '{file_path}' is created")
except FileExistsError:
    print("that file already exists")
