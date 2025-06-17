try:
    a=int(input("Enter a number: "))
    print(1/a)
#except Exception:
 #   print("Something went wrong")
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("We can enter only a number")
except Exception:
    print("Something went wrong")
finally:
    print("Do the necessary changes")

