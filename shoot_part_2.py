import pgzrun
import random
WIDTH = 750
HEIGHT = 650
WHITE = (255,255,255) 
BLUE = (0,0,255)     
ship = Actor("galaga") 
bug = Actor("bug") 
ship.pos = (WIDTH//2,HEIGHT-60) 
speed = 2 
bullets = [] 
enemies = [] 

     


score = 0
direction = 1

for x in range(10):
    enemies.append(Actor("bug"))
    enemies[-1].x= 100+ 70*x 
    enemies[-1].y =-30
    

def displayScore(): 
    screen.draw.text(str(score), (100,30))

def on_key_down(key): 
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y -50 

def update():
    global score 
    global direction 
    moveDown = False
    if keyboard.left: 
        ship.x = ship.x -5
        if ship.x <= 0:
            ship.x = 0

    elif keyboard.right: 
        ship.x = ship.x +5
        if ship.x >= 750:
            ship.x = 750 

    # to make bullet move up         
    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet) 
        else: 
            bullet.y = bullet.y -10   # bullet -= 10 
    if len(enemies)>0 and (enemies[0].x < 20 or enemies[-1].x > WIDTH-30):
        moveDown = True 
        direction = direction*(-1) 
    # to make enemies moving down 
    for enemy in enemies: 
        enemy.y +=3 
        if enemy.y >=HEIGHT:
            enemy.y = -100 
            enemy.x = random.randint(50,WIDTH-50) 
        
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score +=100 
                bullets.remove(bullet) 
                enemies.remove(enemy) 
             




        



def draw():
    screen.clear() 
    screen.fill(BLUE) 
    ship.draw() 
    for bullet in bullets: 
        bullet.draw() 
    for enemy in enemies:
        enemy.draw() 
    displayScore() 
     

pgzrun.go()
