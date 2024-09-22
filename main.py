import pygame

pygame.init()

win_width = 500
win_height = 500

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_width, win_height))
window.fill((255, 255, 255))

font = pygame.font.Font(None, 32)
text = ''
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                text = "On"
            if event.key == pygame.K_UP:
                text = "Up"
            if event.key == pygame.K_RIGHT:
                text = "Right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                text = "Off"
            if event.key == pygame.K_DOWN:
                text = "Down"
            if event.key == pygame.K_LEFT:
                text = "Left"
    window.fill((240, 240 , 240))
    window.blit(font.render(text, True, (0, 0, 0), (10, 225, 50)),  (50, 50))
    clock.tick(60)
    pygame.display.update()