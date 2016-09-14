# -*-coding:Utf-8 -*

"""This module contains the class Point."""

class Point:

    """Defines a point in the map."""

    def __init__(self, x, y):
        """
            Constructor
            @param:
                - x: x coordinate
                - y: y coordinate
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
            Point representation
        """
        return str(self)

    def __str__(self):
        """
            Point as string
        """
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        """
            Defines point == other
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
            Defines point != other
        """
        return not self.__eq__(other)

    def get_x(self):
        """
            Getter (x)
            @return:
                - self.x
        """
        return self.x

    def get_y(self):
        """
            Getter (y)
            @return:
                - self.y
        """
        return self.y

    def set_x(self, x):
        """
            Setter (x)
            @param:
                - x: new x coordinate
        """
        self.x = x

    def set_y(self, y):
        """
            Setter (y)
            @param:
                - y: new y coordinate
        """
        self.y = y

if __name__ == "__main__":
    point = Point(1,1)
    print point
