######################################################################
# Author: Dimitrios Ntentia, Nelson Xunic Cua     TODO: Change this to your names
# Username: ntentiad, xuniccuan                     TODO: Change this to your usernames
#
# Assignment: T11: Intro to Classes
#
#
# Purpose: A class for creating a shape
import random
import turtle

import t11_shape as Shape
from t11_point import Point

def main():
    """Draws 4 randomly placed, randomly sized, random shapes using the turtle library.

    return: None"""
    a_turtle=turtle.Turtle()
    wn = turtle.Screen()
    for i in range(4):
        usersides=int(random.randrange(3,10))
        userlength=int(random.randrange(50,200))
        p = Point(random.randrange(100),random.randrange(100))
        object_shape=Shape.shape(p,usersides,userlength,a_turtle)
        object_shape.draw_shape()
    wn.exitonclick()



if __name__ == "__main__":
    main()