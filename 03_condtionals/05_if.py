order_amount = int(input("Please enter the order amount: "))

delivery_fee = 0 if order_amount >300 else 30

print(f"delivery fee is {delivery_fee}")

