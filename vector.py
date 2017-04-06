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


one = Vector([8.218, -9.341])
print one.plus(Vector([-1.129, 2.111]))

two = Vector([7.119, 8.215])
print two.minus(Vector([-8.223, 0.878]))

three = Vector([1.671, -1.012, -0.318])
print three.times_scalar(7.41)
