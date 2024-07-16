import pygame

class button:
    def __init__(self,surface,text,color, textColor = (0,0,0)):
        self.surface = surface
        self.text = text
        self.color = color
        self.textColor = textColor
        self.x, self.y = None,None
        self.w, self.h = None,None
    
    def draw_button(self,x,y,w,h):
        self.x, self.y = x,y
        self.w, self.h = w,h
        pygame.draw.rect(self.surface, self.color, (x, y, w, h))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.textColor)
        self.surface.blit(text_surface, (x + (w - text_surface.get_width()) // 2, y + (h - text_surface.get_height()) // 2))

    def click_button(self,click_function):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.w and self.y <= mouse[1] <= self.y + self.h :
            click_function()
