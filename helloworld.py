#This program says hello and asks for name and the age of the person.
#who run the program.

print("Hello World!     ")
myName = str(input('what is your name: ')) #ask for their name
print("It is good to meet you, "+ myName)
print("the length of your name is:")
print(len(myName))

myAge = input('what is your age? ') #ask for their age
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
