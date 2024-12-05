import pygame
import os 
import sys
pygame.font.init()
pygame.mixer.init()

#caption
pygame.display.set_caption("spaceship wars")



#windows mesa7a
WIDTH,HEIGHT=800,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

#sounds

victory=pygame.mixer.Sound('items/victory.mp3')
fire=pygame.mixer.Sound('items/laser1.wav')

#colors
white=((255,255,255))
red=((255,0,0))
black=((0,0,0))
green=((0,255,0))
red=((255,0,0))
transpernt=(0,0,0,0)

#fps
FPS=60

#health bar
rhealth = 200
lhealth =  200
health_bar_height = 10 
healthbar_left=pygame.Rect(25,25,lhealth,health_bar_height)
healthbar_right =pygame.Rect(575,25,rhealth,health_bar_height)
lred_bar=pygame.Rect(25,25,200,10)
rred_bar=pygame.Rect(575,25,200,10)


#the border in the middle 
border=pygame.Rect(WIDTH/2 -10 ,0,5,HEIGHT)


#new event
left_hit = pygame.USEREVENT +  1
right_hit = pygame.USEREVENT + 2

#winner quote 
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

#spaceships
VEL=5
left_spaceship_image=pygame.transform.rotate(pygame.image.load(os.path.join('items','WhiteSpaceship.png')),270)
right_spaceship_image=pygame.image.load(os.path.join('items','RedSpaceship.png'))
spaceship_width,spaceship_height=55,50
left_spaceship=pygame.transform.scale(left_spaceship_image,(spaceship_width,spaceship_height))
right_spaceship=pygame.transform.rotate(pygame.transform.scale(right_spaceship_image,(spaceship_width,spaceship_height)),90)
left_health=10
right_health=10

#bullet
bullet_image=pygame.image.load(os.path.join('items','Bullet.png'))
MAX_BULLETS = 6
bullet_width,bullet_height = 30 ,35
bullet_image=pygame.image.load(os.path.join('items','Bullet.png'))
bullet_left=pygame.transform.rotate(pygame.transform.scale(bullet_image,(bullet_width,bullet_height)),270)
bullet_right=pygame.transform.rotate(pygame.transform.scale(bullet_image,(bullet_width,bullet_height)),90)
bullets_vel = 8

#background
background = pygame.image.load(os.path.join('items','background.png'))




def draw_window(left,right,left_bullets,right_bullets):
        
        global lhealth , rhealth 
        WIN.blit(background,(0,0))
        pygame.draw.rect(WIN,transpernt,border)
        pygame.draw.rect(WIN,red,rred_bar)
        pygame.draw.rect(WIN,red,lred_bar)
        healthbar_left.width = lhealth
        healthbar_right.width = rhealth
        pygame.draw.rect(WIN,green,healthbar_left)
        pygame.draw.rect(WIN,green,healthbar_right)
        WIN.blit(left_spaceship,(left.x,left.y))
        WIN.blit(right_spaceship,(right.x,right.y))
        
        for bullet in left_bullets:
            WIN.blit(bullet_left, (bullet.x, bullet.y))

        for bullet in right_bullets:
            WIN.blit(bullet_right, (bullet.x, bullet.y))             
       
        pygame.display.update()



def left_movment (keys_pressed,left):
     if keys_pressed[pygame.K_w] and left.y - VEL > 30 :
          left.y -= VEL
     if keys_pressed[pygame.K_s] and left.y + VEL + spaceship_width < HEIGHT  :
          left.y += VEL
     if keys_pressed[pygame.K_a] and left.x + VEL - 15 > 0  :
          left.x -= VEL
     if keys_pressed[pygame.K_d] and left.x + VEL < border.x - 50 :
          left.x += VEL


def right_movement (keys_pressed,right):
     if keys_pressed[pygame.K_UP] and right.y - VEL  > 30  :
          right.y -= VEL
     if keys_pressed[pygame.K_DOWN] and right.y + spaceship_width + VEL < HEIGHT :
          right.y += VEL
     if keys_pressed[pygame.K_LEFT] and right.x -VEL > border.x :
          right.x -= VEL
     if keys_pressed[pygame.K_RIGHT] and right.x + VEL + spaceship_width < WIDTH :
          right.x += VEL          





def handle_bullets(left_bullets , right_bullets , left , right ):
        for bullet in left_bullets:
             bullet.x +=bullets_vel

             if right.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(right_hit))
                  left_bullets.remove(bullet)

             elif bullet.x > WIDTH:
                  left_bullets.remove(bullet)
                  
 
                
        for bullet in right_bullets:
             bullet.x -=bullets_vel

             if left.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(left_hit))
                  right_bullets.remove(bullet)

             elif bullet.x < 0 :
                  right_bullets.remove(bullet)     
  

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, white)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /  
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    victory.play()
    pygame.time.delay(5000)                  


def main():
    running = True
    left=pygame.Rect(100,300,spaceship_width-5,spaceship_height)
    right=pygame.Rect(700,300,spaceship_width-5,spaceship_height)
    clock=pygame.time.Clock()

    left_bullets=[]
    right_bullets=[]
    global lhealth , rhealth

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                running = False
            
             if event.type ==pygame.KEYDOWN:
                 
                 if event.key== pygame.K_LCTRL and len(left_bullets) < MAX_BULLETS:
                      bullet=pygame.Rect(left.x + spaceship_width - 15  , left.y + spaceship_height//2  - 13 , bullet_width , bullet_height)
                      left_bullets.append(bullet)
                      fire.play()

                 if event.key== pygame.K_RCTRL and len(right_bullets) < MAX_BULLETS:
                      bullet=pygame.Rect(right.x - spaceship_width +30 , right.y + spaceship_height//2 - 13  , bullet_width , bullet_height )
                      right_bullets.append(bullet)
                      fire.play()
             
             if event.type == left_hit:
                  lhealth -=25
                  
                  

             if event.type == right_hit:
                  rhealth-=25



        winner_text =""
        
        if rhealth <= 0 :
             winner_text="left WINS"
             

        if lhealth <= 0 :
             winner_text="right WINS"
             
        if winner_text != "":
             draw_winner(winner_text)
             
             break

        
        keys_pressed = pygame.key.get_pressed()
        handle_bullets(left_bullets , right_bullets , left ,right)
        draw_window(left,right,left_bullets,right_bullets)
        left_movment(keys_pressed,left)
        right_movement(keys_pressed,right)

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()