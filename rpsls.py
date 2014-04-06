#Ray F Allan  "rock paper scissors lizard spock"
#runs in www.codeSkulptor.org
#code from coursera/Rice University 'intro interactive progamming'

import random

def number_to_name(number):
    name = ""
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "error number_to_name: " + number
    return name
    
def name_to_number(name):
    number = ""
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "error name_to_number: " + name
    return number

def rpsls(name): 
    result=""
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    difference = (player_number-comp_number)%5
    if difference == 2 or difference == 1:
        result = "Player wins"
    elif difference == (4) or difference == (3):
        result = "Computer wins"
    elif difference == 0:
        result = "Player and computer tie"
    else:
        print "error rpsls: " + name
    # print results
    print "Player chooses: " + name
    print "Computer chooses: " + number_to_name(comp_number)
    print result + "!"
    print
    
# test your code
rpsls("rock")
rpsls("paper")
rpsls("Spock")
