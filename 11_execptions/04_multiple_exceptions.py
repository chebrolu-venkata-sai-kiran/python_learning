def process_order(item,quantity):

    try :
        price = {"tea":20}[item]
        cost = price * int(quantity)
        print(f"the total price is {cost}")
    except KeyError:
        print(f"Invalid item: {item}")
    except ValueError:
        print("Invalid quantity")


process_order("tea", 5)
process_order("coffee", 3)
process_order("tea", "two")
