import random
choices=('r','p','s')
emojis={
    'r':'🪨',
    'p':'📃',
    's':'✂️'}
print("Welcome to the scissor paper rock game: ")
user_Choice=input('r/s/p: ').lower()

if user_Choice not in choices:
    print("not valid")
computer_Choice = random.choice(choices)
print(f'you chose {emojis[user_Choice]}')
print(f'Computer chose {emojis[computer_Choice]}')

if user_Choice == computer_Choice:
    print("Tie")
elif\
   (user_Choice  =='r' and computer_Choice== 's') or (user_Choice=='p' and computer_Choice=='r') or \
   (user_Choice== 's' and computer_Choice=='p'):
    print("you won")
else:
    print("you lost")
 
print("Hello World!")
        