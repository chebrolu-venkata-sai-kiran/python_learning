drinks = {"coke":20 ,"cola":30}

# print(drinks["cokee"])

try: 
    print(drinks["cokee"])
except KeyError:
    print("The key 'cokee' does not exist in the dictionary.")

print(drinks["cola"])