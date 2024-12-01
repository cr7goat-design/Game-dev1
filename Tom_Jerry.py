import pgzrun 
import random 
import time 
WIDTH = 600 
HEIGHT = 500 

score = 0 
game_over = False  
rat = Actor("rat") 
Cat = Actor("Cat") 
rat.pos = (100,100) 
Cat.pos = (200,200) 
msg = " " 

# To display Actor & other object in screen
def draw(): 
    screen.blit("backround", (0,0))  
    rat.draw() 
    Cat.draw() 
    screen.draw.text("Score:" + str(score), color="black", topleft = (10,10)) 

    if game_over : 
        screen.fill("Green")  
        global msg 
        msg = "Times Up!  \nYour Final Score:" 
        screen.draw.text( msg + str(score),midtop=(WIDTH/2,20), fontsize=50, color="yellow") 

def place_rat(): 
    rat.x = random.randint(70,(WIDTH-70)) 
    rat.y = random.randint(70, (HEIGHT-70))

def time_up(): 
    global game_over 
    game_over = True 

#this func to update the score, chg Cat position with the help of keyboard
def update(): 
    global score 
    if keyboard.left: 
        Cat.x = Cat.x-3 
    
    if keyboard.right: 
        Cat.x = Cat.x+3 
    
    if keyboard.up: 
        Cat.y = Cat.y-3 
    
    if keyboard.down: 
        Cat.y = Cat.y+3  
     
    rat_collected = Cat.colliderect(rat) 
    if rat_collected: 
        score = score + 10 
        place_rat()  


clock.schedule(time_up, 60.0) 
pgzrun.go()
