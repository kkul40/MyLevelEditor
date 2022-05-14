import pygame, sys

pygame.init()

#GAME WİNDOW
screen_size = [1080,720,300,100]

#WİNDOW
dark_grey = (24,24,24)
white_grey = (64,64,64)
white = (255,255,255)
world_pos = [0,0]

rows = 16
maxs_col = 150
tile_size = screen_size[1] // rows

screen = pygame.display.set_mode((screen_size[0] + screen_size[2], screen_size[1] + screen_size[3]))
pygame.display.set_caption("MyLevelEditor")

pattern = pygame.image.load('Pattern.png').convert_alpha()
margin_rect = pygame.Rect(1081,0,300,721)


def draw_bg():
    screen.fill(dark_grey)
    for i in range(10):
        screen.blit(pattern,(world_pos[0] + (i*pattern.get_width()),0))
    
def draw_grid():
    #vertical lines 
    for i in range(maxs_col + 1):
        pygame.draw.line(screen, white, (i * tile_size + world_pos[0],0),(i * tile_size + world_pos[0], screen_size[1]))
    # horizontal lines
    for i in range(rows + 1):
        pygame.draw.line(screen, white, (0, i * tile_size),(screen_size[0], i * tile_size))


while True:
    draw_bg()
    draw_grid()
    pygame.draw.rect(screen,white_grey,margin_rect)
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Mouse Presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and world_pos[0] < 0:
                world_pos[0] += 16
            if event.button == 5:
                world_pos[0] -= 16
                

        
    pygame.display.update()



