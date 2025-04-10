import requests # importing requests for the api
import random # importing random to pick the random email conjoiner.
response = requests.get("https://randomuser.me/api/") # requests data from random user api 
data = response.json() # turns data from api request into json encoded data

emails = ["@aol.com","@gmail.com","@protonmail.com","@icloud.com","@outlook.com"] # list of emails
randomemail = random.choice(emails) # random choice from emails

gender = data['results'][0]['gender'] # gets gender
fname = data['results'][0]['name']['first'] # gets first name
lname = data['results'][0]['name']['last'] # gets last name
dOB = data['results'][0]['dob']['date'][:10] #gets date of birth, more irrelevent information so i slice it after the first 10 characters

phone = data['results'][0]['cell'] # gets phone 
email = data['results'][0]['email'].rsplit('@', 1)[0] + randomemail # i didn't like it being @example.com, so i made a list of emails and sliced the text before the @ sign and then connected the email to it after

country = data['results'][0]['location']['country'] # gets country
city = data['results'][0]['location']['city'] # gets city
postcode = str(data['results'][0]['location']['postcode'])# get postcode
streetNumber = str(data['results'][0]['location']['street']['number']) # gets street number
StreetName = data['results'][0]['location']['street']['name'] # gets street name

name = fname + " " + lname # conjoining first name and last name
location = country + ", " + city + ", " + streetNumber + " " + StreetName + ", " + postcode # conjoining all of the location information


print(f"name : {name}") # printing name
print(f"gender : {gender}") # printing gender
print(f"date of birth : {dOB}") # printing date of birth
print(f"phone number : {phone}") # printing phone number
print(f"email : {email}") # printing email
print(f"location : {location}") # printing location 
while True: # while loop so if error it asks again
    save = input("Would you like to save the information to a file? (y/n) ").lower() # asking if we would like to save information to file

    if save == "y": 
        print("saved!")
        f = open("information.txt", "w")
        f.write(f"""name : {name}
gender : {gender}
date of birth : {dOB}
phone number : {phone}
email : {email}
location : {location}""")
        f.close()
        break 
    # if input is "y" print saved open "information.txt", write the information to the file, and then close it

    elif save == "n":
        print("Okay! Goodbye")
        break
    # if input is "n" print "Okay! Goodbye" and then close

    else:
        print("Try again. ")
        # if anything else is inputted print "Try again." and then it asks the question again.