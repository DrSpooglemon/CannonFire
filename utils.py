def points_from_poly(poly):
    b = poly.body
    def f():
        for v in poly.get_vertices():
            v = v.rotated(b.angle) + b.position
            for p in (v.x, v.y):
                yield p
    return list(f())

def xy_from_circle(circle):
    r = circle.radius
    return circle.body.position - (r, r)

def points_from_segment(segment):
    b = segment.body
    p1 = b.position + segment.a.cpvrotate(b.rotation_vector)
    p2 = b.position + segment.b.cpvrotate(b.rotation_vector)
    return [p1.x, p1.y, p2.x, p2.y]

def points_from_cannon(cannon):
    def f():
        for c in cannon.barrel_coords:
            for p in c:
                yield p
    return list(f())   

def update_polies(polies):
    for p in polies:
        p.quad.points = points_from_poly(p)

def update_circles(circles):
    for c in circles:
        c.ellipse.pos = xy_from_circle(c)

def update_segments(segments):
    for s in segments:
        s.line.points = points_from_segment(s)

def update_cannon(cannon):
    cannon.quad.points = points_from_cannon(cannon)