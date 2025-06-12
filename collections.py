items=[["phone","charger","wire"],
       ["pizza","burger","dosa","idly"],
       ["pen","pencil","waterbottle"]]

print(items[0][2])

for i in items:
    for j in i:
        print(j,end=" ")
    print()

#we can also use this for set within set or tuple with in a tuple or a set with in a tuple