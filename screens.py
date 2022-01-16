from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button 
from kivy.graphics import *
from kivy.core.window import Window

            
# class StartScreen(Screen):
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         button_size = Window.width/10
#         self.add_widget(
#             Button(text='Start Game!',
#                    size_hint=(None,None),
#                    size=(button_size,button_size),
#                    pos=((Window.width/2) - (button_size/2),
#                         (Window.height/2) - (button_size/2)),
#                    on_press=self.app.start))
                    
        
class GameScreen(Screen):
    
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def add_quad(self, points, color):
        with self.canvas.after:
            Color(*color)
            return Quad(points=points)

    def add_ellipse(self, pos, size, color):
        with self.canvas:
            Color(*color)
            return Ellipse(pos=pos, size=size)

    def add_line(self, points, radius, color):
        with self.canvas:
            Color(*color)
            return Line(
                points=points, 
                width=radius)