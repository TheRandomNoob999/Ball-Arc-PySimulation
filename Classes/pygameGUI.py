import pygame

class frame():
    def __init__(self):
        pass

class labelFrame():
    def __init__(self):
        pass

class button():
    def __init__(self, left, top, width, height, color, label):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.label = label
    #    self.create_Label()
        self.rect = pygame.Rect(left, top, width, height)
        
    #def create_Label(self):
    #    font = pygame.font.Font('freesansbold.ttf', 23)
    #    print(pygame.font.Font.size(font, self.label))
    #    self.text = font.render(self.label, True, (0,0,0))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    #    surface.blit(self.text, self.rect)

    def mouseClicked(self, mouse_pos):
        if (mouse_pos[1] < self.height + self.top and mouse_pos[1] > self.top and
            mouse_pos[0] > self.left and mouse_pos[0] < self.left + self.width):

            self.action()

    def action(self):
        print("Button is clicked")

class labelButton():
    def __init__(self):
        pass