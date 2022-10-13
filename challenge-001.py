# Challenge 001
## Developed by LEONARDO TRAVAGINI DELBONI

###########################################################################################
# Write a program that finds all the divisible numbers per 7, between 2000 and 3000, and
# they must not be multiple of 5. All the numbers must be printed in sequence in the same
# line, but separed with a comma (,).
###########################################################################################

# Libraries to be used:
import numpy as np

# Credits of the program:
print('Challenge 001 - Begginer level')
print('Developed by Leonardo Travagini Delboni \n')

# Limits:
lower_lim = 2000
upper_lim = 3000

# Creating the Vector:
vector = []
aux = lower_lim
while aux < upper_lim + 1:
    if aux % 7 == 0 and aux % 5 != 0: #Conditions
        vector.append(aux)
    aux = aux + 1

# Printing:
print(vector)