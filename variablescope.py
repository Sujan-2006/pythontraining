def ex1():     #enclosed variabl search the variable in local level and if it is not available it searches in the enclosed level
    x=2
    def ex2():
      
        print(x)
    ex2()
ex1()

 