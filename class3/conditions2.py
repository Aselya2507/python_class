# == equals
# != not equal 
# > greater than 
# < less than
# >= greater than or equal to
# <= less than or equal to

RESPONSE = input("when were you born?: ")
print(RESPONSE)

if RESPONSE >= "2000" and RESPONSE <= "2022":
    print("you were born in 21st century")
elif RESPONSE >= "1900" and RESPONSE <= "1999":
    print("you were born in 20th century")
elif RESPONSE == "1899" or RESPONSE <= "1800" :
    print("you should not be running this")
else:
    print("please give me a number")

