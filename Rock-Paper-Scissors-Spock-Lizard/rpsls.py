#The Rock-Paper-Scissor-Spock-Lizard Game
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
def name_to_number(name):
    if(name=="rock"):
        number=0
    elif(name=="Spock"):
        number=1
    elif(name=="paper"):
        number=2
    elif(name=="lizard"):
        number=3
    elif(name=="scissors"):
        number=4
    else:
        print("Pls choose a valid option")
    return number
        
def number_to_name(number):
    if(number==0):
        name="rock"
    elif(number==1):
        name="Spock"
    elif(number==2):
        name="paper"
    elif(number==2):
        name="lizard"
    elif(number==3):
        name="scissors"
    else:
        print("Pls choose a valid option")
        
    return name
 
    

def rpsls(player_choice): 
    
    
    print("Player chooses "+player_choice)
    player_number=name_to_number(player_choice)
    computer_number=random.randrange(0,4)
    computer_choice=number_to_name(computer_number)
    print("Computer chooses "+computer_choice)
    
    if(computer_number + 1) % 5 == player_number:
        print ("Player wins!")
        
    elif(computer_number + 2) % 5 == player_number:
        print ("Player wins!")
        
    elif(computer_number )== player_number:
        print ("Player and computer tie!")
        
    else:
        print ("Computer wins!")
        
    print ("")
   
    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



