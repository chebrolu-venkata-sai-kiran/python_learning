class OutOfIngredientsError(Exception):
    pass

def make_drink(milk,sugar):
    if milk < 1 or sugar < 1:
        raise OutOfIngredientsError("Not enough ingredients")
    print("drink is ready ..."
            )
        

make_drink(1,0)