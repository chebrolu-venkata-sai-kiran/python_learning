# string

name  = "sai kiran"

# strings are immutable

print(f"my name is {name}")

#indexing

# if i want ony first name we need to slice the string 

print(f"my first name is {name[0:4]}")

# slicing

print(f"my last name is {name[4:]}")

label_text = "sái kiran"

endcoded_text = label_text.encode("utf-8")

print(f"the lable text {label_text}")

print(f"the encoded text {endcoded_text}")

decoded_text = endcoded_text.decode()
print("the decoded text",decoded_text)


