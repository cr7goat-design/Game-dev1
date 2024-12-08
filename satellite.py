import pgzrun 
from random import randint
from time import time 

WIDTH = 600
HEIGHT = 500 

satellites = [] 
lines = [] 
next_satallite = 0

start_time = 0 
total_time = 0 
end_time = 0 

number_of_satellite = 10 

def create_satallite():
    global start_time 
    for count in range(0,number_of_satellite): 
        satellite = Actor("satellite") 
        satellite.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40) 
        satellites.append(satellite) 
    start_time = time() # To get current time of your computer 
 
def draw(): 
    global total_time 
    screen.blit("background", (0,0)) 
    number = 1
    for satellite in satellites: 
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20)) 
        satellite.draw() 
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255)) 
        if next_satallite < number_of_satellite: 
            total_time = time() - start_time 
            screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30) 
        else: 
            screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30) 







def update(): 
    pass

def on_mouse_down(pos): 
    global lines,next_satallite  
    if next_satallite < number_of_satellite:
        if satellites[next_satallite].collidepoint(pos): 
            if next_satallite:
                lines.append((satellites[next_satallite-1].pos,satellites[next_satallite].pos)) 
            next_satallite +=1  
        else: 
            line = [] 
            next_satallite = 0


create_satallite() 





pgzrun.go()
