a = set()
print(f"the intial reference to the set is: {id(a)}")

# Adding elements to the set
for i in range(10):
    a.add(i)

print(f"the final reference to the set after adding elements is: {id(a)}")

# Checking the size of the set

print(f"The size of the set is: {len(a)}")


# Removing an element from the set
a.remove(5)

print(f"the final reference to the set after removing an element is: {id(a)}")

# sets are muttable in Python, hence their id remains the same even after adding or removing elements.
# here we initially created an empty set and then added 10 elements to it. 
# After adding elements, the id of the set remained the same. 
# Then we removed one element from the set and the id of the set also remain