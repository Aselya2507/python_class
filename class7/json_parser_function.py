# importing existing json module
import json

#import requests

#data = requests("https://drive.google.com/filename")

#for i in data
# print(i)

# reading json file from current directory
with open("data.json","r") as data_file:
    data = json.load(data_file)

# #Get class value from json object
# print(data["class"])   

# #Get school value from json object
# print(data["school"])

# #Get location value from json object
# print(data["location"])

#Get insructors value from json object
print(data["instructors"][0]["instructor1"]["name"])
INSTRUCTOR1_NAME = data["instructors"][0]["instructor1"]["name"]
INSTRUCTOR1_LASTNAME = data["instructors"][0]["instructor1"]["lastname"]
#for i in data["istructors"]:
# print(i)


# write instructors value 
 #target_file.write(data["instructors"][0]["instructor1"]["name"])

with open("instructor1_data","w") as target_file:
    target_file.write(INSTRUCTOR1_NAME + " " + INSTRUCTOR1_LASTNAME)
    target_file.close()



print(data["instructors"][0]["instructor2"]["name"])
INSTRUCTOR2_NAME = data["instructors"][0]["instructor2"]["name"]
INSTRUCTOR2_LASTNAME = data["instructors"][0]["instructor2"]["lastname"]

with open("instructor2_data", "w") as target_file:
    target_file.write(INSTRUCTOR2_NAME + " " + INSTRUCTOR2_LASTNAME)
    target_file.close()
    