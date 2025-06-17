def decorations(func):
    def addparty(*args, **kwargs):
        print("🎉🎊🎊🎊🪅🎉")
        return func(*args, **kwargs)
    return addparty

def decorations2(func):
    def addbaloon(*args, **kwargs):
        print("🪅🪅🪅🪅🪅🪅")
        return func(*args, **kwargs)
    return addbaloon

@decorations
@decorations2
def birthday(name):
    print(f"HAPPY BIRTHDAY {name}🎉")  

birthday("sujan")
