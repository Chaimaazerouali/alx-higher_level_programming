#!/usr/bin/python3
""" module contains class Base """


import json import dumps, load
import csv
import turtle


class Base():
    """ A representation of the base of our OOP hierarchy. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization base class with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Jsonifies a dictionary so it's quite rightly and longer. """
        if type(list_dictionaries) != list and list_dictionaries is not None:
            raise TypeError
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for dic in list_dictionaries:
            if type(dic) != dict:
                raise TypeError
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves jsonified object to file. """
        if list_objs:
            lis = [obj.to_dictionary() for obj in list_objs]
            json_obj = cls.to_json_string(lis)
        else:
            json_obj = "[]"
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        """ Unjsonifies a dictionary. """
        if type(json_string) != str and json_string is not None:
            raise TypeError
        if json_string is None or json_string == "[]" or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Loads instance from dictionary. """
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
        """ Loads string from file and unjsonifies."""
        obj_list = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                json_str = f.read()
        except:
            json_str = '[]'
        lis = cls.from_json_string(json_str)
        if lis:
            for dic in lis:
                obj_list.append(cls.create(**dic))
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves object to csv file."""
        if type(list_objs) != list:
            raise TypeError
        for obj in list_objs:
            if not isinstance(obj, cls):
                raise TypeError
        lis = [obj.to_dictionary() for obj in list_objs]
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            field_names = ['id', 'size', 'x', 'y']
        with open(file_name, mode="w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            for dic in lis:
                writer.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        """ Loads object to csv file. """
        obj_list = []
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field_names = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            field_names = ['id', 'size', 'x', 'y']
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f, fieldnames=field_names)
                for row in reader:
                    dic = {}
                    for key, value in dict(row).items():
                        dic[key] = int(value)
                    obj_list.append(cls.create(**dic))
        except:
            return []
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
