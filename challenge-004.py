# Challenge 004
## Developed by LEONARDO TRAVAGINI DELBONI

###########################################################################################
# Define a class which has at least two methods: getString to receive a string through the
# terminal using input(), and printString to print the string using uppercase letters.
# Also, include a simple funtion to test the class methods.
###########################################################################################

# Credits of the program:
print('Challenge 004 - Begginer level')
print('Developed by Leonardo Travagini Delboni \n')

#Defining the class:
class String:

    # ATRIBUTES:
    # Defining a empty string initially:
    def __init__(self):
        self.string = ""

    # METHODS:
    # getString - Receiving a string through the terminal:
    def getString(self):
        self.string = input('Please, insert the string desired: \n')
    
    # printString - Printing in uppercase:
    def printString(self):
        print(self.string.upper())

# Creating an instance of an object:
input_string = String()

# Executing the desired function:
input_string.getString()
input_string.printString()








    



        
