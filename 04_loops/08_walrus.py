# walrus operator used for assignment in a single line and condition check

# Python version 3.8 or above is required

names = ["sai", "kiran","venkata", "chebrolu"]

# walrus operator

# if (name := input("enter the name to search in college: ")) in names:
#     print(f"{name} is present in the list")
# else:
#     print(f"{name} is not present in the list")


# we can use the walrus operator in a nested loops also

print("student names:",names)

while (name := input("enter the name to search: ")) not in names:
    print(f"{name} is not present in the list. Please enter a valid name.")

print(f"{name} is present in the list")

