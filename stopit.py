#Ray F Allan "Guess the number Game"                                      
#runs in www.codeskulptor.org                                          
#from coursera.org/Rice University Intro Interactive Programming

# template for "Stopwatch: The Game"
import simplegui

# define global variables
timeNum = 0
stops = 0
sucStops = 0

#define converter
def conv(t):
    mill = t % 10
    secs = ((t - mill)/10) % 100
    mins = (((t - mill)/10) - secs)/100
    if secs >= 10:
        return str(mins) + ":" + str(secs) + "." + str(mill)
    return str(mins) + ":0" + str(secs) + "." + str(mill)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    global stops
    global sucStops
    timer.stop()
    stops += 1
    if timeNum % 10 == 0:
        sucStops += 1

def reset_handler():
    global timeNum
    global stops
    global sucStops
    timer.stop()
    timeNum = 0
    stops = 0
    sucStops = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global timeNum
    timeNum += 1

# define draw handler
def draw(canvas):
    canvas.draw_text("StopIT", (123, 50), 20, "Yellow")
    canvas.draw_text("(Try to StopIT ON the second)", (55, 75), 15, "Black")
    canvas.draw_text(conv(timeNum), (100,200), 40, "White")
    canvas.draw_text((str(sucStops) + "/" + str(stops)), (135, 150), 20, "Yellow")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_canvas_background("Teal")

#buttons
start = frame.add_button("start", start_handler)
stop = frame.add_button("stop", stop_handler)
reset = frame.add_button("reset", reset_handler)

#timer
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
