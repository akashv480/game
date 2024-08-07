
import pygame
import sys
from scripts.entity import physicsentity


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Epic dual')
        self.screen = pygame.display.set_mode((800,800))
        
        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('assests\pngtree-nube-pixel-art-png-image_13436335-removebg-preview.png')
        
        self.img_pos = [2,3]
        
        self.movement = [False,False]
        
        self.img.set_colorkey((64,224,208))
        
        self.collision_area = pygame.Rect(50,50,300,50)
        
        self.player = physicsentity(self , 'player' , (50,50) , (8,15))
        
        
#gmae loop where all event has been working
    def run(self):
        while True:
            self.screen.fill((64,224,208))
            
            self.img_pos[1] += ( self.movement[1] - self.movement[0]) * 5 
            
            self.screen.blit(self.img,self.img_pos)
            
            img_r = pygame.Rect(self.img_pos[0] , self.img_pos[1] , self.img.get_width() , self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen , (0,100,255) , self.collision_area)
            else:
                pygame.draw.rect(self.screen , (0,255,100) , self.collision_area)
            
            for event in pygame.event.get():
              if event.type==pygame.QUIT:
                  pygame.Quit()
                  sys.exit()

            # movement
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: 
                    self.movment[0] = True
                if event.key == pygame.K_DOWN:
                    self.movement[1] = True
              if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP: 
                    self.movment[0] = False
                if event.key == pygame.K_DOWN:
                    self.movement[1] = False


            pygame.display.update()
            self.clock.tick(60)
Game().run()  
              
