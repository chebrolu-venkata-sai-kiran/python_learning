# we have three ways to import the any funtion or file to the any other file or new file 

#example we have one cafe.py where we have serve() function if we open new cafe instead of writing the whole serve
# method we can import the cafe.py 

# import cafe.py 
# cafe.serve()  # here we are importing whole file 

# from cafe.py import serve
# serve()  # here we are importing only the serve function

# from cafe.py import serve as serving
# serving()  # here we are importing only the serve function and renaming it to serving as we can have the serve in 
# our existing file where we are importing 


# if we want to import multiple functions from the cafe.py file

# from cafe.py import serve, eat, drink
# serve()
# eat()
# drink()  # here we are importing all the functions as coma seprated

