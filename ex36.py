##Learn Python the Hard Way
##Exercise 36
##Designing and Debugging
##Create my own text based game.

from random import *
from sys import argv

#unpack launch arguments
script, diff_arg, max_arg = argv

max_diff = int(max_arg)

prompt = "-->> "

####### get_operator returns arithmetic operator for the games

def get_operator(difficulty):
    seed()
    op_float = difficulty * random ()
    band1 = difficulty / 2
    band2 = difficulty / 8
    band3 = difficulty / 16
    
    #Check the logical arguments below were working ok
    #print(f"get_operator (op_int {op_float}, band1 {band1}, band2 {band2}, band3 {band3})")
    
    if difficulty >= op_float > band1:
        op_string = "+"
        
    elif band1 > op_float >= band2:
        op_string = "-"
    
    elif band2 > op_float >= band3:
        op_string = "*"
        
    else: #presumably band3 > op_float >= 0:
        op_string = "/"
    
    return op_string

def start(diff):
    seed()
    print("You wake up in a dark room with a chalk and a blackboard.\nA key is held in an unbreakable cage.\nThere appears to be a camera looking at the blackboard, perhaps someone is watching...")
    print("There is some text written on the blackboard it reads:")
    
    print(f"You are on level {diff} - I will release the key at level {max_diff}")
    
    #randomly generate operator weighted on difficulty
    question_op = get_operator(diff)
        
    #randomly generate numbers, size dependant on difficulty level
    question_p1 = int(randint(1, int(diff)))
    question_p2 = int(randint(1, int(diff)))
    
    ##need to force production of an int number pair with perfect division
    if question_op == "/":
        #infinite loop until numbers cleanly divide
        while (question_p1 % question_p2 != 0) or (question_p1 == question_p2):
            #print (question_p1 % question_p2)
            question_p1 = int(randint(1 ,int(diff)))
            question_p2 = int(randint(2, int(diff)))
    
    #display question
    print(f"""\n
    \t\t{question_p1}
    \t{question_op}
    \t\t{question_p2}
    """)
    
    #work out the answer to the question depening on the randomly generated operation
    if question_op == "+":
        question_answer = question_p1 + question_p2
        
    elif question_op == "-":
        question_answer = question_p1 - question_p2
    
    elif question_op == "*":
        question_answer = question_p1 * question_p2
        
    elif question_op == "/":
        question_answer = question_p1 / question_p2
        
    else:
        print("Operator Error!")
        exit(1)
    
    print("What do you think the answer is?")
    user_answer = input(prompt)
    
    if diff < (max_diff - 1) and int(user_answer) == int(question_answer):
        print("Correct, increasing difficulty...")
        start(diff + 5)
        
    elif diff >= (max_diff - 1) and int(user_answer) == int(question_answer):
        print(f"Correct, and you have reached level {max_diff}.  I shall release the key...\n  Well done.")
        finish(int(diff_arg))
    else:
        print("Let's try again, but perhaps a little easier...")
        if diff > 5:
            start(diff - 1)
        else:
            start(5)

def finish(diff):
    print(f"level: {diff}")
    print("You take the key and torches around the room illuminate.")
    print("You are wearing a ninja outfit, and it seems you have passed a test on the way to being a supreme ninja.")
    print("You can use the key to open the door to the left - marked 'Gold Store' or to the right marked 'Weapons'")
    print("Do you want to open the door to the left, or right? (type left or right)")
    user_choice = input(prompt)
    
    if user_choice == "left":
       # print ("Left - Gold - Good Choice")
        gold_room(diff)
    elif user_choice == "right":
       # print ("Right - Weapons - Good Choice")
        weapons_room(diff)
    else:
        print ("Sorry I didn't understand that - please try again...")
        finish(diff)

def gold_room(diff):
    print("You enter the room and door locks behind you.\n")
    print("You can have all the money and gold you could ever dream of!")
    print("The only problem is you cannot escape the room.")
    print("None of your ninja powers work, and you are stuck here, FOREVER!")
    print("\n\n\t THE END \n\n")
    exit (0)
    
def weapons_room(diff):
    print("You enter the room and the door locks behind you.\n")
    print("You can choose from every ninja weapon ever invented.  All are in silent dull black - to strike from the shadows.")
    print("\nWhat will you choose?")
    weapon_choice = input(prompt)
    print(f"You choose the deadliest looking {weapon_choice} you can find, and use it to cut a hole in the wall to escape")
    print(f"Over the years, you and your {weapon_choice} become one, and you become the greatest ninja in all of human history")
    print(f"You should name your {weapon_choice}, what will you call it?")
    weapon_name = input(prompt)
    print(f"Yes, a {weapon_choice} called {weapon_name} sounds perfect.  Fit for the legends you will both create.")
    print("No-one could defeat such a weapon in the hands of such a powerful ninja!")
    print("\n\n\t THE END \n\n")
    
## Call the starting room
start(int(diff_arg))
