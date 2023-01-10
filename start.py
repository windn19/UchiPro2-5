class Point:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'Точка с координатой {self.x}'


my_point1 = Point(2)
my_point2 = Point(3)
my_point1 + my_point2
