def fun(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for key,value in kwargs.items():
        print(f"{key}:{value}")
fun("sujan","mathew","manoj",a="naruto",b="eren",c="luffy")