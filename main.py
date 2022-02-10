from turtle import color, down
import pygame, sys
import math
from random import randint

def display_score():
    curr_time = math.floor(pygame.time.get_ticks() / 1000 - (start_time / 1000))
    score_surf = test_font.render(f'Score: {curr_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return curr_time

def obstacle_movement(obstacle_list):
    global upward
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            # if obstacle_rect.bottom > 300:
            #     # if obstacle_rect.y >= 100 and upward:
            #         obstacle_rect.bottom -= 1
                # if obstacle_rect.y <= 250 and downward:
                #     obstacle_rect.y += 3 

                # if obstacle_rect.y >= 250:
                #     upward = True
                #     downward = False
                # if obstacle_rect.y <= 100:
                #     upward = False
                #     downward = True

            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                if upward:
                    obstacle_rect.top -= 3
                if obstacle_rect.top <= 200:
                    upward = False               
                if upward == False:
                    obstacle_rect.bottom += 3
                if obstacle_rect.bottom >= 250:
                    upward = True
                screen.blit(fly_surf,obstacle_rect)




        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def cloud_animation():
    global cloud2_surf, cloud2_index
    cloud2_index += 0.2
    if cloud2_index >= len(cloud2):cloud2_index = 0
    cloud2_surf = cloud2[int(cloud2_index)]



def cyc_animation():
    global cyc_surf, cyc_walk_index
    cyc_walk_index += 0.5
    if cyc_walk_index >= len(cyc_walk):cyc_walk_index = 0
    cyc_surf = cyc_walk[int(cyc_walk_index)]



pygame.init()
screen = pygame.display.set_mode((800, 400)) #This creates a display
pygame.display.set_caption('Goober Run') #This names the Window
clock = pygame.time.Clock() #Creates the game clock which is used to set speed
test_font = pygame.font.Font('PixelArt/Game1/Font/Pixeltype.ttf', 50) #creates a font to use for text later
game_active = False
start_time = 0
score = 0
upward = True
crab = False
liz = False
monke = False
monk = False
turt = False
lion = False
flow = False
cyc = False


title_surf = pygame.image.load('PixelArt/Game1/TitleScreen/background.png').convert()

titlecard_surf = test_font.render('Goober Run', False, '#b6d53c')
titlecard_surf = pygame.transform.rotozoom(titlecard_surf,0,2.5)
titlecard_rect = titlecard_surf.get_rect(midbottom = (400,100))

choose_surf = test_font.render('Choose your Goober:',False, '#d95763')
choose_rect = choose_surf.get_rect(midbottom = (400,150))

crabtext_surf = test_font.render('Lord Crab',False,'#d95763')
crabtext_rect = crabtext_surf.get_rect(midbottom = (400,300))

liztext_surf = test_font.render('Liz the Wiz',False,'#d95763')
liztext_rect = liztext_surf.get_rect(midbottom = (400,300))

monketext_surf = test_font.render('Monke',False,'#d95763')
monketext_rect = monketext_surf.get_rect(midbottom = (400,300))

monktext_surf = test_font.render('Gandalf the Wise',False,'#d95763')
monktext_rect = monktext_surf.get_rect(midbottom = (400,300))

turttext_surf = test_font.render('Michaelangelo',False,'#d95763')
turttext_rect = turttext_surf.get_rect(midbottom = (400,300))

liontext_surf = test_font.render('Simba',False,'#d95763')
liontext_rect = liontext_surf.get_rect(midbottom = (400,300))

flowtext_surf = test_font.render('Ralta the Formidable',False,'#d95763')
flowtext_rect = flowtext_surf.get_rect(midbottom = (400,300))

cyctext_surf = test_font.render('Steve',False,'#d95763')
cyctext_rect = cyctext_surf.get_rect(midbottom = (400,300))



menu_crab_surf = pygame.image.load('PixelArt/Game1/Player/crabman_stand.png').convert_alpha()
menu_crab_scaled = pygame.transform.scale(menu_crab_surf,(72,88))
menu_crab_rect = menu_crab_scaled.get_rect(center = (50,200))

menu_liz_surf = pygame.image.load('PixelArt/Game1/Player/lizardman_stand.png').convert_alpha()
menu_liz_scaled = pygame.transform.scale(menu_liz_surf,(72,88))
menu_liz_rect = menu_liz_scaled.get_rect(center = (150,200))

menu_monke_surf = pygame.image.load('PixelArt/Game1/Player/monke_stand.png').convert_alpha()
menu_monke_scaled = pygame.transform.scale(menu_monke_surf,(72,88))
menu_monke_rect = menu_monke_scaled.get_rect(center = (250,200))

menu_monk_surf = pygame.image.load('PixelArt/Game1/Player/monk_stand.png').convert_alpha()
menu_monk_scaled = pygame.transform.scale(menu_monk_surf,(72,88))
menu_monk_rect = menu_monk_scaled.get_rect(center = (350,200))

menu_turt_surf = pygame.image.load('PixelArt/Game1/Player/turtle_stand.png').convert_alpha()
menu_turt_scaled = pygame.transform.scale(menu_turt_surf,(72,88))
menu_turt_rect = menu_turt_scaled.get_rect(center = (450,200))

menu_lion_surf = pygame.image.load('PixelArt/Game1/Player/lion_stand.png').convert_alpha()
menu_lion_scaled = pygame.transform.scale(menu_lion_surf,(72,88))
menu_lion_rect = menu_lion_scaled.get_rect(center = (550,200))

menu_flow_surf = pygame.image.load('PixelArt/Game1/Player/flower_stand.png').convert_alpha()
menu_flow_scaled = pygame.transform.scale(menu_flow_surf,(72,88))
menu_flow_rect = menu_flow_scaled.get_rect(center = (650,200))

menu_cyc_surf = pygame.image.load('PixelArt/Game1/Player/cyclops_stand.png').convert_alpha()
menu_cyc_scaled = pygame.transform.scale(menu_cyc_surf,(72,88))
menu_cyc_rect = menu_cyc_scaled.get_rect(center = (750,200))


cyc_1 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk1.png')
cyc_2 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk2.png')
cyc_3 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk3.png')
cyc_4 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk4.png')
cyc_5 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk5.png')
cyc_walk = [cyc_1,cyc_2,cyc_3,cyc_4,cyc_5]
cyc_walk_index = 0
cyc_surf = cyc_walk[cyc_walk_index]
cyc_rect = cyc_surf.get_rect(midbottom = (80,300))


sky_surface = pygame.image.load('PixelArt/Game1/DaySky1.png').convert() #Loads the background image
ground_surface = pygame.image.load('PixelArt/Game1/Ground.png').convert() #Loads the ground image

thumb_cloud_surf = pygame.image.load('PixelArt/Game1/Clouds/thumb_cloud.png').convert_alpha()
thumb_cloud_rect = thumb_cloud_surf.get_rect(midleft = (800,70))
# star_cloud_surf = pygame.image.load('PixelArt')

cloud1_surf = pygame.image.load('PixelArt/Game1/Clouds/cloud.png').convert_alpha()
cloud1_rect = cloud1_surf.get_rect(midleft = (400,30))

cloud2_1 = pygame.image.load('PixelArt/Game1/Clouds/Cloud2/cloud2.png').convert_alpha()
cloud2_2 = pygame.image.load('PixelArt/Game1/Clouds/Cloud2/cloud3.png').convert_alpha()
cloud2_3 = pygame.image.load('PixelArt/Game1/Clouds/Cloud2/cloud4.png').convert_alpha()
cloud2_4 = pygame.image.load('PixelArt/Game1/Clouds/Cloud2/cloud5.png').convert_alpha()
cloud2 = [cloud2_1,cloud2_2,cloud2_3,cloud2_4]
cloud2_index = 0
cloud2_surf = cloud2[cloud2_index]
cloud2_rect = cloud2_surf.get_rect(midleft = (200,100))

# score_surf = test_font.render('My game', False, (60,60,60)) #Creates a font on the display
# score_rect = score_surf.get_rect(midtop = (400,50)) #Creates a rectangle around the font and places it center

snail_surf = pygame.image.load('PixelArt/Game1/Pictures/snail/snail1.png').convert_alpha() #Loads the snail image
fly_surf = pygame.image.load('PixelArt/Game1/Pictures/Fly/Fly1.png').convert_alpha()
fly_surf = pygame.transform.rotozoom(fly_surf,0,.5)

obstacle_rect_list = []
if crab:
    player_rect = crab_rect
if liz:
    player_rect = liz_rect
if monke:
    player_rect = monke_rect
if monk:
    player_rect = monk_rect
if turt:
    player_rect = turt_rect
if lion:
    player_rect = lion_rect
if flow:
    player_rect = flow_rect 
if cyc:
    player_rect = cyc_rect

#Creates a rectangle around the player and places it on the left of the screen
player_gravity = 0 #Creates a gravity values for the player

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True: #Creates our game loop. While our loop is active, the game runs.
    for event in pygame.event.get(): #Checks for events in the game.
        if event.type == pygame.QUIT: #Checks if we clicked to close the window
            pygame.quit() #Closes the loop
            exit() #Closes the window
        if game_active == True:
            if event.type == pygame.KEYDOWN: #Checks if a key was pressed
                if event.key == pygame.K_SPACE: #If the key was space bar
                    if player_rect.bottom >= 300:
                        player_gravity = -20 #Set player gravity to -20
            if event.type == pygame.MOUSEBUTTONDOWN: #Check if a mouse button was pressed
                if player_rect.collidepoint(event.pos): #If the mouse was clicked on the player rectangle
                    if player_rect.bottom >= 300:
                        player_gravity = -20 #Set player gravity to -20
        if game_active == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_crab_rect.collidepoint(event.pos):
                    player_surf = menu_crab_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_liz_rect.collidepoint(event.pos):
                    player_surf = menu_liz_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_monke_rect.collidepoint(event.pos):
                    player_surf = menu_monke_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_monk_rect.collidepoint(event.pos):
                    player_surf = menu_monk_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_turt_rect.collidepoint(event.pos):
                    player_surf = menu_turt_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_lion_rect.collidepoint(event.pos):
                    player_surf = menu_lion_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_flow_rect.collidepoint(event.pos):
                    player_surf = menu_flow_surf
                    game_active = True
                    start_time = pygame.time.get_ticks()
                if menu_cyc_rect.collidepoint(event.pos):
                    cyc = True
                    game_active = True
                    start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),210)))


    # draw all our elements
    # update everything
    if game_active == False:
        obstacle_rect_list.clear()
        screen.blit(title_surf, (0,0))
        screen.blit(titlecard_surf, titlecard_rect)
        pygame.draw.line(screen,'#39314b',(0,200),(800,200),200)
        screen.blit(choose_surf, choose_rect)

        pygame.draw.rect(screen,'#cd6093',menu_crab_rect)
        pygame.draw.rect(screen,'#8e478c',menu_crab_rect,5)
        screen.blit(menu_crab_scaled, menu_crab_rect)

        pygame.draw.rect(screen,'#cd6093',menu_liz_rect)
        pygame.draw.rect(screen,'#8e478c',menu_liz_rect,5)
        screen.blit(menu_liz_scaled, menu_liz_rect)

        pygame.draw.rect(screen,'#cd6093',menu_monke_rect)
        pygame.draw.rect(screen,'#8e478c',menu_monke_rect,5)
        screen.blit(menu_monke_scaled, menu_monke_rect)

        pygame.draw.rect(screen,'#cd6093',menu_monk_rect)
        pygame.draw.rect(screen,'#8e478c',menu_monk_rect,5)
        screen.blit(menu_monk_scaled, menu_monk_rect)

        pygame.draw.rect(screen,'#cd6093',menu_turt_rect)
        pygame.draw.rect(screen,'#8e478c',menu_turt_rect,5)
        screen.blit(menu_turt_scaled, menu_turt_rect)

        pygame.draw.rect(screen,'#cd6093',menu_lion_rect)
        pygame.draw.rect(screen,'#8e478c',menu_lion_rect,5)
        screen.blit(menu_lion_scaled, menu_lion_rect)

        pygame.draw.rect(screen,'#cd6093',menu_flow_rect)
        pygame.draw.rect(screen,'#8e478c',menu_flow_rect,5)
        screen.blit(menu_flow_scaled, menu_flow_rect)

        pygame.draw.rect(screen,'#cd6093',menu_cyc_rect)
        pygame.draw.rect(screen,'#8e478c',menu_cyc_rect,5)
        screen.blit(menu_cyc_scaled, menu_cyc_rect)

        if menu_crab_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(crabtext_surf, crabtext_rect)

        if menu_liz_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(liztext_surf, liztext_rect)

        if menu_monke_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(monketext_surf, monketext_rect)

        if menu_monk_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(monktext_surf, monktext_rect)

        if menu_turt_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(turttext_surf, turttext_rect)

        if menu_lion_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(liontext_surf, liontext_rect)

        if menu_flow_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(flowtext_surf, flowtext_rect)

        if menu_cyc_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(cyctext_surf, cyctext_rect)
        score_message = test_font.render(f'Your High Score: {score}', False, '#b6d53c')
        score_message_rect = score_message.get_rect(center = (400,350))
        if score != 0:
            screen.blit(score_message,score_message_rect)
        

    if game_active:    
        screen.blit(sky_surface,(0,0)) #Draws the background image on our display
        screen.blit(ground_surface,(0,300)) #Draws the ground image on our display
        # pygame.draw.rect(screen,'#c0e8ec',score_rect) #Creates a background color for the score rectangle
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10) #Creates a border around the rectangle
        # screen.blit(score_surf, score_rect) #Draws the score
        cloud1_rect.left -= 3
        if cloud1_rect.right <= -50: cloud1_rect.left = 900
        screen.blit(cloud1_surf, cloud1_rect)

        cloud_animation()
        cloud2_rect.left -= 5
        if cloud2_rect.right <= 0: cloud2_rect.left = 800
        screen.blit(cloud2_surf, cloud2_rect)

        thumb_cloud_rect.left -= 2
        if thumb_cloud_rect.right <= -100: thumb_cloud_rect.left = 1000
        screen.blit(thumb_cloud_surf,thumb_cloud_rect)

        if score < display_score():
            score = display_score()

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #Player
        if crab:
            player_rect = crab_rect
            crab_animation()
            screen.blit(crab_surf, crab_rect)
        if liz:
            player_rect = liz_rect
            liz_animation()
            screen.blit(liz_surf, liz_rect)
        if monke:
            player_rect = monke_rect
            monke_animation()
            screen.blit(monke_surf, monke_rect)
        if monk:
            player_rect = monk_rect
            monk_animation()
            screen.blit(monk_surf, monk_rect)
        if turt:
            player_rect = turt_rect
            turt_animation()
            screen.blit(turt_surf, turt_rect)
        if lion:
            player_rect = lion_rect
            lion_animation()
            screen.blit(lion_surf, lion_rect)
        if flow:
            player_rect = flow_rect
            flow_animation()
            screen.blit(flow_surf, flow_rect) 
        if cyc:
            player_rect = cyc_rect
            cyc_animation()
            screen.blit(cyc_surf, cyc_rect)
        
            
        if player_rect.bottom >= 300: player_rect.bottom = 300 #If the player's bottom goes below the ground, set it above ground
        player_gravity += 1 #Every frame, the player gravity goes up by 1
        player_rect.bottom += player_gravity #The bottom of the player gets dragged by the gravity every frame

        #Collisions
        game_active = collisions(player_rect,obstacle_rect_list)

    pygame.display.update() #Updates the display every frame
    clock.tick(60) #Sets our frame rate