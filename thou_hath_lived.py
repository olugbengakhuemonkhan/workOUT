# price = 110
# if price < 100:
#     print ("Buy oranges")
# elif price == 100:
#     print ("If you feel like")
# else:
#         print ("Do not buy oranges") 




# def age_Cal():
#     ageDays = raw_input(" Type Y for number of days or H for number of hours ") 
#     if ageDays == "Y":
#         userAge = raw_input(" I am ")
#         print("thou hath lived {} days on earth".format(int(userAge)* 365 ))
#     elif ageDays == "H":
#         userAge = raw_input("I am ")
#         print("thou hath lived {} hours on earth".format(int(userAge)* 365 * 24))


# age_Cal()
def whatAge():
    whatMonth = raw_input("Type M if you are interested in Months and W if you are interested in weeks\n")
    if whatMonth == "M":
        userMonth = raw_input("How old are you? ")
        print("You have lived {} months on earth".format (int(userMonth) * 12 ))
    elif whatMonth == "W":
        userMonth = raw_input("How old are you? ")
        print("You have lived {} weeks on earth".format (int(userMonth) * 52 ))

whatAge()        