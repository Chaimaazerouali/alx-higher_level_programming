#!/usr/bin/python3
"""
Defines MyList, a class inheriting from list, with a print_sorted() method.
"""
class MyList(list):
    """MyList inherits from list."""
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

