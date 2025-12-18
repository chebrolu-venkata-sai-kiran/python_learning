# file = open("order.txt","w")
# try:
#     file.write("1. 2 cups of coffee\n")
#     file.write("2. 1 cup of tea\n")
#     file.write("3. 1/2 cup of milk\n")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     file.close()

#second way

with open("order.txt","w") as file:
    file.write("1. 2 cups of coffee\n")
    file.write("2. 1 cup of tea\n")
    file.write("3. 1/2 cup of milk\n")
    print("File created successfully")
