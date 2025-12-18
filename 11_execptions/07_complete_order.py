class InvalidChaiError(Exception): pass

def bill(flavor,cups):
    menu = {"tea":20 , "ginger":30}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Invalid Chai flavor")
        if not isinstance(cups,int):
            raise TypeError("Cups must be an integer")
        total = cups * menu[flavor]
        print(f"your bill for the {cups} cups of flavor {flavor} chai : rupees {total}")
    except Exception as e:
        print("error ",e)
    finally:
        print("Thank you for using our service!")


bill("ginger", 3)

bill("mint",2)

bill("tea", "four")