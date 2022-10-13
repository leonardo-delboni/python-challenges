# Challenge 003
## Developed by LEONARDO TRAVAGINI DELBONI

###########################################################################################
# Write a program that receives a sequence of numbers separated with commas thorough the 
# terminal and creates a list and a tuple with all of them. 
###########################################################################################

# Credits of the program:
print('Challenge 003 - Begginer level')
print('Developed by Leonardo Travagini Delboni \n')

# Receiving the numbers through the terminal:
sequence = input('Please, insert the sequence of numbers separeted with commas: \n')

# Converting string to list type:
sequence_list = sequence.split(',')
print('In the list format:')
print(sequence_list)

# Converting to tuple type:
sequence_tuple = tuple(sequence_list)
print('In the tuple format:')
print(sequence_tuple)
print('\n')