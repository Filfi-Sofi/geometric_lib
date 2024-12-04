from math import pi


def calc(fig, func, size):
    if func == 'area':
        if fig == 'circle':
            if len(size) == 1 and size[0] > 0:
                return pi * size[0] ** 2
            else:
                raise AssertionError("Invalid parameters for circle area")

        elif fig == 'square':
            if len(size) == 1 and size[0] > 0:
                return size[0] ** 2
            else:
                raise AssertionError("Invalid parameters for square area")

        elif fig == 'triangle':
            if len(size) == 3 and all(s > 0 for s in size):
                a, b, c = size
                if a + b > c and a + c > b and b + c > a:
                    s = (a + b + c) / 2
                    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
                else:
                    raise AssertionError("Invalid triangle sides")
            else:
                raise AssertionError("Invalid parameters for triangle area")

        else:
            raise AssertionError("Unknown figure for area calculation")

    elif func == 'perimeter':
        if fig == 'circle':
            if len(size) == 1 and size[0] > 0:
                return 2 * pi * size[0]
            else:
                raise AssertionError("Invalid parameters for circle perimeter")

        elif fig == 'square':
            if len(size) == 1 and size[0] > 0:
                return 4 * size[0]
            else:
                raise AssertionError("Invalid parameters for square perimeter")

        elif fig == 'triangle':
            if len(size) == 3 and all(s > 0 for s in size):
                return sum(size)
            else:
                raise AssertionError("Invalid parameters for triangle perimeter")

        else:
            raise AssertionError("Unknown figure for perimeter calculation")

    else:
        raise AssertionError("Unknown function")
