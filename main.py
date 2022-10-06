# Created by Will Whitehead, w1lt#4683
# Version 0.0.3
# Last modified:
import os
from datetime import date
today = date.today()
todays_date = today.strftime("%m/%d")
def create_set():
    user_input = input("Enter First name, Last name, and KUID: ")
    user_input = user_input.split(", ")
    first = user_input[0]
    last = user_input[1]
    kuid = user_input[2]
    output_file = open("settings.txt","w")
    output_file.write(f"{first},{last},{kuid}")
    output_file.close()
if os.path.exists("settings.txt") == False:
    create_set()
else:
    output_file = open("settings.txt", "r") 
    for line in output_file:
        user_input = line.split(",")
        first = user_input[0]
        last = user_input[1]
        kuid = user_input[2]
        print(f"\nWelcome back, {first}!")
        print(f"Is this info still correct? {first} {last}, {kuid}")
        if input("y / n: ") == "n":
            create_set()
output_file = open("settings.txt", "r") 
for line in output_file:
    user_input = line.split(",")
    first = user_input[0]
    last = user_input[1]
    kuid = user_input[2]
lab_number = input("Enter lab number: ")
exercises = int(input("Enter excercise amount: "))
dir_name = last + "-" + kuid + "-Lab-" + lab_number
os.mkdir(dir_name)
output_file.close()
for i in range(exercises):
    lab_name = "lab" + lab_number + "-" + "exercise0" + str(i+1) + ".py"
    completeName = os.path.join(dir_name, lab_name)
    output_file = open(completeName,"w")
    output_file.write("\'\'\'\n" + 
    f"Author: {first} {last}\n" +
    f"KUID: {kuid}\n" +
    f"Date: {todays_date}\n" +
    f"Lab: lab{lab_number}\n" +
    f"Last modified: {todays_date}\n" +
    "Purpose: Enter purpose here\n" + 
    "\'\'\'")
print("Done!")
output_file.close()


