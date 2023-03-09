'''
Title: eto rossiya!!!
Group:
Popov I.
Fedyakin D.
Fisher D.
'''
import turtle as turtle
import math
screen = turtle.Screen()
screen.setup(800, 800)
screen.tracer(0,0)
turtle.speed(0)

def triangle(x, y, a, b, angle, fill_color, border_color, border_width):
    '''
    responsible person: Popov I.

    :param x:
    :param y:
    :param a:
    :param b:
    :param angle:
    :param fill_color: Fill color
    :param border_color: Border color
    :border_width: Border width
    :return: None
    '''
    pass

def ellipse(x, y, a, b, angle, fill_color, border_color, border_width):
    '''
    responsible person: Fisher D.

    :param x: X coordinate centre of ellipse
    :param y: Y coordinate centre of ellipse
    :param a: ellipse lenght
    :param b: ellipse width
    :param angle: angle of inclination
    :param fill_color: Fill color
    :param border_color: Border color
    :border_width: Border width
    :return: None
    '''

    turtle.color(border_color, fill_color)
    turtle.begin_fill()
    turtle.pensize(border_width)

    n = 10000
    t = 0
    dx = x + a * math.cos(t) * math.cos(math.radians(angle)) - b * math.sin(t) * math.sin(math.radians(angle))
    dy = y + a * math.cos(t) * math.sin(math.radians(angle)) + b * math.sin(t) * math.cos(math.radians(angle))
    turtle.up()
    turtle.goto(dx, dy)
    turtle.down()

    for i in range(n):
        dx = x + a * math.cos(t) * math.cos(math.radians(angle)) - b * math.sin(t) * math.sin(math.radians(angle))
        dy = y + a * math.cos(t) * math.sin(math.radians(angle)) + b * math.sin(t) * math.cos(math.radians(angle))
        turtle.goto(dx, dy)
        t += 2 * math.pi / n

    turtle.end_fill()



def rectangle(x, y, a, b, angle, fill_color, border_color, border_width):
    '''
    responsible person: Fedyakin D.

    :param x:
    :param y:
    :param a:
    :param b:
    :param angle:
    :param fill_color: Fill color
    :param border_color: Border color
    :border_width: Border width
    :return: None

    '''
    turtle.pu()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.rt(angle)
    turtle.pensize(border_width)
    turtle.color(border_color, fill_color)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(a)
        turtle.rt(90)
        turtle.fd(b)
        turtle.rt(90)
    turtle.end_fill()
def main():
    '''
    Main function
    :return: None
    '''

    rectangle(-400, 400, 800, 300, 0, 'lightskyblue', '', 0)
    rectangle(-400, 100, 800, 500, 0, 'olivedrab3', '', 0)
    rectangle(-300, 50, 30, 40, 0, 'brown', 'black', 3)
    rectangle(-220, 150, 15, 105, 0, 'brown', 'black', 2)
    rectangle(-60, 85, 20, 20, 0, 'brown', 'black', 1)
    rectangle(300, 90, 20, 20, 0, 'brown', 'black', 1)
    ellipse(-215,250,100,100,0,'chartreuse3','black',2)
    ellipse(-270,255,20,20,0,'red','black',2)
    ellipse(-205,210,20,20,0,'red','black',2)
    ellipse(-160,260,20,20,0,'red','black',2)
    ellipse(-205,300,20,20,0,'red','black',2)
    turtle.done()

if __name__ == '__main__':
    main()

