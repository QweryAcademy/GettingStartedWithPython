# print("Hello world")

# print("What is your name?")
# my_name = raw_input()
# print("Your name is {}{}{}".format(my_name,"Oyeniyi","Biola"))

# my_name = raw_input("What is your name?\n")
# print("Your name is {}{}{}".format(my_name,"Oyeniyi","Biola"))


# name_of_schools = []
# primary_school = raw_input("What is the name of your primary school?\n")
# name_of_schools.append(primary_school)
# secondary_school = raw_input("What is the name of your secondary school?\n")
# name_of_schools.append(secondary_school)
# university = raw_input("What is the name of your University?\n")
# name_of_schools.append(university)

# print(','.join(name_of_schools))

# name_of_schools = {
#     'primary':"",
#     'secondary':"",
#     "university":""
# }
# name_of_schools['primary'] = raw_input("What is the name of your primary school?\n") 
# name_of_schools['secondary'] = raw_input("What is the name of your secondary school?\n")
# name_of_schools['university'] = raw_input("What is the name of your University?\n")

# y = [x for x in []]
# import pdb
# pdb.set_trace()
# transform = ["The name of the {} school is {}".format(key, value) for key, value in name_of_schools.items()]
# sorted_result = name_of_schools.items()
# sorted_result.sort()

# transform = ["The name of the {} school is {}".format(*item) for item in sorted_result]
# result = ",\n".join(transform)

# print(result)




# primary_school = raw_input("What is the name of your primary school?\n")
# secondary_school = raw_input("What is the name of your secondary school?\n")
# university = raw_input("What is the name of your University?\n")
# name_of_schools = [primary_school, secondary_school, university]

def summation(*a):
    result = 0
    for w in a:
        # result = result + w
        result += w
    return result

print(summation(3,2))
print(summation(7, 5))
print(summation(200,1000, 5999))
print(summation(3))


