#The Program Starts

#Importing Stuff
import sys
from sys import exit
import time

#The time
print(time.asctime())

#Warnings and Messages
print('Hello and welcome to the "Phone Book" App!\n')

print('Remember dont call anyone you do not know because they might be voicemails, scammers, unkown numbers and more plus it might be fake and you might not know who you are calling and i set defaults too\n')

print('Please select an option below\n A - Create a new contact\n B - View contact list\n C - Quit')
question = input('Plese select A/B/ or C ')

#The users output
if question == "A":
  question2 = input('Enter your name and phone number ')
  file = open("Phone Numbers.txt", "w")
  file.write(question2)
  file.write("\n")
  file.close()
  sys.exit("Hope you enjoyed")

elif question == "B":
  print('Remember dont call anyone you do not know because they might be voicemails, scammers, unkown numbers and more plus it might be fake and you might not know who you are calling and i set som deafaults too\n')
  file = open('Phone Numbers.txt', "r")
  print(file.read())
  file.close()
  sys.exit("Hope you enjoyed")

else:
  sys.exit("Bye") 

#The Program Ends
