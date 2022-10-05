# == equals
from lib2to3.pgen2.token import EQUAL


# !=not equal
# > greater than 
# < less than
# >= greater
# <=
# input() function gets the response from the user at CLI

RESPONSE = input("When were you born?:")
print(RESPONSE)
if RESPONSE == "1900"
   print("You were born in 1900")
else:
    print("PLease give me anumber")

if RESPONSE >= "2000" and RESPONSE <="2022":
   print("You were born in 21st century")
elif RESPONSE >= "1900" and RESPONSE <= "1999":
   print("You were born in 20th century")  
elif RESPONSE == "1899" or RESPONSE <="1898":
    print("You should not be running this.")
else:
    print("PLease give me anumber")


