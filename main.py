from cgi import test
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
       
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                if upward:
                    obstacle_rect.top -= 3
                if obstacle_rect.top <= 150:
                    upward = False               
                if upward == False:
                    obstacle_rect.bottom += 3
                if obstacle_rect.bottom >= 225:
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



def crab_animation():
    global crab_surf, crab_walk_index
    crab_walk_index += 0.5
    if crab_walk_index >= len(crab_walk):crab_walk_index = 0
    crab_surf = crab_walk[int(crab_walk_index)]

def liz_animation():
    global liz_surf, liz_walk_index
    liz_walk_index += 0.5
    if liz_walk_index >= len(liz_walk):liz_walk_index = 0
    liz_surf = liz_walk[int(liz_walk_index)]

def monke_animation():
    global monke_surf, monke_walk_index
    monke_walk_index += 0.5
    if monke_walk_index >= len(monke_walk):monke_walk_index = 0
    monke_surf = monke_walk[int(monke_walk_index)]

def monk_animation():
    global monk_surf, monk_walk_index
    monk_walk_index += 0.5
    if monk_walk_index >= len(monk_walk):monk_walk_index = 0
    monk_surf = monk_walk[int(monk_walk_index)]

def turt_animation():
    global turt_surf, turt_walk_index
    turt_walk_index += 0.5
    if turt_walk_index >= len(turt_walk):turt_walk_index = 0
    turt_surf = turt_walk[int(turt_walk_index)]

def lion_animation():
    global lion_surf, lion_walk_index
    lion_walk_index += 0.5
    if lion_walk_index >= len(lion_walk):lion_walk_index = 0
    lion_surf = lion_walk[int(lion_walk_index)]

def flow_animation():
    global flow_surf, flow_walk_index
    flow_walk_index += 0.5
    if flow_walk_index >= len(flow_walk):flow_walk_index = 0
    flow_surf = flow_walk[int(flow_walk_index)]

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
char_select = True
stage_select = False
game_active = False


start_time = 0
crab_score = 0
liz_score = 0
monke_score = 0
monk_score = 0
turt_score = 0
lion_score = 0
flow_score = 0
cyc_score = 0
upward = True
crab = False
liz = False
monke = False
monk = False
turt = False
lion = False
flow = False
cyc = False

beach = False
city = False


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


crab_1 = pygame.image.load('PixelArt/Game1/Player/crab/crabman_walk1.png')
crab_2 = pygame.image.load('PixelArt/Game1/Player/crab/crabman_walk2.png')
crab_3 = pygame.image.load('PixelArt/Game1/Player/crab/crabman_walk3.png')
crab_4 = pygame.image.load('PixelArt/Game1/Player/crab/crabman_walk4.png')
crab_walk = [crab_1,crab_2,crab_3,crab_4]
crab_walk_index = 0
crab_surf = crab_walk[crab_walk_index]
crab_rect = crab_surf.get_rect(midbottom = (80,300))


liz_1 = pygame.image.load('PixelArt/Game1/Player/lizard/lizardman_walk1.png')
liz_2 = pygame.image.load('PixelArt/Game1/Player/lizard/lizardman_walk2.png')
liz_walk = [liz_1,liz_2]
liz_walk_index = 0
liz_surf = liz_walk[liz_walk_index]
liz_rect = liz_surf.get_rect(midbottom = (80,300))

monke_1 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk1.png')
monke_2 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk2.png')
monke_3 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk3.png')
monke_4 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk4.png')
monke_5 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk5.png')
monke_6 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk6.png')
monke_7 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk7.png')
monke_8 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk8.png')
monke_9 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk9.png')
monke_10 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk10.png')
monke_11 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk11.png')
monke_12 = pygame.image.load('PixelArt/Game1/Player/monke/monke_walk12.png')
monke_walk = [monke_1,monke_2,monke_3,monke_4,monke_5,monke_6,monke_7,monke_8,monke_9,monke_10,monke_11,monke_12]
monke_walk_index = 0
monke_surf = monke_walk[monke_walk_index]
monke_rect = monke_surf.get_rect(midbottom = (80,300))


monk_1 = pygame.image.load('PixelArt/Game1/Player/monk/monk_walk1.png')
monk_2 = pygame.image.load('PixelArt/Game1/Player/monk/monk_walk2.png')
monk_walk = [monk_1,monk_2]
monk_walk_index = 0
monk_surf = monk_walk[monk_walk_index]
monk_rect = monk_surf.get_rect(midbottom = (80,300))


