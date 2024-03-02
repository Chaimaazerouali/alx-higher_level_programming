#!/usr/bin/python3
""" Write a Python script that print html status error """

import sys
from urllib import request, error
if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as rep:
            print(rep.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
