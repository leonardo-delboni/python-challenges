# Challenge 002
## Developed by LEONARDO TRAVAGINI DELBONI

###########################################################################################
# Write a program that calculates the factorial of a number inserted by the user. 
###########################################################################################

# Credits of the program:
print('Challenge 002 - Begginer level')
print('Developed by Leonardo Travagini Delboni \n')

# Input by the user:
value = int(input('Please, insert the value to find its factorial: \n'))

# Calculating the factorial:
aux1 = value
aux2 = 1

while aux1 >= 1:
    aux2 = aux2*aux1
    aux1 = aux1 - 1

# Results:
print(str(aux2))
