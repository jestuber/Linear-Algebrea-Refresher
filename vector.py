from math import pi, acos, sqrt
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

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
        new_coord = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coord)

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def norm(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0') / Decimal(magnitude))
        except Exception as e:
            raise e

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle(self, v, in_degrees=False):
        try:
            norm_self = self.norm()
            norm_v = v.norm()
            norms_dotted = norm_self.dot_product(norm_v)
            angle = acos(round(norms_dotted, 10))

            if in_degrees:
                return angle * 180. / pi
            else:
                return angle

        except ZeroDivisionError:
            raise Exception("Cannot find Angle with Zero Vector")

    def is_parallel(self, v):
        if self.is_zero() or v.is_zero():
            return True
        elif (self.angle(v) == 0) or (self.angle(v) == pi):
            return True
        else:
            return False

    def is_orthogonal(self, v, tol=1e-10):
        if abs(self.dot_product(v)) < tol:
            return True
        else:
            return False

    def is_zero(self, tol=1e-10):
        return self.magnitude() < tol

    def projection(self, b):
        try:
            return b.norm().times_scalar(v.dot_product(b.norm()))
        except Exception as e:
            raise e

    def perp(self, b):
        try:
            return self.minus(self.projection(b))
        except Exception as e:
            raise e


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

v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
print v.is_parallel(w)
print v.is_orthogonal(w)

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print v.is_parallel(w)
print v.is_orthogonal(w)

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print v.is_parallel(w)
print v.is_orthogonal(w)

v = Vector([2.118, 4.827])
w = Vector([0, 0])
print v.is_parallel(w)
print v.is_orthogonal(w)

v = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])
print v.projection(b)

v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print v.perp(b)

v = Vector([3.009, -6.172, 3.692, -2.51])
b = Vector([6.404, -9.144, 2.759, 8.718])
print v.projection(b)
print v.perp(b)
