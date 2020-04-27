##Learn Python the Hard Way
##Exercise 36
##Designing and Debugging
##Create my own text based game.

from random import *
from sys import argv

#unpack launch arguments
script, diff_arg = argv

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
    
    print(f"You are on level {diff} - I will release the key at level 100")
    
    #randomly generate operator weighted on difficulty
    question_op = get_operator(diff)
    question_op = "/"
    
    #randomly generate numbers, size dependant on difficulty level
    question_p1 = int(randint(1, int(diff)))
    question_p2 = int(randint(1, int(diff)))
    
    ##need to force production of an int number pair with perfect division
    if question_op == "/":
        #infinite loop until numbers cleanly divide
        while (question_p1 % question_p2 != 0) or (question_p1 == question_p2):
            print (question_p1 % question_p2)
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
    
    if diff < 99 and int(user_answer) == int(question_answer):
        print("Correct, increasing difficulty...")
        start(diff + 5)
        
    elif diff >= 99 and int(user_answer) == int(question_answer):
        print("Correct, and you have reached level 100.  I shall release the key...\n  Well done.")
        finish(diff_arg)
    else:
        print("Let's try again, but perhaps a little easier...")
        if diff > 5:
            start(diff - 1)
        else:
            start(5)

def finish(diff):
    print(f"level: {diff}")
    

start(int(diff_arg))
