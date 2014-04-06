#Ray F Allan "Guess the number Game"
#runs in www.codeskulptor.org
#from coursera.org/Rice University Intro Interactive Programming

import simplegui
import random

# initialize global variables used in your code
secNum = 50
guessNum = 1001
rangeTop = 100
guesses = 0
guessTop = 6

#program logic
def num_test():
    if guesses>guessTop:
        print "Sorry, " + str(guessNum) + " is not the number."
        print "GAME OVER!"
        print ""
        if rangeTop == 100:
            range100()
            frame.start()
        elif rangeTop == 1000:
            range1000()
            frame.start()
     
    elif guessNum > secNum:
        print str(guessNum) + " is too high"
        print "guess again"
        print "(you have "+ str(guessTop-guesses+1) +" guesses left)"
        print ""
    elif guessNum < secNum:
        print str(guessNum) + " is too low"
        print "guess again"
        print "(you have "+ str(guessTop-guesses+1) +" guesses left)"
        print ""
    elif guessNum == secNum:
        print "WINNER!" 
        print str(guessNum) + " is right!"
        print ""
        if rangeTop == 100:
            range100()
            frame.start()
        elif rangeTop == 1000:
            range1000()
            frame.start()
        
def randInt(start, end):
    secNum = random.randrange(start, end)
    return secNum

# define event handlers for control panel   
def range100():
    # button that changes range to range [0,100) and restarts
    global rangeTop
    global secNum
    global guesses
    global guessTop
    print "NEW GAME"
    print "range is 0-100"
    rangeTop = 100
    guessTop = 6
    secNum = randInt(0, 100)
    guesses = 0
    frame.start()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global rangeTop
    global secNum
    global guesses
    global guessTop
    print "NEW GAME"
    print "range is 0-1000"
    rangeTop = 1000
    guessTop = 9
    secNum = randInt(0, 1000)
    guesses = 0
    frame.start()
    
def text_Num(text_input):
    global guessNum
    global guesses
    guesses += 1
    guessNum = float(text_input)
    num_test()
    
        
# create frame
frame = simplegui.create_frame("Guess the Number", 300, 200)
frame.add_input("Guess (then press enter)", text_Num, 75)
frame.add_button("0-100", range100, 75)
frame.add_button("0-1000", range1000, 75)

# start frame

frame.start()
