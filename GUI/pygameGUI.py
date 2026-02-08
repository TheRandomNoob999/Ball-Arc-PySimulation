import pygame

class Frame(pygame.Rect):
    def __init__(self, left, top, width, height, **kwargs) -> None:
        super().__init__(left, top, width, height)
        self.backgroundColor = kwargs.get("backgroundColor", (255,255,255))
        self.paddingX = kwargs.get("paddingX", 0)
        self.paddingY = kwargs.get("paddingY", 0)
        self.parent = kwargs.get("parent", None)
        self.children = kwargs.get("children", [])
    
    def setParent(self, object) -> None:
        self.parent = object
    
    def removeParent(self) -> None:
        self.parent = None

    def addChild(self, object) -> None:
        self.children.append(object)
        object.setParent(self)

        # Moves Child based on Parent
        object.update(self.left + object.left, self.top + object.top, object.width, object.height)
    
    def removeChild(self, object) -> None:
        self.children.remove(object)
        object.removeParent()

        # Moves child to original coordinates
        object.update(object.left, object.top, object.width, object.height)
    
    def getChild(self, target):
        for child in self.getChildren():
            if child == target:
                return child 
        
        return "Can't find child"

    def getChildren(self) -> list:
        return self.children
    
    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.backgroundColor, self.addPadding())

        #Checks and draws all children since they're not added to ObjectManager GUI list
        if len(self.getChildren()) >= 1:
            for child in self.getChildren():
                if callable(getattr(child, "draw", None)):
                    child.draw(surface)

    def changePadding(self, x, y) -> None:
        self.paddingX = x
        self.paddingY = y

    def addPadding(self) -> pygame.Rect:
        paddingRect = pygame.Rect(self.left + self.paddingX*.5, self.top + self.paddingY*.5, 
                                  self.width + self.paddingX*.5, self.height + self.paddingY*.5)
        return paddingRect

class labelFrame(Frame):
    def __init__(self, left, top, width, height, **kwargs) -> None:
        super().__init__(left, top, width, height, **kwargs)
        self.label = kwargs.get("label", "")
        self.autoSize = kwargs.get("autoSize", False)
        self.textSize = kwargs.get("textSize", 36)
        self.textColor = kwargs.get("color", (0,0,0))

    def create_Label(self) -> None:
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        if self.autoSize:
            self.update((self.left, self.top), (font.size(self.label)))
        self.text = font.render(self.label, True, self.textColor)

    def draw(self, surface) -> None:
        self.create_Label()
        pygame.draw.rect(surface, self.backgroundColor, self.addPadding())
        if self.label != "":
            surface.blit(self.text, self.text.get_rect(center=self.addPadding().center))
        
        #Draws all children since they're not added to ObjectManager GUI list
        if len(self.getChildren()) >= 1:
            for child in self.getChildren():
                if callable(getattr(child, "draw", None)):
                    child.draw(surface)

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
    
    def setFunc(self, function) -> None:
        self.func = function

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

def getFontSize(size, text) -> tuple[int, int]:
    font = pygame.font.Font('freesansbold.ttf', size)
    return font.size(text)