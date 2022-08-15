from math import pi


class rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b


class square(rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class triangle(rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        area = super().area() / 2
        return area


class circle(square):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        area = super().area() * pi
        return area


class ngon(triangle):
    def __init__(self, radius, side, n):
        super().__init__(side, radius)
        self.n = n

    def area(self):
        area = super().area() * self.n
        return area


def select_shape():
    shape = input("Select shape by write first letter of it."
                  "You can chose rectangle, square, trinagle, circle or ngon.")
    return shape


def area(shape):
    if shape == "r" or shape == "R":
        area = rectangle(int(input("Insert length of side a.")), int(input("Insert length of side b."))).area()
    elif shape == "s" or shape == "S":
        area = square(int(input("Insert length of side a."))).area()
    elif shape == "c" or shape == "C":
        area = circle(int(input("Insert length of side radius."))).area()
    elif shape == "t" or shape == "T":
        area = triangle(int(input("Insert length of side base.")), int(input("Insert length of side height."))).area()
    elif shape == "n" or shape == "N":
        area = ngon(int(input("Insert length of side base.")), int(input("Insert length of side height.")),
                    int(input("Insert number of sides."))).area()
    return area


def main():
    shape = select_shape()
    area_ = area(shape)
    print(f"Area of selected shape is {area_}")


main()