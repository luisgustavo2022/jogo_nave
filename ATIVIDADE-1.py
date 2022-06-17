import pgzrun
import random

WIDTH = 300
HEIGHT = 300

GAME_OVER = False
nave = Actor("nave", (WIDTH / 2, HEIGHT / 2))
coin = Actor("coin.jpg", (random.randrange(0, WIDTH), 0))
met = Actor("pedra.png", (random.randrange(0, WIDTH), 0))
tiro = Rect((20,20), (20,20))

box = Rect((20, 20), (50, 50))
score = 0
def draw():
    global GAME_OVER

    screen.clear()
    if GAME_OVER == False:
        screen.fill((255, 255, 255))
        nave.draw()
        met.draw()
        coin.draw()

    elif GAME_OVER == True:
        game_over()

def set_angle():
    nave.angle = 0

def update():
    global score
    coin.y += 1
    met.y += 1

    if met.y >= 300:
        met.y = 0
        met.x = random.randrange(0, WIDTH)

    if coin.y >= 300:
        coin.y = 0
        coin.x = random.randrange(0, WIDTH)



    #movimentação lateral da nave
    if keyboard.left:
        nave.x -= 2
        nave.angle = 15
        clock.schedule(set_angle, 0.5)

    elif keyboard.right:
        nave.x += 2
        nave.angle = 345
        clock.schedule(set_angle, 1.0)

    #if nave.colliderect(met):
        #set_nave_atingindo()

        
    #movimentação vertical    
    if keyboard.up:
        nave.y -= 2
    elif keyboard.down:
        nave.y += 2

    if nave.colliderect(coin):
        met.x = random.randint(0, WIDTH)
        met.y = 0
        score += 1
        print("Score:", score)

    if nave.colliderect(met):
       set_nave_atingindo()

    if nave.colliderect(coin):
        coin.y = 0
        coin.x = random.randrange(0, WIDTH)

    #checa colisão
    if nave.x >= WIDTH or nave.x < 0:
       set_nave_atingindo()

    elif nave.y >= HEIGHT or nave.y < 0:
        set_nave_atingindo()

    if GAME_OVER == True:
        game_over()

            
def set_nave_atingindo():
    global GAME_OVER
    global life
    nave.image = 'boom.png'
    #clock.schedule(set_nave_normal, 1.0)
    GAME_OVER = True

def set_nave_normal():
    nave.image = 'nave.png'

def game_over():
    screen.clear()
    screen.fill( (0,0,0) )
    screen.draw.text('GAME OVER', (90, 110))


pgzrun.go()

        
