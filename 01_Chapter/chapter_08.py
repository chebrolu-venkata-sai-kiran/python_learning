# operator overloading

# Python supports operator overloading, which means we can define
#  how certain operators behave with our own custom objects.

name =  "sai kiran"
name2 = "sai"

# the '+' operator is overloaded to concatenate strings

print(name + " " + name2)

# the '*' operator is overloaded to repeat strings

print(name * 3)

#bytearray


byte_name = bytearray(b"sai kiran")

byte_name = byte_name.replace(b"sai", b"chebrolu sai")

print(byte_name)



