#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv


class Base:
    '''A representation of the base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ print with turtle list of rectangles and squares """
        turtles1 = []
        turtles2 = []
        turtles3 = []
        turtles4 = []

        for i in range(len(list_rectangles) + len(list_squares) * 8):
            turtles1.append(turtle.Turtle())
            turtles2.append(turtle.Turtle())
            turtles3.append(turtle.Turtle())
            turtles4.append(turtle.Turtle())
        pos_x = 0
        pos_y = 0
        i = 0
        x_plan = 0
        y_plan = 0
        for obj in list_rectangles:
            i += 1
            dic = obj.to_dictionary()
            print(dic)
            w = dic['width']
            h = dic['height']
            x = dic['x']
            y = dic['y']
            plan_x = w + x + pos_x
            plan_y = h + y + pos_y
            max_x = max(plan_x, plan_y) + 20
            max_y = -max(plan_x, plan_y) - 20
            turtle.setworldcoordinates(-30, 30, max_x, max_y)
            turtles1[i].penup()
            turtles1[i].goto(pos_x, 0)
            turtles1[i].pendown()
            turtles1[i].forward(w + x + 10)
            turtles1[i].write(w)

            turtles2[i].penup()
            turtles2[i].goto(pos_x, 0)
            turtles2[i].pendown()
            turtles2[i].right(90)
            turtles2[i].forward(h + y + 10)
            turtles2[i].write(h)
            i += i

            turtles1[0].speed(1)
            turtles1[0].color('red')
            turtles1[0].pensize(1)

            turtles1[0].goto(pos_x, 0)
            turtles1[0].pendown()
            turtles1[0].goto(pos_x + x, -y)
            turtles1[0].begin_fill()
            turtles1[0].color('blue')
            turtles1[0].pensize(5)
            turtles1[0].forward(w)
            turtles1[0].right(90)
            turtles1[0].forward(h)
            turtles1[0].right(90)
            turtles1[0].forward(w)
            turtles1[0].right(90)
            turtles1[0].forward(h)
            turtles1[0].right(90)
            turtles1[0].end_fill()
            turtles1[0].penup()
            pos_x += w + 80

        old_plan_x = plan_x
        old_plan_y = plan_y
        pos_y += -150 - h
        pos_x = 0
        i = 0

        for obj in list_squares:
            i += 1
            dic = obj.to_dictionary()
            print(dic)
            s = dic['size']
            x = dic['x']
            y = dic['y']

            plan_x = s + x + pos_x + old_plan_x + 50
            plan_y = s + y + pos_y + old_plan_y + 50
            max_x = max(plan_x, plan_y) + 20

            turtles3[i].penup()
            turtles3[i].goto(pos_x, pos_y)
            turtles3[i].pendown()
            turtles3[i].forward(x + s + 10)
            turtles3[i].write(s)

            turtles4[i].penup()
            turtles4[i].goto(pos_x, pos_y)
            turtles4[i].pendown()
            turtles4[i].right(90)
            turtles4[i].forward(y + s + 10)
            turtles4[i].write(s)
            i += i

            turtles1[0].speed(1)
            turtles1[0].color('red')
            turtles1[0].pensize(1)

            turtles1[0].goto(pos_x, pos_y)

            turtles1[0].pendown()
            turtles1[0].goto(pos_x + x, pos_y - y)
            turtles1[0].begin_fill()
            turtles1[0].color('green')
            turtles1[0].pensize(5)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].forward(s)
            turtles1[0].right(90)
            turtles1[0].end_fill()
            turtles1[0].penup()
            pos_x += s + 80
            turtle.setworldcoordinates(-30, 30, max_x, -max_x)
        turtle.Screen().exitonclick()
