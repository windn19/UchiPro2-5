class Polygon:
   def __init__(self, sides):
       self.sides = sides

   def __len__(self):
       return len(self.sides)


sides = list(map(int, input().split()))
print(sides)
polygon = Polygon(sides)
print(len(polygon))