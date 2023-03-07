'''
Title: eto rossiya!!!
Group:
Popov I.
Fedyakin D.
Fisher D.
'''

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
    import turtle
    import math

    turtle.rt(angle)
    turtle.color(border_color, fill_color)
    turtle.pensize(border_width)
    for degree in range(361):
        rad = math.radians(degree)
        x = a * math.sin(rad) + x
        y = -b * math.cos(rad) + b + y
        turtle.goto(x, y)

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
    pass

def main():
    '''
    Main function
    :return: None
    '''

if __name__ == '__main__':
    main()

ellipse(0,0,50,100,45,"green","yellow",5)