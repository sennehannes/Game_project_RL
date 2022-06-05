import pygame

class game():

    def __init__(self, screen, target_fps):
        self.screen = screen
        self.width = self.screen.get_size()[0]
        self.height = self.screen.get_size()[1]
        self.target_fps = target_fps
        self.screen_color=(255,255,255)
        self.running = True
        self.paused = False

    def run(self):
        screen.fill(self.screen_color)
        image = pygame.image.load("sprites/characters/player.png")
        screen.blit(image, dest = (0,0))
        while(self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    print("a key has been pressed")
                    if event.key == pygame.K_m:
                        print("m has been pressed")
            pygame.display.update()
        
if __name__ == '__main__':
    pygame.init()
    is_initialized = pygame.get_init()
    while is_initialized == False:
        pygame.init()
        print("reinitialize pygame")
    disp_size = (1280,720)
    screen = pygame.display.set_mode(disp_size)
    pygame.display.set_caption('adventure')
    game(screen,60).run()
    pygame.quit
    exit()