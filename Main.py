import pygame, sys
import random


class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/runner.png")
        self.position = [x, y]
        self.name = "Pajaro"
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #self.__screen.fill((0, 255, 0))
        self.__background = pygame.image.load("images/bg.jpg")
        pygame.display.set_caption("Carrera de bichos")
        
        firstRunner = Runner(self.__startLine,0)
        firstRunner.name = "Speedy"
        self.runners.append(firstRunner)

        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            self.runners[0].avanzar()
            
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado".format(self.runners[0].name))
                gameOver = True
            
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runners[0].custome, self.runners[0].position) #Como si fuesen rutas 
             
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
        
        
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()