class Conic(object):
    """ The class that creates a Conic like the format::

            a x2 + 2 h x y + b y2 + 2 g x + 2 f y + c = 0

    Only `a`, `h` and `g` are needed. rest is optional. They are set to zero by default."""

    def __init__(self, a: float, h: float, b: float, f: float = 0, g: float = 0, c: float = 0) -> None:
        self.c = c
        self.g = g
        self.f = f
        self.a = a
        self.h = h
        self.b = b

    def __str__(self) -> str:
        return '{0.a} x2 + {1} x y + {0.b} y2 + {2} x + {3} y + {0.c} = 0'.format(self, 2 * self.h, 2 * self.g,
                                                                                  2 * self.f)

    @classmethod
    def from_str(cls, string: str, *, delimiter: str = ' ') -> object:
        """
        ```This method is used as an alternative constractor of Conic```

        :arg:
            string: in the format "a h b g f c". space in between.
            delimiter: takes the delimiter of the string. if not provided, defaults to ' '.

        :return: Returns an Object of the class ``Conic``.

        """
        args = string.split(delimiter)
        args = filter(lambda x: x is not '', args)
        try:
            args = map(lambda x: float(x), args)
            klass = cls(*args)

        except ValueError as exc:
            print('Error: ', exc)
            print('Please Check Your Input')
            raise

        return klass


class Line2D(object):
    """
    Class Straight Line that constracts a straight line in 2D
    """

    def __init__(self, m: float, c: float) -> None:
        self.c = c
        self.m = m

    @classmethod
    def from_intersection(cls, x: float, y: float) -> object:
        """
        Takes the x and y axis intercept and returns a Line2D object. It is used as an Alternative
        Constructor.

            Y / b + X / a = 1
        ->  Y / b = 1 - X/a
        ->  Y  =  b - (b / a) X


        :param x: the X axis intercept
        :param y: the Y axis intercept
        :return: returns a Line2D object
        """
        m = -y / x
        c = y

        return cls(m, c)

    def get_intersection(self):
        if self.c == 0:
            return 0, 0

        i_x = -self.m / self.c
        i_y = 1 / self.c

        return i_x, i_y

    def __mul__(self, other):
        a = self.m * other.m
        h = - self.m - other.m
        b = 1


if __name__ == '__main__':
    conic1 = Conic(1, 2, 1)
    conic2 = Conic.from_str("1 2 3")
    print(conic1)
    print(conic2)
