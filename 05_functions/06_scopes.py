# def serve_drink():
#     drink_type = "cold"
#     print(f"inside function {drink_type}")

# drink_type = "hot"

# serve_drink()

# print(f"outside function {drink_type}")

def drink_counter():
    drink_order = "blue laggon"
    
    def print_drink():
        drink_order = "lemon soda"
        print(f"inside nested function {drink_order}")
    print("outside nested function",drink_order)
    print_drink()
drink_counter()
drink_order = "chass"
print("global",drink_order)