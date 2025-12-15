# sending generators

def get_drink():
    print("welcome to my cafe!")
    order = yield
    print("outside loop",order)
    while True:
        print(f"we have {order} in stock")
        order = yield
        print("inside loop",order)

user1 = get_drink()

print(next(user1)) # welcome to my cafe! # here we are strating the generator so we can send the values to generator 

user1.send("Coke")  # we have Coke in stock
user1.send("mojito")
        
