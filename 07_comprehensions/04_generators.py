# generators are basically used for the saving the space and run it fast

prices = (12,4,5,3,2,4,6,8,7,7,8,1,3,4)

price = (12,4,5,3,2,4,6,8,7,7,8,1,3,4)


# creating a generator

gen_price = (price[i] for i in range(len(price)) if price[i] % 2 == 0)

# printing the generator

for i in gen_price:
    print(i)


# for suppose if we need sum of all the items which is divisible by two in this case we can use the generator
# we don't need the list values we just need a sum

# sum of all even numbers

sum_even = sum(pric for pric in prices if pric % 2 ==0)

print(f"Sum of all even numbers: {sum_even}")
