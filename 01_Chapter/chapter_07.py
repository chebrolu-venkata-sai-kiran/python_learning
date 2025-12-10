#lists are muttable in python

names = ["sai" ,"kiran", "chebrolu"]

# adding names

names.append("venkata")

print(f"list of the names after adding is: {names}")

# removing names

names.remove("sai")

print(f"list of the names after removing is: {names}")

# combine two lists

names2 = ["ram", "shyam"]

names.extend(names2)

print(f"list of the names after combining is: {names}")

#insert a name at a specific index

names.insert(0, "sai")

print(f"list of the names after inserting is: {names}")

#pop a name from the end

last_name =names.pop()
print(last_name)

print(f"list of the names after popping is: {names}")

#reverse the list

names.reverse()

print(f"list of the names after reversing is: {names}")

#sort the list

names.sort()

print(names)

#min and max

min_name = min(names)

max_name = max(names)

print(f"min name is: {min_name}")

print(f"max name is: {max_name}")




