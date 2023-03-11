'''
Title: eto rossiya!!!
Group:
Popov I. 50%
Fedyakin D. 55%
Fisher D. 70%
'''

import turtle as turtle
import math

#turtle settings
screen = turtle.Screen()
screen.setup(800, 800)
screen.tracer(0, 0)
turtle.speed(0)
turtle.shape('turtle')


def triangle(x, y, sd_lngth_a, sd_lngth_b, sd_lngth_c, angle_a, angle_b, angle_main, fill_clr, brdr_clr,
             brdr_wdth):
    '''
    responsible person: Popov I.

    :param x: X coordinate
    :param y: Y coordinate
    :param sd_lngth_a: A side length
    :param sd_lngth_b: B side length
    :param sd_lngth_c: C side length
    :param angle_a: A angle
    :param angle_b: B angle
    :param angle_c: C angle
    :param angle_main: Triangle rotation angle
    :param fill_clr: Fill color
    :param brdr_clr: Border color
    :param brdr_wdth: Border width
    :return: None
    '''
    turtle.pu()

    turtle.color(brdr_clr, fill_clr)
    turtle.pensize(brdr_wdth)
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pd()

    turtle.rt(angle_main)

    turtle.fd(sd_lngth_b)
    turtle.rt(180 - angle_a)
    turtle.fd(sd_lngth_c)
    turtle.rt(180 - angle_b)
    turtle.fd(sd_lngth_a)

    turtle.end_fill()
    turtle.pu()
    turtle.home()


