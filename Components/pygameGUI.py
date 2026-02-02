import pygame

class labelFrame(pygame.Rect):
    def __init__(self, left, top, width, height, **kwargs):
        super().__init__(left, top, width, height)
        self.label = kwargs.get("label", "")
        self.autoSize = kwargs.get("autoSize", False)
        self.textSize = kwargs.get("textSize", 36)
        self.textColor = kwargs.get("color", (0,0,0))
        self.backgroundColor = kwargs.get("backgroundColor", (255,255,255))
        self.paddingX = kwargs.get("paddingX", 0)
        self.paddingY = kwargs.get("paddingY", 0)
        self.create_Label()

    def create_Label(self):
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        if self.autoSize:
            self.update((self.left, self.top), (font.size(self.label)))
        self.text = font.render(self.label, True, self.textColor)

    def addPadding(self):
        paddingRect = pygame.Rect(self.left + self.paddingX*.5, self.top + self.paddingY*.5, 
                                  self.width + self.paddingX*.5, self.height + self.paddingY*.5)
        return paddingRect

    def draw(self, surface):
        pygame.draw.rect(surface, self.backgroundColor, self.addPadding())
        surface.blit(self.text, self.text.get_rect(center=self.addPadding().center))

class button(labelFrame):
    def __init__(self, left, top, width, height, **kwargs):
        super().__init__(left, top, width, height, **kwargs)
        self.func = kwargs.get("func", self.default)

    def mouseClicked(self, mouse_pos):
        if (mouse_pos[1] < self.height + self.top and mouse_pos[1] > self.top and
            mouse_pos[0] > self.left and mouse_pos[0] < self.left + self.width):

            self.action()
            return True
        return False

    def default(self):
        print("This button was pressed!")

    def action(self):
        self.func()
