from math import sin, cos, tan, radians, sqrt


class Cannon:
    
    def __init__(self, env_width, pos):
        self.width = width = int(env_width/10)
        self.pos = (x,y) = pos
        self.base = base = width, width/3
        self.barrel_radius = r = width/5
        self.barrel_len = l = width - r
        self.barrel_center_line = [(x + r, y + base[1] + r),
                                   (x + r + l/2, y + base[1] + r)]
        self.barrel_coords = [(x + r, y + base[1]),
                              (x + r + l, y + base[1]), 
                              (x + r + l, y + base[1] + r*2),
                              (x + r, y + base[1] + r*2)
                              ]
        self.barrel_angle = 0.0
        
    def aim(self, a):
        angle = self.barrel_angle + a
        if angle > 90.0:
            angle = 90.0
        elif angle < 0.0:
            angle = 0.0
        self.barrel_angle = angle
        a = radians(angle)
        
        (rx, ry) = self.barrel_center_line[0]
        h = self.barrel_len/2
        x = rx + (cos(a) * h)
        y = ry + (sin(a) * h)
        self.barrel_center_line[1] = (x, y)
        
        h = self.barrel_radius
        x1 = rx + (sin(a) * h)
        y1 = ry - (cos(a) * h)
        coord_0 = (x1,y1)
        
        h = self.barrel_len
        x2 = x1 + (cos(a) * h)
        y2 = y1 + (sin(a) * h)
        coord_1 = (x2, y2)
        
        h = self.barrel_radius*2
        x3 = x2 - (sin(a) * h)
        y3 = y2 + (cos(a) * h)
        coord_2 = (x3, y3)
        
        h = self.barrel_len
        x4 = x3 - (cos(a) *h)
        y4 = y3 - (sin(a) * h)
        coord_3 = (x4, y4)
        
        self.barrel_coords[0] = coord_0
        self.barrel_coords[1] = coord_1
        self.barrel_coords[2] = coord_2
        self.barrel_coords[3] = coord_3
        
        
        
        
        
        
        
        
        
        
