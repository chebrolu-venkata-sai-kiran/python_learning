# anonymous function or lambda

# lambda function to square a number

# square = lambda x: x**2

# # calling the lambda function

# print(square(5))

# here we are using the lamba function to check if any of the available drink list which we asked should not be 
# there so we kept the not equal here to check and return 


drink_types = ["small","medium","large","extra"]

req_drink = list(filter(lambda drink : drink!="xl",drink_types))

print(req_drink)