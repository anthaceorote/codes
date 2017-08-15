import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_pt):
        new_x = self.x + other_pt.x
        new_y = self.y + other_pt.y
        return Point(new_x, new_y)

    def __truediv__(self, divider):
        new_x = self.x / divider
        new_y = self.y / divider
        return Point(new_x, new_y)

    def __str__(self):
        return '(%r, %r)' % (self.x, self.y)

    def __getitem__(self, key):
        key_map = {0: self.x, 1: self.y}
        if key not in key_map:
            raise IndexError
        return key_map[key]

    @staticmethod
    def mid_pt(pt1, pt2):
        new_pt = pt1 + pt2
        return new_pt / 2


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def mid_point(p1, p2):
    return ((p1 + p2) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree - 1], myTurtle)
    if degree > 0:
        sierpinski([points[0], mid_point(points[0], points[1]), mid_point(points[0], points[2])], degree - 1, myTurtle)
        sierpinski([points[1], mid_point(points[0], points[1]), mid_point(points[1], points[2])], degree - 1, myTurtle)
        sierpinski([points[2], mid_point(points[2], points[1]), mid_point(points[0], points[2])], degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [Point(-100, -50), Point(0, 100), Point(100, -50)]
    sierpinski(myPoints, 3, myTurtle)

if __name__ == '__main__':
    main()
