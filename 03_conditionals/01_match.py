seat_type = input("select the seat(sleeper,AC,General,luxury)").lower()

match seat_type:
    case "sleeper":
        print("The cost of sleeper seat is $350")
        
    case "ac":
        print("The cost of AC seat is $500")
        
    case "general":
        print("The cost of general seat is $150")
        
    case "luxury":
        print("The cost of luxury seat is $600")

    case _:
        print("select valid seat")
        


