#ASSIGNING A VALUE OF "APPLE" INTO A KEY "FRUIT"
FRUIT = "apple"

print(FRUIT)

#shows the location of the string in the memory
print(id(FRUIT))

#shows the data type 
print(type(FRUIT))

#shows the methods of the string
#print(dir(FRUIT))

#CApitalizes the first letter
print(FRUIT.capitalize())

#Find how many times "P" is repeated
print(FRUIT.count("p"))

#find out if the string starts with something "..."
print(FRUIT.startswith("app"))

#find out if the string ends with something "..."
print(FRUIT.endswith("pple"))

#change (letters) to uppercases
print(FRUIT.upper())



INCORECT_STRING = "   spaced_string   "

#print value
print(INCORECT_STRING)

#Remove spacces on the left side
print(INCORECT_STRING.lstrip())

#remove spaces on the right side
print(INCORECT_STRING.rstrip)

#remove spaces from both sides
print(INCORECT_STRING.strip())

