import pgzrun

WIDTH = 300
HEIGHT = 300
GAME_OVER = False
nave = Actor ("nave", (WIDTH / 2, HEIGHT / 2))

def draw():
    global GAME_OVER
    
    screen.clear()
    if GAME_OVER == False:
        screen.fill((255, 255, 255))
        nave.draw()
    elif GAME_OVER == True:
        game_over()
def game_over():
    screen.clear()

    screen.fill( (0,0,0) )

    screen.draw.text('GAME OVER', (90,110))
        
def update():
    #movimentação lateral da nave
    if keyboard.left:
        nave.x -= 2
        nave.angle = 15
    elif keyboard.right:
        nave.x += 2
        nave.angle = 345
        
    #movimentação vertical    
    if keyboard.up:
        nave.y -= 2
    elif keyboard.down:
        nave.y += 2
        
    #checa colisão
    if nave.x >= WIDTH or nave.x < 0:
        set_nave_atingindo()
    elif nave.y >= HEIGHT or nave.y < 0:
        set_nave_atingindo()

    

            
def set_nave_atingindo():
    global GAME_OVER 
    nave.image = 'boom.png'
    # clock.schedule(set_nave_normal , 1.0)
    GAME_OVER = True

def set_nave_normal():
    nave.image = 'nave.png'

pgzrun.go()

        
