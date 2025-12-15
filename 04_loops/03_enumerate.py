# enumerate basically return the index and in a form of tuple
items = ["snacks","drinks","food","tea","deserts"]


# using for loop to iterate over the items
for idx,snacks in enumerate(items,start=1):
    print(f"{idx} : {snacks}")