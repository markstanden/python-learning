## Learn python 3 the hard way Ex13
## Parameters, Unpacking, Variables

#from sys import argv

#Read the WYSS section for how to run this
#script, first, second, third = argv

#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)

## My Version

#load the argv module
from sys import argv

#list the arguments and assign them to strings
script_name, arg1, arg2 = argv

print(f"You have run {script_name} with the following arguments:\n1:\t{arg1}\n2:\t{arg2}")
answer = input("Would you like to overwrite?\nAll data in the directory will be destroyed: ")
print(f"{answer} - OK, Overwriting disk...")
print("Transaction complete")
