from Presets import loaders as sets
from Components import arc
from Components import ball
from Core import app

class ObjectManager():
    def __init__(self, space) -> None:
        self.space = space
        self.BALLSET = {}
        self.ARCSET = {}
        self.BALLS = []
        self.ARCS = []
        self.GUI_ELEMENTS = []
        self.run_BallPhysics = True
        self.run_ArcPhysics = True
    
    def step(self) -> None:
        if self.run_BallPhysics:
            dt = 1.0 / 60.0
            for x in range(1):
                self.space.step(dt)

    def deLoadSet(self) -> None:
        app.runningSimulation = False
        self.ARCSET = {}
        self.BALLSET = {}
        for ball in self.BALLS[:]:
            self.removeBall(ball)
        for arc in self.ARCS[:]:
            self.removeArc(arc)

    def loadSets(self, fileName) -> None:
        self.run_BallPhysics = False
        self.deLoadSet()
        self.ARCSET = sets.loadArcSet(fileName)
        self.BALLSET = sets.loadBallSet(fileName)
        self.run_BallPhysics = True
        app.runningSimulation = True
        print("LOADED SET: " + fileName)

    def addArcs(self, _space, _screen) -> None:
        if self.ARCSET != {}:
            arcCountOffset = -1
            while len(self.ARCS) < self.ARCSET["amount"]:
                    arcCountOffset += 1
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
                        new_arc.set_radius(new_arc.get_radius() + self.ARCSET["offset"]*arcCountOffset)
                        new_arc.randomize_rotation()

                    self.ARCS.append(new_arc)

    def addBalls(self, _space, _screen) -> None:
        if self.BALLSET != {}:
            while len(self.BALLS) < self.BALLSET["amount"]:
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

    def removeArc(self, arc) -> None:
        for segment in arc.segment_shapes:
                self.space.remove(segment)
        self.ARCS.remove(arc)

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