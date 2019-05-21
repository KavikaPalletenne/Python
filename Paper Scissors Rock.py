import random
import time

moves = ['rock', 'paper', 'scissors']

print('+=+=+=+=Welcome to NigerianScammers™ Rock, Paper, Scissors!=+=+=+=+')
print('')

play = input('Would you like to play? yes or no ')

if play == 'yes':
    play2 = True
else:
    play2 == False
    print('Oh! See you later then.')
    time.sleep(0.5)
    sys.exit()
    

while play2 == True:
    pmove = input('Input your move: rock, paper or scissors ')
    cmove = random.choice(moves)
    
    if cmove == pmove:
        print(cmove)
        print('We go the same, try again!')
    
    
    if cmove == 'rock' and pmove == 'scissors':
        print(cmove)
        print('I won!')
        playagain = input('Do you want to play again? yes or no ')
        
        if playagain == yes:
            play2 = True
        else:
            play2 = False
            time.sleep(0.5)
            sys.exit()
            
    if cmove == 'rock' and pmove == 'paper':
        print(cmove)
        print('I lost!')
        playagain = input('Do you want to play again? yes or no ')
        
        if playagain == yes:
            play2 = True
        else:
            play2 = False
            time.sleep(0.5)
            sys.exit()
            
    if cmove == 'paper' and pmove == 'scissors':
        print(cmove)
        print('I lost!')
        playagain = input('Do you want to play again? yes or no ')
        
        if playagain == yes:
            play2 = True
        else:
            play2 = False
            time.sleep(0.5)
            sys.exit()
            
    if cmove == 'paper' and pmove == 'rock':
        print(cmove)
        print('I won!')
        playagain = input('Do you want to play again? yes or no ')
        
        if playagain == yes:
            play2 = True
        else:
            play2 = False
            time.sleep(0.5)
            sys.exit()
            
    if cmove == 'scissors' and pmove == 'rock':
        print(cmove)
        print('I lost!')
        playagain = input('Do you want to play again? yes or no ')
        
        if playagain == yes:
            play2 = True
        else:
            play2 = False
            time.sleep(0.5)
            sys.exit()
            
            
    if cmove == 'scissors' and pmove == 'paper':
        print(cmove)
        print('I won!')
        playagain = input('Do you want to play again? yes or no ')
        
        if playagain == yes:
            play2 = True
        else:
            play2 = False
            time.sleep(0.5)
            sys.exit()