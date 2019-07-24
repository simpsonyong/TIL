""" 아래와같은클래스Circle이있을때,반지름이3이고
x, y좌표가(2,4)인원을만들어넓이와둘레를출력하시오. """


class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return Circle.pi * self.r**2

    def circumference(self):
        return 2 * Circle.pi * self.r

    def center(self):
        return (self.x, self.y)

test = Circle(3, 2, 4)
print(test.area())
print(test.circumference())
