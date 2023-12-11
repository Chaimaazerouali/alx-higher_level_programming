#!/usr/bin/python3
""" Module for Square class. """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square clase """

    def __init__(self, size, x=0, y=0, id=None):
        """ init with arguments and __init__ from Rectangle """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns string info about this square. """
        id_str = str(self.id)
        w_str = str(self.width)
        x_str = str(self.x)
        y_str = str(self.y)
        div_str = x_str + '/' + y_str + ' - ' + w_str
        return ("[Square] " + '(' + id_str + ') ' + div_str)

    def update(self, *args, **kwargs):
        """ update id, width, height, x and y, this order """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[1] if len(args) >= 2 else self.height
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
