def caliculate_bill(cups, price):
    return price * cups

my_bill = caliculate_bill(3, 7.50)
print(f"Your total bill is {my_bill:.2f} dollars")

print("order for the table 2 :",caliculate_bill(3,45))