######################################################################
# Author: Dimitrios Ntentia, Nelson Xunic Cua      TODO: Change this to your names
# Username: ntentiad, xuniccuan                       TODO: Change this to your usernames
#
# Assignment: T11: Intro to Classes
#
# Purpose:  Demonstrates a Point class and a related main() to create objects
######################################################################
# Acknowledgements:
#
# Based on the point class from our textbook: http://cs.berea.edu/courses/csc226book/classes_and_objects_I.html

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import math
import turtle       # needed by both point class and main()
import random       # needed by main()
from math import *

class Point:
    """
    The Point class represents and manipulates x,y coordinates.
    It is dependent upon the turtle libraries for draw_point() method.
    In particular, a Screen must exist and the color mode should be set to 255
    """

    def __init__(self, x=0, y=0):       # Each Point object has its own x and y coordinates and possibly a turtle
        """
        Initializer method a.k.a. Constructor:
        Creates a new point at x, y. If no x, y are given, the point is created at 0, 0

        :param x: the x coordinate of the point
        :param y: the y coordinate of the point
        """
        self.x = x
        self.y = y
        self.turtley = None

    def __str__(self):
        """
        Makes the str() function work with Points

        :return: A formatted string for better printing
        """
        return "({0}, {1})".format(self.x, self.y)

    def distance_from_origin(self):
        """
        Compute my distance from the origin

        :return: float representing distance from (0, 0)
        """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def user_set(self):
        """
        Allows the user to change the x and y value of a Point

        :return: None
        """
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))

    def draw_point(self, r=0, g=0, b=0, text=""):         # black is the default color
        """
        Instantiates a Turtle object and draws the Point on the Screen

        :param r: the red channel
        :param g: the green channel
        :param b: the blue channel
        :param text: any additional text to stamp
        :return: None
        """
        if not self.turtley:
            self.turtley = turtle.Turtle()
            self.turtley.hideturtle()
        self.turtley.color(r, g, b)
        self.turtley.penup()
        self.turtley.goto(self.x, self.y)
        self.turtley.showturtle()
        self.turtley.stamp()

        # This code was added from the original point.py class
        # to allow custom text to be written to the screen
        self.turtley.penup()
        if text == "":
            self.turtley.write(str(self), True)
        else:
            self.turtley.write(text, True)
        self.turtley.hideturtle()

    def draw_middle_point(self,valuex,valuey):
        """
        Compute the distance of the two inputs and then draws that value into the windows

        :return:
        """
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))

        mdpointx=math.sqrt((self.x*self.x)-(valuex*valuex))
        mdpointy=math.sqrt((self.y*self.y)-(valuey*valuey))
        tuple=(mdpointx,mdpointy)
        return tuple

# end class


def main():
    """
    A program that demonstrates the use of the Point class

    :return: None
    """
    wn = turtle.Screen()
    wn.colormode(255)        # change color modes

    p = Point()              # Instantiate an object of type Point at (0, 0)
    k=Point()


    print("point = " + str(p))

    q = Point(30, 40)        # Make a second point at (30, 40)
    print("point = " + str(q))

    p.draw_point()           # draw Point p as the default color of black
    q.draw_point(255, 0, 0)  # draw Point q as red (255, 0, 0)

    print("\nPlease enter x and y values. To end, enter x = 0 and y = 0.")
    while q.x != 0 or q.y != 0:
        q.user_set()
        testing=k.draw_middle_point(q.x,q.y)

        print("point = " + str(q))
        q.draw_point(random.randrange(256), random.randrange(256), random.randrange(256))  # Random color
        k.draw_point(random.randrange(256), random.randrange(256), random.randrange(256))
        why=Point(testing[0],testing[1])
        why.draw_point(random.randrange(256), random.randrange(256), random.randrange(256))

    print("Exiting. Bye!")

    wn.bye()

# end main


if __name__ == "__main__":
    main()
