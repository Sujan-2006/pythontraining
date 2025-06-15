def week(a):                #alternative of switch case
    match a:
        case 1:
            return "sunday"
        case 2:
            return "monday"
        case 3:
            return "monday"
        case 4:
            return "monday"
        case 5:
            return "monday"
        case 6:  
            return "monday"
        case 7:
            return "monday"
        case _:        # _id used as like default
            return "invalid"
print(week("k"))
    
