import pygame

class game():

    def __init__(self, screen, target_fps):
        self.screen = screen
        self.width = self.screen.get_size()[0]
        self.height = self.screen.get_size()[1]
        self.target_fps = target_fps
        self.running = True
        self.paused = False

    def run(self):
        while(self.running):
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      self.running = False
            pygame.display.update()
        



if __name__ == '__main__':
    pygame.display.init()
    disp_size = (1280,720)
    screen = pygame.display.set_mode(disp_size)
    pygame.display.set_caption('adventure')
    game(screen,60).run()

    pygame.quit
    exit()