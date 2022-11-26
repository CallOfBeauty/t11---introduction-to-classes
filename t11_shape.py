######################################################################
# Author: Dimitrios Ntentia, Nelson Xunic Cua     TODO: Change this to your names
# Username: ntentiad, xuniccuan                     TODO: Change this to your usernames
#
# Assignment: T11: Intro to Classes
#
#
# Purpose: A class for creating a shape
import turtle

class shape:
    """A class to manufacture any shape objects"""
    def __init__(self,start_point, num_sides,side_length,turtle):
        """Initialize the shape at the startpoint, with number of sides, num_sides and length, side_length using the turtle
        object

        :param start_point: The point where the turtle starts
        :param num_sides: the number of sides of the shape
        :param side_length: the length of the sides of the shape
        :param turtle: the name of the turtle object"""
        self.start_point=start_point
        self.num_sides=num_sides
        self.side_length=side_length
        self.turtle=turtle

    def draw_shape(self):
        """using a turtle, draws the shape on the screen, at a certain position

        return: None"""
        self.turtle.penup()
        self.turtle.goto(self.start_point.x,self.start_point.y)
        self.turtle.pendown()
        for i in range(self.num_sides):
            self.turtle.forward(self.side_length)
            self.turtle.left(180-180*(self.num_sides-2)/self.num_sides)


