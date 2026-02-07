from Presets import loaders as sets
from Components import arc
from Components import ball

class objectManager():
    def __init__(self, space):
        self.space = space
        self.BALLSET = {}
        self.ARCSET = {}
        self.BALLS = []
        self.ARCS = []
        self.GUI_ELEMENTS = []
    
    def step(self):
        dt = 1.0 / 60.0
        for x in range(1):
            self.space.step(dt)

    def loadSets(self, fileName) -> None:
        for ball in self.BALLS:
            self.removeBall(ball)
        for arc in self.ARCS:
            for segment in arc.segment_shapes:
                self.space.remove(segment)
            self.ARCS.remove(arc)

        self.ARCSET = sets.loadArcSet(fileName)
        self.BALLSET = sets.loadBallSet(fileName)
        print("LOADED SET: " + fileName)

    def addArcs(self, _space, _screen) -> None:
        if self.ARCSET != {}:
            if len(self.ARCS) < self.ARCSET["amount"]:
                    new_arc = arc.Arc(
                        position = self.ARCSET["position"],
                        friction = self.ARCSET["friction"],
                        elasticity = self.ARCSET["elasticity"],
                        radius = self.ARCSET["radius"],
                        width = self.ARCSET["width"],
                        color = self.ARCSET["color"],
                        segments = self.ARCSET["segments"],
                        rotation_speed = self.ARCSET["rotation_speed"],
                        start_angle = self.ARCSET["start_angle"],
                        end_angle = self.ARCSET["end_angle"],
                        space = _space,
                        screen = _screen
                    )

                    # Makes the arcs not overlap
                    if len(self.ARCS) >= 1:
                        new_arc.set_radius(new_arc.get_radius() + 100)
                        new_arc.randomize_rotation()
                        self.ARCSET["radius"] += 100

                    self.ARCS.append(new_arc)

    def addBalls(self, _space, _screen) -> None:
        if self.BALLSET != {}:
            if len(self.BALLS) < self.BALLSET["amount"]:
                   new_ball = ball.Ball(
                       mass = self.BALLSET["mass"],
                       moment = self.BALLSET["moment"],
                       position = self.BALLSET["position"],
                       friction = self.BALLSET["friction"],
                       elasticity = self.BALLSET["elasticity"],
                       radius = self.BALLSET["radius"],
                       width = self.BALLSET["width"],
                       color = self.BALLSET["color"],
                       space = _space,
                       screen = _screen
                   )
                   new_ball.create_ball()
                   self.BALLS.append(new_ball)

    def removeBall(self, ball) -> None:
        self.space.remove(ball.shape, ball.body)
        self.BALLS.remove(ball)

    def drawArcs(self) -> None:
      for arc in self.ARCS:
            arc.rotate_arc()
            arc.create_arc_collision()
            arc.draw_arc()

    def drawBalls(self) -> None:
        for ball in self.BALLS:
            if(not ball.get_position().y < -300):
                # Draw the ball
                ball.draw_ball()

                # Caps velocity
                if(ball.get_velocity().length > 1000):
                    ball.set_velocity(0.99)
            else:
                # Off of screen so remove
                self.removeBall(ball)

    def addGUI(self, element) -> None:
        self.GUI_ELEMENTS.append(element)

    def removeGUI(self, element) -> None:
        self.GUI_ELEMENTS.remove(element)

    def drawGUI(self, screen) -> None:
        for element in self.GUI_ELEMENTS:
            element.draw(screen)