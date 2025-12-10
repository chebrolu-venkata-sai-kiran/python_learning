#dict

# creating a dictionary

details = dict(name ="kiran",age = "24",state = "ap")

print(details)

college ={}

college["kiran"] = "srm"

college["kalyan"] = "vignan"



college["venkat"] = "vignan"



print(college)

del college["venkat"]

print(college)

print(f"is srm exist {'kiran' in college}")


print(f"names of students {college.keys()}")
print(f"names of colleges {college.values()}")
print(f"names of students and colleges {college.items()}")


last_student = college.popitem()

print("the last guy",last_student)

extra_details ={'shoes':'black','shirt':'polo'}

details.update(extra_details)

print(details)

sai_detail = details.get('naame','not available ')

print(sai_detail)