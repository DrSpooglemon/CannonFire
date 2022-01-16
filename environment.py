from pymunk import *

class Environment(Space):

    def __init__(self, gravity=900, slt=.5):
        super().__init__()
        self.rectangles = []
        self.gravity = (0, -gravity)
        self.sleep_time_threshold = slt
        self.floor = Segment(self.static_body, (-100, 0), (1000, 0), 10)
        self.floor_level = 10
        self.floor.friction = .7
        self.floor.elasticity = .1
        self.add(self.floor)
        
    def __str__(self):
        lines = ["* * * * * * * * * * * * * * * * * *",
                 "* This is a Pymunk environment!   *",
                 f"* The gravity is {-self.gravity[1]}.           *",
                 "*                                 *",
                 "* Thank you...                    *",
                 "* * * * * * * * * * * * * * * * * *",
                 ]
        return '\n'.join(lines)

    def step(self, dt):
        for x in range(12):
            super().step(dt/12)
    
    def make_ball(self, mass, pos, radius, friction, elasticity, density=None):
        if density:
            body = Body()
            shape = Circle(body, radius)
            shape.density = density
        else:
            moment = moment_for_circle(mass, radius*0.99, radius)
            body = Body(mass, moment)
            shape = Circle(body, radius)
        shape.friction = friction
        shape.elasticity = elasticity
        body.position = Vec2d(*pos)
        self.add(body, shape)
        return shape
    
    def make_box(self, mass, pos, size, friction, elasticity, density=None):
        if density:
            body = Body()
            shape = Poly.create_box(body, size)
            shape.density = density
        else:
            moment = moment_for_box(mass, size)
            body = Body(mass, moment)
            shape = Poly.create_box(body, size)
        shape.friction = friction
        shape.elasticity = elasticity
        body.position = pos
        self.add(body, shape)
        return shape
        
    def get_circle_edge(self, circle):
        return circle.body.position + Vec2d(circle.radius, 0).rotated(circle.body.angle)