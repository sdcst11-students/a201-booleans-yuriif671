#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

###problem
a = input("Gimme a number: ")

print("Integer") if a.isdigit() else print("Nuh-uh")