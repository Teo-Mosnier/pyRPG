import sys, pygame

pygame.init()

size = width, height = 1080, 720
screen = pygame.display.set_mode(size)

white = (255,255,255)


player = pygame.image.load("../Graph_resources/Sprites/Characters/Mage/Mage_1.png")
player = pygame.transform.flip(player,True,False)

pl_position = player.get_rect()
facing_right = True
velocity = 5

while 1:
    pygame.time.delay(1000)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            pl_position.move([1,1])
        #if keys[pygame.K_LEFT]:
        pl_position.move([-velocity,1])
        #if keys[pygame.K_DOWN]:
        pl_position.move([0,0])
        #if keys[pygame.K_UP]:
        pl_position.move([0,0])
    
    screen.fill(white)
    screen.blit(player, pl_position)

    print(pl_position)

    pygame.display.flip()