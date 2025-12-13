# when we are using the nonlocal we are able to access the above function and we can modify the value 


def update_order():
    drink_type = "hot"

    def kitchen():
        nonlocal drink_type
        print(f"The current drink type is {drink_type}")
        drink_type = "cold"
        
    kitchen()
    print(f"After updating, the drink type is {drink_type}")
update_order()