from Presets import setup as sets
from Components import arc
from Components import ball

BALLS = []
ARCS = []
GUI_ELEMENTS = []

def addArcs(_space, _screen) -> None:
    arcSet = sets.loadArcSet()

    if len(ARCS) < arcSet["amount"]:
            new_arc = arc.Arc(
                position = arcSet["position"],
                friction = arcSet["friction"],
                elasticity = arcSet["elasticity"],
                radius = arcSet["radius"],
                width = arcSet["width"],
                color = arcSet["color"],
                segments = arcSet["segments"],
                rotation_speed = arcSet["rotation_speed"],
                start_angle = arcSet["start_angle"],
                end_angle = arcSet["end_angle"],
                space = _space,
                screen = _screen
            )

            # Makes the arcs not overlap
            if len(ARCS) >= 1:
                new_arc.set_radius(new_arc.get_radius() + 100)
                new_arc.randomize_rotation()
                arcSet["radius"] += 100
                
            ARCS.append(new_arc)

def addBalls(_space, _screen) -> None:
     ballSet = sets.loadBallSet()
     if len(BALLS) < ballSet["amount"]:
            new_ball = ball.Ball(
                mass = ballSet["mass"],
                moment = ballSet["moment"],
                position = ballSet["position"],
                friction = ballSet["friction"],
                elasticity = ballSet["elasticity"],
                radius = ballSet["radius"],
                width = ballSet["width"],
                color = ballSet["color"],
                space = _space,
                screen = _screen
            )
            new_ball.create_ball()
            BALLS.append(new_ball)

def drawArcs() -> None:
      for arc in ARCS:
            arc.rotate_arc()
            arc.create_arc_collision()
            arc.draw_arc()

def drawBalls() -> None:
      for ball in BALLS:
            if(not ball.get_position().y < -300):
                # Draw the ball
                ball.draw_ball()

                # Caps velocity
                if(ball.get_velocity().length > 1000):
                    ball.set_velocity(0.99)
            else:
                # Off of screen so remove
                ball.destroy_Ball()
                BALLS.remove(ball)

def addGUI(element) -> None:
    GUI_ELEMENTS.append(element)

def removeGUI(element) -> None:
    GUI_ELEMENTS.remove(element)

def drawGUI(screen) -> None:
     for element in GUI_ELEMENTS:
          element.draw(screen)