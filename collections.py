anime={"naruto":"hinata",
       "sasuke":"sakura",
       "eren":"mikasa",
       "sanji":"nami"}
print(dir(anime))
print(anime.get("sasuke"))

if anime.get("tanjiro"):
    print("naruto loves hinata")
else:
    print("mc doesn't exist")


anime.update({"sanji":"violet"})
#anime.pop("naruto")
#anime.popitem()
#anime.clear()

print(anime)
#keys=anime.keys()
#print(keys)

'''
for k in anime.keys():
    print(k)

values=anime.values()
print(values)

for v in anime.values():
    print(v)

print(anime.items())
'''

for k,v in anime.items():
    print(f"{k}:{v}")
                



