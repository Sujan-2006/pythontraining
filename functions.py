def fun(*args,**kwargs):
   for arg in args:
       print(arg,end=" ")
       print()
   for value in kwargs.values():
       print(value,end=" ")
    #print(f"{kwargs.get('a')}")
print(fun("naruto","sasuke","sakura","kakashi",a="hi",b="I",c="am",d="Sujan"))