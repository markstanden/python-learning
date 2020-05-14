#Write a program that prints the numbers from 1 - 100
#but for multiples of three print "Fizz" instead of the multiple.
#for multiples of five print "Buzz" instead of multiple
#for multiples of both, print "FizzBuzz"

#create a list of the numbers from 1-100
fizzbuzz_list = list(range (1, 101))

#iterate the list
for count in fizzbuzz_list:
    #Change anything that divides perfectly by 3 and 5
    if count % 3 == 0 and count % 5 == 0:
        fizzbuzz_list[ count-1 ] = "FizzBuzz"
    
    #change anything that divides cleanly by 3 (anything above would skip this step)
    elif count % 3 == 0:
        fizzbuzz_list[ count-1 ] = "Fizz"

    #now change anything that divides cleanly by 5
    elif count % 5 == 0:
        fizzbuzz_list[ count-1 ] = "Buzz"

    #everything else just stays as it is.
    else:
        pass

###print the list to screen
for count in range(0, 100, 1):
    print(fizzbuzz_list[count])

##mega fast way:
for number in range( 1, 101 ):
    print( ("Fizz"*(number % 3 == 0) + "Buzz"*(number % 5 == 0) or number) )