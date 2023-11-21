#!/usr/bin/python3
def magic_calculation(a, b):
    rl = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            rl += a ** b / i
        except Exception:
            rl = b + a
            break
    return (rl)
