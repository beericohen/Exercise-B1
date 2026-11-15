class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __add__(left, right):
        return (left.get_area() + right.get_area())


class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x,x)


if __name__ == "__main__":
    s = Square(5)
    r = Rectangle(8, 2)

    print(f"square area = {s.get_area()}")
    print(f"rectangle area = {r.get_area()}")

    print(f"aggregated area is: {s+r}")
