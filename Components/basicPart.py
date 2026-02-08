class BasicPart():
    def __init__(self, **kwargs) -> None:
        self.position = kwargs.get('position', (0,0))
        self.radius = kwargs.get('radius', 1)
        self.width = kwargs.get('width', 1)
        self.friction = kwargs.get('friction', 1)
        self.elasticity = kwargs.get('elasticity', 1)
        self.color = kwargs.get('color', (255,255,255))
        self.amount = kwargs.get('amount', 1)
        self.space = kwargs.get('space', None)
        self.screen = kwargs.get('screen', None)

    def flipy(self, y, screenYSize) -> int:
        return -y + screenYSize