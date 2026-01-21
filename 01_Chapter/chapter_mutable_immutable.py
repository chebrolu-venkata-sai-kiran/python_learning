# ================================
# MUTABLE vs IMMUTABLE IN PYTHON
# ================================

print("----- IMMUTABLE OBJECTS -----\n")

# Example 1: Integer reassignment
x = 10
print("x value:", x)
print("x id:", id(x))

x = 20
print("x new value:", x)
print("x new id:", id(x))
print()

# Example 2: Integer operation creates new object
x = 10
y = x
print("x id:", id(x))
print("y id:", id(y))

y = y + 1
print("After y = y + 1")
print("x value:", x)
print("y value:", y)
print("x id:", id(x))
print("y id:", id(y))
print()

# Example 3: String immutability
s = "hello"
print("Original string:", s)
print("ID:", id(s))

s = s + " world"
print("New string:", s)
print("New ID:", id(s))
print()

# Example 4: Tuple immutability (commented to avoid error)
t = (1, 2, 3)
print("Tuple:", t)
# t[0] = 10  # ❌ TypeError


print("\n----- MUTABLE OBJECTS -----\n")

# Example 5: List mutation
a = [1, 2, 3]
print("Original list:", a)
print("ID:", id(a))

a[0] = 100
print("Modified list:", a)
print("ID after change:", id(a))
print()

# Example 6: Two references to same list
a = [1, 2, 3]
b = a
print("a:", a)
print("b:", b)

b.append(4)
print("After modifying b")
print("a:", a)
print("b:", b)
print()

# Example 7: Dictionary mutation
student = {"name": "Ali", "age": 20}
print("Before dict:", student)

student["age"] = 21
print("After dict:", student)
print()

# Example 8: Set mutation
numbers = {1, 2, 3}
numbers.add(4)
print("Set after add:", numbers)


print("\n----- FINAL COMPARISON -----\n")

# Immutable vs Mutable comparison
x = 10
print("Immutable before:", x, id(x))
x = x + 5
print("Immutable after:", x, id(x))

l = [1, 2, 3]
print("Mutable before:", l, id(l))
l.append(4)
print("Mutable after:", l, id(l))


# -------------------------------
# SUMMARY (Exam Ready)
# -------------------------------
# Immutable objects:
# - Cannot be changed in place
# - New object is created on reassignment
#
# Mutable objects:
# - Can be changed in place
# - Same object is modified
