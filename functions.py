def fun(**kwargs):
   for key,value in kwargs.items():
       print(f"{key}:{value}")
print(fun(a="hi",b="I",c="am",d="Sujan"))