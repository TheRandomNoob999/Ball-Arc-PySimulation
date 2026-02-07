import pygame
from Core import objects as obj

class labelFrame(pygame.Rect):
    def __init__(self, left, top, width, height, **kwargs) -> None:
        super().__init__(left, top, width, height)
        self.label = kwargs.get("label", "")
        self.autoSize = kwargs.get("autoSize", False)
        self.textSize = kwargs.get("textSize", 36)
        self.textColor = kwargs.get("color", (0,0,0))
        self.backgroundColor = kwargs.get("backgroundColor", (255,255,255))
        self.paddingX = kwargs.get("paddingX", 0)
        self.paddingY = kwargs.get("paddingY", 0)
        self.create_Label()

    def create_Label(self) -> None:
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        if self.autoSize:
            self.update((self.left, self.top), (font.size(self.label)))
        self.text = font.render(self.label, True, self.textColor)

    def addPadding(self) -> pygame.Rect:
        paddingRect = pygame.Rect(self.left + self.paddingX*.5, self.top + self.paddingY*.5, 
                                  self.width + self.paddingX*.5, self.height + self.paddingY*.5)
        return paddingRect

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.backgroundColor, self.addPadding())
        surface.blit(self.text, self.text.get_rect(center=self.addPadding().center))

class button(labelFrame):
    def __init__(self, left, top, width, height, **kwargs) -> None:
        super().__init__(left, top, width, height, **kwargs)
        self.func = kwargs.get("func", self.default)

    def mouseClicked(self, mouse_pos) -> bool:
        if (mouse_pos[1] < self.height + self.top and mouse_pos[1] > self.top and
            mouse_pos[0] > self.left and mouse_pos[0] < self.left + self.width):

            self.action()
            return True
        return False

    def default(self) -> None:
        print("This button was pressed!")

    def action(self) -> None:
        self.func()

class dropDownMenu(button):
    def __init__(self, left, top, width ,height, **kwargs) -> None:
        super().__init__(left, top, width, height, **kwargs)
        self.menuOptions = kwargs.get("menu", None)
        self.open = False
        self.objectManager = kwargs.get("manager", None)
    
    def action(self) -> None:
        print("Dropdown menu clicked")
        if not self.open:
            self.open = True
            optionCount = 0
            for option in self.menuOptions:
                optionCount += 1
                option.update(self.left, self.top + self.height*optionCount, self.width, self.height)
                self.objectManager.addGUI(option)
        else:
            self.open = False
            for option in self.menuOptions:
                self.objectManager.removeGUI(option)

def getFontSize(size, text):
    font = pygame.font.Font('freesansbold.ttf', size)
    return font.size(text)