turt_1 = pygame.image.load('PixelArt/Game1/Player/turt/turt_walk1.png')
turt_2 = pygame.image.load('PixelArt/Game1/Player/turt/turt_walk2.png')
turt_3 = pygame.image.load('PixelArt/Game1/Player/turt/turt_walk3.png')
turt_4 = pygame.image.load('PixelArt/Game1/Player/turt/turt_walk4.png')
turt_walk = [turt_1, turt_2, turt_3, turt_4]
turt_walk_index = 0
turt_surf = turt_walk[turt_walk_index]
turt_rect = turt_surf.get_rect(midbottom = (80,300))


lion_1 = pygame.image.load('PixelArt/Game1/Player/lion/lion_walk1.png')
lion_2 = pygame.image.load('PixelArt/Game1/Player/lion/lion_walk2.png')
lion_3 = pygame.image.load('PixelArt/Game1/Player/lion/lion_walk3.png')
lion_4 = pygame.image.load('PixelArt/Game1/Player/lion/lion_walk4.png')
lion_walk = [lion_1,lion_2,lion_3,lion_4]
lion_walk_index = 0
lion_surf = lion_walk[lion_walk_index]
lion_rect = lion_surf.get_rect(midbottom = (80,300))


flow_1 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk1.png')
flow_2 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk2.png')
flow_3 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk3.png')
flow_4 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk4.png')
flow_5 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk5.png')
flow_6 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk6.png')
flow_7 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk7.png')
flow_8 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk8.png')
flow_9 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk9.png')
flow_10 = pygame.image.load('PixelArt/Game1/Player/flow/flow_walk10.png')
flow_walk = [flow_1,flow_2,flow_3,flow_4,flow_5,flow_6,flow_7,flow_8,flow_9,flow_10]
flow_walk_index = 0
flow_surf = flow_walk[flow_walk_index]
flow_rect = flow_surf.get_rect(midbottom = (80,300))


cyc_1 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk1.png')
cyc_2 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk2.png')
cyc_3 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk3.png')
cyc_4 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk4.png')
cyc_5 = pygame.image.load('PixelArt/Game1/Player/cyclops/cyclops_walk5.png')
cyc_walk = [cyc_1,cyc_2,cyc_3,cyc_4,cyc_5]
cyc_walk_index = 0
cyc_surf = cyc_walk[cyc_walk_index]
cyc_rect = cyc_surf.get_rect(midbottom = (80,300))



stage_text = test_font.render('Select a Stage',False,'#b6d53c')
stage_text = pygame.transform.rotozoom(stage_text,0,2.5)
stage_text_rect = stage_text.get_rect(center = (400,200))

beach_surface = pygame.image.load('PixelArt/Game1/stages/beach/beach.png').convert()
beach_stage = pygame.transform.rotozoom(beach_surface,0,0.25)
beach_rect = beach_stage.get_rect(center = (200,75))

