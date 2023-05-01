#setup---------------------------------------
import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
from pygame.locals import*
offset=[0,0]
mainClock = pygame.time.Clock()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
screen_width=1600
screen_height=900
#text----------------------------------------
score=0
misses=0
accuracy =0
font = pygame.font.Font(None, 20)
text = font.render("Hits: "+str(score)+"    Misses: "+str(misses),True, (255, 255, 255))
text2 = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 255, 255))
               
text_rect = text.get_rect(center=(screen_width/2, 50))
text2_rect = text2.get_rect(center=(screen_width/1.7, 50))
#hitsound-------------------------------------
pygame.mixer.init()
pygame.mixer.music.load('hit.ogg')



screen=pygame.display.set_mode([screen_width,screen_height])
bg_img = pygame.image.load('background.jpg')
bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))
red=(255,0,0)

xx=random.randint(20,screen_width-20)
xy=random.randint(20,screen_height-20)
radius_circle=(9)



#loop---------------------------------------
run=True
while run:
    screen.blit(bg_img, (0, 0))
    #screen.blit(text, text_rect) 
    
#buttons---------------------------------------
    for event in pygame.event.get():       
        if event.type==pygame.QUIT:  
            run=False
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()[0]
    qx=(x-xx)**2
    qy=(y-xy)**2
    if math.sqrt(qx+qy)<radius_circle and click==1:
        score=score+1
        text = font.render("Hits: "+str(score)+"Misses: "+str(misses),True, (255, 255, 255))
        pygame.mixer.music.play()
        xx=random.randint(20,screen_width-20)
        xy=random.randint(20,screen_height-20)
        if score+misses==0:
             accuracy=0
             text2 = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 255, 255))
        else:
            text2 = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 255, 255))
            accuracy = score / (score + misses) * 100
       
    elif math.sqrt(qx+qy)>radius_circle and click==1:
        misses+=1
        text = font.render("Hits: "+str(score)+"Misses: "+str(misses),True, (255, 255, 255))

        text2 = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 255, 255))
        print(misses,score)
        accuracy = score / (score + misses) * 100
        if score+misses==0:
             accuracy=0
             text2 = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 255, 255))
        else:
            text2 = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 255, 255))
            accuracy = score / (score + misses) * 100
        
        
    pygame.draw.circle(screen,red,(xx,xy),radius_circle)
    #

    screen.blit(text, text_rect)

    screen.blit(text2, text2_rect)
    pygame.display.update()
    mainClock.tick(15)
pygame.quit() 
    
