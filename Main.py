import pygame, sys

pygame.init()

#GAME WİNDOW
screen_size = [1080,720,300,100]

#WİNDOW
dark_grey = (24,24,24)
white_grey = (64,64,64)
white = (255,255,255)
green = (0,255,0)
world_pos = [0,0]


mouse_pos = [0,0]
mouse_rect = pygame.Rect(mouse_pos[0],mouse_pos[1],1,1)
selected_tile = [0,0]


rows = 10
cols = 100
tile_size = screen_size[1] // rows
tile_size = 32

display_tile_size = 50

tile_assets = 21

screen = pygame.display.set_mode((screen_size[0] + screen_size[2], screen_size[1] + screen_size[3]))
pygame.display.set_caption("MyLevelEditor")

pattern = pygame.image.load('Pattern.png').convert_alpha()


#GENERATE WORLD MAP
World_map = []
for i in range(rows):
    temp = [-1] * cols
    World_map.append(temp)
    
for i in range(cols):
    World_map[rows-1][i] = 0


tile_list = []
display_tile_list = []
tile_rect_list = []
for i in range(tile_assets):
    img = pygame.image.load(f'img/{i}.png')
    img = pygame.transform.scale(img,(tile_size,tile_size))
    tile_list.append(img)
    img = pygame.transform.scale(img,(display_tile_size,display_tile_size))
    display_tile_list.append(img)
    

margin_rect = pygame.Rect(1081,0,300,721)


def draw_bg():
    screen.fill(dark_grey)
    for i in range(10):
        screen.blit(pattern,(world_pos[0] + (i*pattern.get_width()),0))
    
def draw_grid():
    #vertical lines 
    for i in range(cols + 1):
        pygame.draw.line(screen, white, (i * tile_size + world_pos[0],0),(i * tile_size + world_pos[0], screen_size[1]))
    # horizontal lines
    for i in range(rows + 1):
        pygame.draw.line(screen, white, (0, i * tile_size),(screen_size[0], i * tile_size))

def draw_button():
    x_offset = 0
    y_offset = 0
    for i in range(tile_assets):
        screen.blit(display_tile_list[i], (screen_size[0] + (x_offset * 75) + 50 , (y_offset * 75) + 50))
        tile_rect_list.append(pygame.Rect(screen_size[0] + (x_offset * 75) + 50 , (y_offset * 75) + 50, display_tile_size, display_tile_size))
        
        x_offset += 1
        if x_offset == 3:
            y_offset += 1
            x_offset = 0
    
def select_tile():
    for i in range(tile_assets):
        if mouse_rect.colliderect(tile_rect_list[i]):
            pygame.draw.rect(screen,white, tile_rect_list[i],1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        selected_tile[0] = i
        
        
    pygame.draw.rect(screen,green, tile_rect_list[selected_tile[0]],2)                    

def draw_world_map():
    for y, row in enumerate(World_map):
        for x, tile in enumerate(row):
            if tile >= 0:
                 screen.blit(tile_list[tile],(x * tile_size + world_pos[0], y * tile_size + world_pos[1]))
            


while True:
    mouse_pos = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_pos[0],mouse_pos[1],1,1)
    draw_bg()
    draw_grid()
    draw_world_map()
    pygame.draw.rect(screen,white_grey,margin_rect)
    draw_button()
    select_tile()
    
    
    
    
    if pygame.mouse.get_pressed()[0] and mouse_pos[0] < screen_size[0] and mouse_pos[1] < screen_size[1]:
        x = (mouse_pos[0] - world_pos[0]) // tile_size
        y = (mouse_pos[1] - world_pos[1]) // tile_size
        
        if x < cols and y < rows:
            World_map[y][x] = selected_tile[0]
    elif pygame.mouse.get_pressed()[2] and mouse_pos[0] < screen_size[0] and mouse_pos[1] < screen_size[1]:
        x = (mouse_pos[0] - world_pos[0]) // tile_size
        y = (mouse_pos[1] - world_pos[1]) // tile_size
        
        if x < cols and y < rows:
            World_map[y][x] = -1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Keyboard Presses
        #Mouse Presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and world_pos[0] < 0:
                world_pos[0] += 16
            if event.button == 5:
                world_pos[0] -= 16
                

        
    pygame.display.update()