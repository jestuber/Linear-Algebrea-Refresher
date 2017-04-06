import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coord = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coord)

    def minus(self, v):
        new_coord = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coord)

    def times_scalar(self, c):
        new_coord = [c * x for x in self.coordinates]
        return Vector(new_coord)

    def magnitude(self):
        return sum([x**2 for x in self.coordinates])**0.5

    def norm(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1. / magnitude)
        except ZeroDivisionError:
            raise Exception("Zero Vector has no norm")

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle(self, v, in_degrees=False):
        try:
            norm_self = self.norm()
            norm_v = v.norm()
            angle = math.acos(norm_self.dot_product(norm_v))

            if in_degrees:
                return angle * 180. / math.pi
            else:
                return angle

        except ZeroDivisionError:
            raise Exception("Cannot find Angle with Zero Vector")


one = Vector([8.218, -9.341])
print one.plus(Vector([-1.129, 2.111]))

two = Vector([7.119, 8.215])
print two.minus(Vector([-8.223, 0.878]))

three = Vector([1.671, -1.012, -0.318])
print three.times_scalar(7.41)

print Vector([-0.221, 7.437]).magnitude()
print Vector([8.813, -1.331, -6.247]).magnitude()
print Vector([1.996, 3.108, -4.554]).norm()
print Vector([5.581, -2.136]).norm()

print Vector([7.887, 4.138]).dot_product(Vector([-8.802, 6.776]))
print Vector([-5.955, -4.904, -1.874]).dot_product(Vector([-4.496, -8.755, 7.103]))
print Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319]))
print Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985]),True)
