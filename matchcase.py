def week(a):                #alternative of switch case
    match a:
        case  "sunday" | "saturday":
            return "week end"
        case "monday" | "tuesday" | "wednesday" | "thursday" |"friday":
            return "not a weekend"
        case _:
            return "invalid"
print(week("monday"))
    
