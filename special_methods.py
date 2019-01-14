from math import hypot

class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Vector(%r, %r)" % (self.x, self.y)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __abs__(self):
		return hypot(self.x, self.y)

	def __bool_(self):
		return bool(abs(self))

	def __mul__(self, scalar):
		x = self.x * scalar
		y = self.y * scalar
		return Vector(x, y)


vec = Vector(4, 3)
print("abs: %f" % abs(vec))

print("add: %r" % (vec + vec))

print("bool: %r" % bool(vec))

print("mul: %r" % (vec * 4))
