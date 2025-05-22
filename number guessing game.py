import random
answer = (random.randint(1,100)) 


def process(n, chances):
    
    for chances in range(1,n):
      X = (input('Enter your guess:'))
      try:
            guess = int(X)
      except ValueError:
            print('Please enter a valid value')
           
      if guess == answer:
            print(f'Congratulations! You guessed the corct number in {chances} attemps\n')
            break
      elif guess > answer:
            print(f'Incorrect! The number is lesser than {guess}.\n')
            chances = chances+1
      elif guess < answer:
            print(f'Incorrect! The number is greater than {guess} .\n' )
            chances = chances+1
      else:
            print('Please enter a valid number between 1 to 100')
    else:
           print('Sorry you have run out of chances!')



keep_playing = True
          
while keep_playing == True:
      print('''Welcome to the Number Guessing Game
I am thinking of a numver between 1 and 100.

      ''')
      print('''Please select a difficulty level:
1. Easy (10 chances)
2. Medium (5 chances) 
3. Hard (3 chances) 
            ''')
      choose_level = (input('Enter your choice: '))

      game_start = ('Let us start the game\n')
      try:
            choice= int(choose_level)
      except ValueError:
            print('Please enter a valid value')

      if choice == 1:
            print('''Great you have selected the Easy difficulty level.''',
            game_start)
            
            process(11,1)

      elif choice == 2:
            print('''Great you have selected the Medium difficulty level.''',
            game_start)
    
            process(6,1)
   
      elif choice == 3:
            print('''Great you have selected the Hard difficulty level.''', 
            game_start)
    
            process(4,1)

      
      ask = input('''Do you wanna continue the game? 
1. Yes
2. No
Press 1 to continue, press 2 to exit the game. Your choice:\n''')
      try:
            options = int(ask)
            if options == 1:
                  keep_playing = True
            elif options == 2:
                  keep_playing = False
                  print('Thank you for playing!')
                  break
      except ValueError:
                  print('Please enter a valid value')


