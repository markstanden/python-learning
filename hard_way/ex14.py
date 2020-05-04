## Learn python 3 the hard way Ex14
## Prompting and Passing

from sys import argv

#assign arguments to variables (unpack)
script, user_name = argv

#look of prompt
prompt = f'{script} \" '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
    Alright, so you said {likes} about liking me, fair enough.
    You live in {lives}.  Not sure where that is, needs some work by the look of you
    And you have a {computer} computer.  Nice.
    """)
