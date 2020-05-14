#import random to allow a random choice from each of the tuples
import random

#number of similes to display
number_to_display = 10

#first tuple, random verbs
verbs = ( 'running',
          'playing',
          'jumping',
          'squatting',
          'kicking',
          'headbutting',
          'laying',
          'tickling',
          'eating',
          'singing',
          'pissing',
          'drilling',
          'shagging',
          'twisting',
          'jiving',
          'coding',
          'walking' )

#second tuple, persons
persons = ( 'your mum',
            'your gran',
            'someone elses mum',
            'your best friend',
            'your best friend\'s wife',
            'your dog',
            'the vicar',
            'your teacher',
            'your boss',
            'your workmates',
            'the taxman',
            'Donald Trump' )

#third tuple, location
locations = ( 'up-hill',
              'down-hill',
              'in the bath',
              'in the shower',
              'in the rain',
              'in the garden',
              'in bed',
              'in your grave',
              'at work',
              'at the gym',
              'in the car',
              'in the shed',
              'in the garage' )

#fourth tuple, reason
reasons = ( 'you love',
            'you hate',
            'you lust after',
            'you can\'t live without',
            'you always hide from',
            'you need to avoid',
            'you only have eyes for' )

#Print a hilarious opening phrase 
print('\nWe know it can be difficult in this modern age of fast thinking millenials and gen Xers to sound hip and spontaneous.  Here at Standensoft we aim to solve this problem, just throw in a few of the similies below and you\'ll sound super hip, and on trend.\n\n')

# loop over the number of results to display, and print results to screen
for i in range(number_to_display):

    random_verb = random.choice(verbs)
    random_person_one = random.choice(persons)
    random_location = random.choice(locations)
    random_reason = random.choice(reasons)
    
    #random person two would ideally be different to person one
    random_person_two = random.choice(persons)
    #if they are the same, loop until different
    while random_person_two == random_person_one:
        random_person_two = random.choice(persons)
        
    #print the result to screen
    print(f"{i+1}.\tIt's a bit like {random_verb} with {random_person_one} {random_location} because {random_reason} {random_person_two}")