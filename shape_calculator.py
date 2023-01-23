import math
class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50: return "Too big for picture."
    returnStr = f'{"*"*self.width}\n'
    returnStr = returnStr * self.height
    return returnStr

  def get_amount_inside(self, shape):
    vertical = math.floor(self.height/shape.height)
    horizontal = math.floor(self.width/shape.width)
    if vertical < 0 or horizontal< 0 : return 0
    return vertical * horizontal if vertical * horizontal > 0 else 0

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.width = height
    self.height = height

  ...