city_surface = pygame.image.load('PixelArt/Game1/stages/city/city.png').convert()
city_stage = pygame.transform.rotozoom(city_surface,0,0.25)
city_rect = city_stage.get_rect(center = (600,75))

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
        if char_select:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_crab_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    crab = True
                    start_time = pygame.time.get_ticks()
                if menu_liz_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    liz = True
                    start_time = pygame.time.get_ticks()
                if menu_monke_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    monke = True
                    start_time = pygame.time.get_ticks()
                if menu_monk_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    monk = True
                    start_time = pygame.time.get_ticks()
                if menu_turt_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    turt = True
                    start_time = pygame.time.get_ticks()
                if menu_lion_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    lion = True
                    start_time = pygame.time.get_ticks()
                if menu_flow_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    flow = True
                    start_time = pygame.time.get_ticks()
                if menu_cyc_rect.collidepoint(event.pos):
                    char_select = False
                    stage_select = True
                    cyc = True
                    start_time = pygame.time.get_ticks()

        if stage_select:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if beach_rect.collidepoint(event.pos):
                    stage_select = False
                    game_active = True
                    beach = True
                if city_rect.collidepoint(event.pos):
                    stage_select = False
                    game_active = True
                    city = True

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),210)))


    # draw all our elements
    # update everything
    if char_select:
        crab = False
        liz = False
        monke = False
        monk = False
        turt = False
        lion = False
        flow = False
        cyc = False
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
            score_message = test_font.render(f'Lord Crab High Score: {crab_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if crab_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_liz_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(liztext_surf, liztext_rect)
            score_message = test_font.render(f'Liz the Wiz High Score: {liz_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if liz_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_monke_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(monketext_surf, monketext_rect)
            score_message = test_font.render(f'Monke High Score: {monke_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if monke_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_monk_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(monktext_surf, monktext_rect)
            score_message = test_font.render(f'Gandalf the Wise High Score: {monk_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if monk_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_turt_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(turttext_surf, turttext_rect)
            score_message = test_font.render(f'Michaelangelo High Score: {turt_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if turt_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_lion_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(liontext_surf, liontext_rect)
            score_message = test_font.render(f'Simba High Score: {lion_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if lion_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_flow_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(flowtext_surf, flowtext_rect)
            score_message = test_font.render(f'Ralta the Formidable High Score: {flow_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if flow_score != 0:
                screen.blit(score_message,score_message_rect)

        if menu_cyc_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(cyctext_surf, cyctext_rect)
            score_message = test_font.render(f'Steve High Score: {cyc_score}', False, '#b6d53c')
            score_message_rect = score_message.get_rect(center = (400,350))
            if cyc_score != 0:
                screen.blit(score_message,score_message_rect)

    if stage_select:
        beach = False
        city = False
        screen.blit(title_surf, (0,0))
        pygame.draw.line(screen,'#39314b',(0,200),(800,200),100)
        pygame.draw.line(screen,'#397b44',(0,75),(400,75),150)
        pygame.draw.line(screen,'#71aa34',(400,75),(800,75),150)
        pygame.draw.line(screen,'#71aa34',(0,325),(400,325),150)
        pygame.draw.line(screen,'#397b44',(400,325),(800,325),150)
        screen.blit(stage_text,stage_text_rect)
        screen.blit(beach_stage,beach_rect)
        screen.blit(city_stage,city_rect)
        
        

    if game_active:
        if beach: 
            screen.blit(beach_surface,(0,0))
        if city:
            screen.blit(city_surface,(0,0)) #Draws the background image on our display
        #Draws the ground image on our display
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
            

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #Player
        if crab:
            player_rect = crab_rect
            crab_animation()
            screen.blit(crab_surf, crab_rect)
            if crab_score < display_score():
                crab_score = display_score()
        if liz:
            player_rect = liz_rect
            liz_animation()
            screen.blit(liz_surf, liz_rect)
            if liz_score < display_score():
                liz_score = display_score()
        if monke:
            player_rect = monke_rect
            monke_animation()
            screen.blit(monke_surf, monke_rect)
            if monke_score < display_score():
                monke_score = display_score()
        if monk:
            player_rect = monk_rect
            monk_animation()
            screen.blit(monk_surf, monk_rect)
            if monk_score < display_score():
                monk_score = display_score()
        if turt:
            player_rect = turt_rect
            turt_animation()
            screen.blit(turt_surf, turt_rect)
            if turt_score < display_score():
                turt_score = display_score()
        if lion:
            player_rect = lion_rect
            lion_animation()
            screen.blit(lion_surf, lion_rect)
            if lion_score < display_score():
                lion_score = display_score()
        if flow:
            player_rect = flow_rect
            flow_animation()
            screen.blit(flow_surf, flow_rect)
            if flow_score < display_score():
                flow_score = display_score() 
        if cyc:
            player_rect = cyc_rect
            cyc_animation()
            screen.blit(cyc_surf, cyc_rect)
            if cyc_score < display_score():
                cyc_score = display_score()
        
            
        player_gravity += 1 #Every frame, the player gravity goes up by 1
        player_rect.bottom += player_gravity #The bottom of the player gets dragged by the gravity every frame
        if player_rect.bottom >= 300: player_rect.bottom = 300 #If the player's bottom goes below the ground, set it above ground

        #Collisions
        game_active = collisions(player_rect,obstacle_rect_list)
    if game_active == False and stage_select == False:
        char_select = True

    pygame.display.update() #Updates the display every frame
    clock.tick(60) #Sets our frame rate