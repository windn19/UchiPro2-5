class Circle:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R

    def __str__(self):
        return f'Окружность с центром в точке ({self.x}, {self.y}) и радиусом {self.R}'


x, y, R = map(int, input().split())
circle = Circle(x, y, R)
print(circle)
