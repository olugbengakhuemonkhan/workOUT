
#  STRINGS
# print ("I am " + str(45) + " years old")
# # i did it after 6 trials

# INTEGER
# x = "45"
# print int(x) + 5

# FORMAT is a better way

# create a variable age
# create a curly braces to make room for the variable
# add the format to feed/replace the curly braces with the variable

# ("I am " + str(45) + " years old")
age = 45
# print ("I am {} years old").format(age)

print ("I am {} years old".format(age))
user_age = raw_input("are you {} years old too?".format(age))
       