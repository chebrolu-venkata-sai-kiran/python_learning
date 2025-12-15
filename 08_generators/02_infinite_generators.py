def infinte_drink():
    count =1

    while True:
        yield(f"Drink number {count}") # here we need to keep the yield instead of yield if we keep the print program will crash
        count +=1

user1 = infinte_drink()

# user2 = infinte_drink()

for _ in range(3):
    print(next(user1))

# for k in range(6):
#     print(next(user2))