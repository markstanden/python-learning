##Learn python the hard way exercise 17
##More Files

#import the argv and exists modules
from sys import argv # argument handling
from os.path import exists

#unpack arguments
#argv expects 2 arguments
#print(argv)
script, from_file, to_file = argv 

#print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line - how?

##ONE LINER##
open(to_file, "w").write(open(from_file, "r" ).read())

##DOWN TO 2 LINES## in_data = open(from_file).read() #works - but less clear i guess.

#ORIGINAL #in_file = open(from_file)
#ORIGINAL #in_data = in_file.read()


#print(f"The input file is {len(in_data)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort")
#input()

#out_file = open(to_file, "w")
#out_file.write(in_data)
##DOWN TO 2 LINES## open(to_file, "w").write(in_data)
#print("Alright, all done")
print("Complete")
#to_file.close()
# from_file.close()