def ellipse(x, y, a, b, angle, fill_color, border_color, border_width):
    '''
    responsible person: Fisher D.

    :param x: X coordinate centre of ellipse
    :param y: Y coordinate centre of ellipse
    :param a: ellipse length
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

    :param x: X coordinate
    :param y: Y coordinate
    :param a: A side length
    :param b: B side length
    :param angle: The angle from which the figure starts to turn
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

def background():
    '''
    responsible person: Fedyakin D.
    field and sky
    :return: None
    '''

    rectangle(-400, 400, 800, 300, 0, 'lightskyblue', '', 0) #sky in the background
    rectangle(-400, 100, 800, 500, 0, 'olivedrab3', '', 0) #field in the background

def trees():
    '''
    responsible person: Fedyakin D.
    tree trunks and foliage
    :return: None
    '''

    #tree with apples
    rectangle(-220, 150, 15, 105, 0, 'brown', 'black', 2) #tree trunk
    ellipse(-215, 250, 100, 100, 0, 'chartreuse3', 'black', 2) #tree foliage
    ellipse(-270, 255, 20, 20, 0, 'red', 'black', 2) #first apple
    ellipse(-205, 210, 20, 20, 0, 'red', 'black', 2) #second apple
    ellipse(-160, 260, 20, 20, 0, 'red', 'black', 2) #third apple
    ellipse(-205, 300, 20, 20, 0, 'red', 'black', 2) #fourth apple

    #tree with dark green foliage
    rectangle(-305, 40, 30, 40, 0, 'brown', 'black', 3) #tree trunk
    triangle(-225, 40, 115, 130, 115, 55, 70, 180, 'dark green', 'black', 3) #tree foliage

    #two-level spruce
    rectangle(-60, 85, 20, 20, 0, 'brown', 'black', 1) #tree trunk
    triangle(-20, 85, 60, 60, 60, 60, 60, 180, 'olivedrab3', 'black', 2) #first spruce level
    triangle(-20, 138, 60, 60, 60, 60, 60, 180, 'olivedrab3', 'black', 2) #second spruce level

    #three-level spruce
    rectangle(300, 90, 20, 20, 0, 'brown', 'black', 1) #tree trunk
    triangle(340, 90, 60, 60, 60, 60, 60, 180, 'olivedrab3', 'black', 2) #first spruce level
    triangle(340, 143, 60, 60, 60, 60, 60, 180, 'olivedrab3', 'black', 2) #second spruce level
    triangle(340, 196, 60, 60, 60, 60, 60, 180, 'olivedrab3', 'black', 2) #third spruce level

def carrots():
    '''
    responsible person: Fedyakin D.
    carrots on field
    :return: None
    '''

    #first carrot
    triangle(-330, -250, 85, 44, 85, 75, 30, -60, 'limegreen', 'black', 1) #first carrot tops
    triangle(-265, -300, 135, 70, 135, 75, 30, -60, 'orangered', 'black', 1) #first carrot

    #second carrot
    triangle(240, -270, 85, 44, 85, 75, 30, 75, 'limegreen', 'black', 1) #second carrot tops
    triangle(160, -280, 135, 70, 135, 75, 30, 75, 'orangered', 'black', 1) #second carrot

    #third carrot
    triangle(180, -150, 85, 44, 85, 75, 30, 40, 'limegreen', 'black', 1) #third carrot tops
    triangle(120, -200, 135, 70, 135, 75, 30, 40, 'orangered', 'black', 1) #third carrot

def grass():
    '''
    responsible person: Fedyakin D.
    grass on field
    :return: None
    '''
    
    #grass
    triangle(-130, -250, 50, 18, 50, 80, 20, 180, 'palegreen4', 'black', 1)
    triangle(-50, -200, 50, 70, 50, 45, 90, 60, 'palegreen4', 'black', 1)
    triangle(-270, -180, 40, 40, 40, 60, 60, 180, 'palegreen4', 'black', 1)
    triangle(-220, -180, 60, 60, 60, 60, 60, 180, 'palegreen4', 'black', 1)
    triangle(300, -100, 20, 20, 20, 60, 60, 180, 'palegreen4', 'black', 1)
    triangle(327, -100, 40, 27, 40, 70, 40, 180, 'palegreen4', 'black', 1)

def head():
    '''
    responsible person: Fisher D.
    rabbit's head
    :return: None
    '''

    ellipse(70, 160, 35, 100, 23, "LightGrey", "black", 2)  # rabbit's left outer ear
    ellipse(80, 139, 28, 80, 23, "LightPink", "black", 2)  # rabbit's left inner ear

    ellipse(225, 175, 35, 100, -15, "LightGrey", "black", 2)  # rabbit's right outer ear
    ellipse(219, 152, 28, 80, -15, "LightPink", "black", 2)  # rabbit's right inner ear

    ellipse(159, 23, 95, 95, 0, "LightGrey", "black", 2)  # rabbit's head base

    ellipse(125, 19, 20, 30, 2, "white", "black", 2)  # rabbit's white of left eye
    ellipse(125, 15, 13, 13, 0, "blue4", "blue4", 2)  # rabbit's left iris
    ellipse(125, 15, 10, 10, 0, "black", "black", 2)  # rabbit's pupil of left eye

    ellipse(201, 21, 20, 30, 2, "white", "black", 2)  # rabbit's white of right eye
    ellipse(201, 17, 13, 13, 0, "blue4", "blue4", 2)  # rabbit's right iris
    ellipse(201, 17, 10, 10, 0, "black", "black", 2)  # rabbit's pupil of right eye

    ellipse(163, -33, 20, 20, 0, "white", "black", 1)  # rabbit's lip contour
    ellipse(163, -33, 17, 17, 0, "red", "black", 1)  # rabbit's mouth

    ellipse(163, -13, 54, 30, 2, "white", "black", 2)  # rabbit's nose base
    ellipse(163, -1, 18, 6, 2, "black", "black", 2)  # rabbit's nose

    rectangle(162, -1, 2, 30, 0, "black", "black", 1)  # rabbit's nose bridge

    # right side of the rabbit's whiskers
    ellipse(180, -16, 2, 2, 0, "black", "black", 1)
    ellipse(194, -10, 2, 2, 0, "black", "black", 1)
    ellipse(194, -22, 2, 2, 0, "black", "black", 1)

    # left side of the rabbit's whiskers
    ellipse(143, -16, 2, 2, 0, "black", "black", 1)
    ellipse(129, -10, 2, 2, 0, "black", "black", 1)
    ellipse(129, -22, 2, 2, 0, "black", "black", 1)


def body():
    '''
    responsible person: Popov I.
    rabit's body, legs, hands, tale
    :return: None
    '''

    # left hand
    ellipse(130, -140, 33, 23, 0, "LightGray", "black", 2)

    # body
    ellipse(20, -60, 150, 110, 10, "White", "black", 2)  
    ellipse(16, -33, 140, 82, 10, "LightGray", "black", 2)  

    # tale
    ellipse(-150, -45, 33, 33, 0, "White", "black", 2)

    # leg
    ellipse(-75, -155, 50, 20, 165, "LightGray", "black", 2)
    ellipse(-85, -85, 70, 70, 0, "LightGray", "black", 2)

    # right hand
    ellipse(70, -150, 38, 28, 0, "LightGray", "black", 2)



def main():
    '''
    Main function
    :return: None
    '''

    background()
    grass()
    carrots()
    trees()
    body()
    head()

    turtle.done()

if __name__ == '__main__':
    main()

