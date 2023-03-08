
'''
Title: eto rossiya!!!
Group:
Popov I.
Fedyakin D.
Fisher D.
'''
from turtle import *
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

    :param x: X start coordinate
    :param y: Y start coordinate
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
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    '''
    turtle.rt(angle)
    turtle.circle(a, 45)
    turtle.circle(b, 90)
    turtle.circle(a, 90)
    turtle.circle(b, 90)
    turtle.circle(a, 45)
    turtle.lt(angle)
    '''
    import math

    turtle.rt(angle)
    turtle.color(border_color, fill_color)
    turtle.pensize(border_width)

    for degree in range(361):
        rad = math.radians(degree)
        dx = a * math.sin(rad) + x
        dy = -b * math.cos(rad) + b + y
        turtle.goto(dx, dy)

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
    pu()
    setx(x)
    sety(y)
    pd()
    rt(angle)
    pensize(border_width)
    color(border_color, fill_color)
    begin_fill()
    for i in range(2):
        fd(a)
        rt(90)
        fd(b)
        rt(90)
    end_fill()

def main():
    '''
    Main function
    :return: None
    '''

    '''
    rectangle(-400, 400, 800, 300, 0, 'lightskyblue', '', 0)
    rectangle(-400, 100, 800, 500, 0, 'olivedrab3', '', 0)
    rectangle(-300, 50, 30, 40, 0, 'brown', 'black', 3)
    rectangle(-220, 150, 15, 105, 0, 'brown', 'black', 2)
    rectangle(-60, 85, 20, 20, 0, 'brown', 'black', 1)
    rectangle(300, 90, 20, 20, 0, 'brown', 'black', 1)
    done()
    '''

if __name__ == '__main__':
    main()
