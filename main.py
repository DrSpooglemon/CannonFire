from kivy.core.window import Window
Window.clearcolor = 1, 1, 1, 1
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import GameScreen
from environment import Environment
from cannon import Cannon
from utils import *

''' ----------------
BLOCK = [pos, size, friction, elasticity, density, color]

'''
concrete_color = (.5, .5, .5)
wood_color     = (.7, .5, .0)
floor_color    = (.0, 1., .2)
ball_color     = (.0, .0, .0)

u = Window.width/40

d = 22
cd = .3
wd = .1
bd = .6

LEVELS = [
    [
        [(u * (d + 0),   u * 2.5),  (u * 1,  u * 5), 0.7, 0.3, wd, (wood_color)],
        [(u * (d + 15),  u * 2.5),  (u * 1,  u * 5), 0.7, 0.3, wd, (wood_color)],
        [(u * (d + 7.5), u * 5.5),  (u * 16, u * 1), 0.9, 0.7, cd, (concrete_color)],
        [(u * (d + 2),   u * 8.5),  (u * 1,  u * 5), 0.7, 0.3, wd, (wood_color)],
        [(u * (d + 13),  u * 8.5),  (u * 1,  u * 5), 0.7, 0.3, wd, (wood_color)],
        [(u * (d + 7.5), u * 11.5), (u * 12, u * 1), 0.9, 0.7, cd, (concrete_color)],
        [(u * (d + 4),   u * 14.5), (u * 1,  u * 5), 0.7, 0.3, wd, (wood_color)],
        [(u * (d + 11),  u * 14.5), (u * 1,  u * 5), 0.7, 0.3, wd, (wood_color)],
        [(u * (d + 7.5), u * 17.5), (u * 8,  u * 1), 0.9, 0.7, cd, (concrete_color)]],
]
            

class CannonFireApp(App):

    screen_manager = ScreenManager()
    env = Environment()
    polies = []
    circles = []
    segments = []
    current_level = 1
    
    def build(self):
        print(str(self.env))
        self.main_screen = main = GameScreen(name='Main')
        self.screen_manager.add_widget(main)

        self.env.floor.line = self.main_screen.add_line(
            points_from_segment(self.env.floor), 
            self.env.floor.radius, 
            floor_color)
        self.segments.append(self.env.floor)
        self.cannon = c = Cannon(
            Window.width, (Window.width/50, self.env.floor_level))
        c.quad = self.main_screen.add_quad(
            points_from_cannon(c), wood_color)
        Window.bind(
            on_touch_down=self.on_touch_down,
            on_touch_up=self.on_touch_up,
            on_touch_move=self.on_touch_move)
        self.touch_pos = (0, 0)
        self.make_level(LEVELS[self.current_level-1])
        return self.screen_manager

    def make_level(self, blocks):
        for block in blocks:
            pos, size, friction, elasticity, density, color = block
            pos = (pos[0], pos[1] + self.env.floor_level)
            b = self.env.make_box(
                0, pos, size, friction, elasticity, density=density)
            b.quad = self.main_screen.add_quad(
                points_from_poly(b), color)
            self.polies.append(b)
        self.fired = False
        Clock.schedule_once(self.start, 1)

    def start(self, _):
        Clock.schedule_interval(self.step, .04)
    
    def step(self, dt):
        self.env.step(dt)
        update_polies(self.polies)
        update_circles(self.circles)
        update_segments(self.segments)
        update_cannon(self.cannon)

    def on_touch_down(self, _, touch):
        self.touch_pos = touch.pos
        self.timer = True
        def time_out():
            self.timer = False
        Clock.schedule_once(lambda dt: time_out(), 0.2)
        
    def on_touch_up(self, _, touch):
        if self.timer:
            if self.fired == False:
                self.fire()
                self.fired = True
                Clock.schedule_once(self.reload, 2)
        self.timer = False
        
    def on_touch_move(self, _, touch):
        if not self.timer:
            (x1, y1) = self.cannon.barrel_coords[1]
            self.cannon.aim((touch.pos[1] - self.touch_pos[1]))
        self.touch_pos = touch.pos
                
    def fire(self):
        pos = self.cannon.barrel_center_line[1]
        r = self.cannon.barrel_radius * 0.7
        ball = self.env.make_ball(0, pos, r, .1, 0.7, density=bd)
        ball.ellipse = self.main_screen.add_ellipse(
            xy_from_circle(ball), (ball.radius*2,)*2, ball_color)
        self.circles.append(ball)
        point = self.cannon.barrel_center_line[0]
        diff_x = pos[0] - point[0]
        diff_y = pos[1] - point[1]
        impulse_increment = ii = 10**3.8
        impulse = (diff_x * ii, diff_y * ii)
        ball.body.apply_impulse_at_world_point(impulse, point)

    def reload(self, _):
        self.fired = False

    
if __name__ == '__main__':  
    CannonFireApp().run()