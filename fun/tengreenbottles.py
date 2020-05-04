start_num = 10
amount_to_fall = 1

falling_item = "green bottle"
falling_items = falling_item + "s"

def sitting_on_the_wall(wall_number):
    if wall_number > 1:
        return(str(wall_number) + " " + str(falling_items) + " sitting on a wall")
        
    elif wall_number == 1:
        return(str(wall_number) + " " + str(falling_item) + " sitting on a wall")
    
    else:
        return("no " + str(falling_items) + " sitting on a wall...  Oh well.")

def accidently_fall(fall_number):
    if fall_number > 1:
        return("and if " + str(fall_number) + " " + str(falling_items) + " should accidently fall") 
    
    elif fall_number == 1:
        return("and if " + str(fall_number) + " " + str(falling_item) + " should accidently fall")
    
    else:
        return("It doesn't really work with values less than 1")


## Main Iteration
for i in range(start_num, 0, -1*(amount_to_fall) ):
    if amount_to_fall > i:
        amount_to_fall = i
    
    print( sitting_on_the_wall(i) + ",\n" +
           sitting_on_the_wall(i) + ",\n" +
           accidently_fall(amount_to_fall) + ",\n" +
           "there'd be " +
           sitting_on_the_wall(i-amount_to_fall) + ".\n" )

