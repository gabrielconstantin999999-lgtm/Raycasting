import pygame 


class Button:
    def __init__(self,x,y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = pygame.font.SysFont("Arial", 50)
    def draw(self,screen,text,text_color):
        text_display = self.font.render(text, False,text_color)
        pygame.draw.rect(screen,(self.color),(self.x,self.y,self.width,self.height))
        screen.blit(text_display,((self.x + self.width/2 - text_display.get_width()/2),(self.y + self.height/2 - text_display.get_height()/2)))
    def get_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] and self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            return True
        else:
            return False
