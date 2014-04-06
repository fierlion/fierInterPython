#code from coursera.org/Rice University 'intro Interactive Programming'
#should be run in www.codeskulptor.com

import simplegui

#globals
start = 217
iterations = 0
maxi = 1

#compute
def compute(initial):
    global start
    global iterations
    global maxi
    if start > maxi:
        maxi = start
    if start % 2 == 0:
        start = start / 2
        print start
    else:
        start = (start * 3) + 1
        print start
    iterations += 1
    if start == 1:
        timer.stop()
        print "max is: " + str(maxi)

#timerhandler
def timer_handler():
    compute(start)

#timer
timer = simplegui.create_timer(10, timer_handler)

#start timer
timer.start()
