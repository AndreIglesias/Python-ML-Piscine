

class Vector:
    def __init__(self, vec):
        """By default, the vectors are generated as classical column vectors if initialized with a
size or range."""
        self.values = None
        self.shape = None
        self.__valid_vec(vec)
        if type(vec) == list:
            self.values = vec
            if len(vec) == 1:
                self.shape = (1, len(vec[0]))
            else:
                self.shape = (len(vec), 1)
        elif type(vec) == int:
            self.values = [[float(x)] for x in range(vec)]
            self.shape = (len(self.values), 1)
        elif type(vec) == tuple:
            self.values = [[float(x)] for x in range(vec[0], vec[1])]
            self.shape = (len(self.values), 1)

    def __valid_vec(self, vec):
        assert type(vec) in {list, int, tuple}, 'Invalid type of vector'
        if type(vec) == list:
            assert len(vec) > 0, 'Non identifiable shape'
            for elem in vec:
                assert type(elem) == list, 'Invalid type of vector list: ' + str(elem)
                for f in elem:
                    assert type(f) == float or type(f) == int, 'Invalid type of element: ' + str(f)
            if len(vec) > 1:
                for elem in vec:
                    assert len(elem) == 1, 'Too many elements for a column vector: ' + str(vec)
        elif type(vec) == tuple:
            assert len(vec) == 2, 'Range must have two limits'
            for i in vec:
                assert type(i) == int, "Limit's type must be integer but is " + str(type(i))
            assert vec[0] <= vec[1], 'Invalid limits '
        elif type(vec) == int:
            assert vec >= 0, 'Invalid size of vector'

    def T(self):
        new = []
        if len(self.values) == 1:
            for elem in self.values[0]:
                new.append([elem])
            return Vector(new)
        else:
            new.append([])
            for elem in self.values:
                new[0].append(elem[0])
            return Vector(new)

    def dot(self, other):
        assert isinstance(other, Vector), 'Invalid dot product with ' + str(type(other))
        assert self.shape == other.shape, 'Incompatible vector shapes'
        if self.shape[0] == 1:
            new = [self.values[0][x] * other.values[0][x] for x in range(len(self.values[0]))]
            return sum(new)
        else:
            new = [self.values[x][0] * other.values[x][0] for x in range(len(self.values))]
            return sum(new)

    def __add__(self, other):
        assert isinstance(other, Vector), 'Invalid vector operation with ' + str(type(other))
        assert self.shape == other.shape, 'Incompatible vector shapes'
        if self.shape[0] == 1:
            new = [[self.values[0][x] + other.values[0][x] for x in range(len(self.values[0]))]]
            return Vector(new)
        else:
            new = [[self.values[x][0] + other.values[x][0]] for x in range(len(self.values))]
            return Vector(new)

    def __radd__(self, other):
        assert isinstance(other, Vector), 'Invalid vector operation with ' + str(type(other))
        return other.__add__(self)

    def __sub__(self, other):
        assert isinstance(other, Vector), 'Invalid vector operation with ' + str(type(other))
        assert self.shape == other.shape, 'Incompatible vector shapes'
        if self.shape[0] == 1:
            new = [[self.values[0][x] - other.values[0][x] for x in range(len(self.values[0]))]]
            return Vector(new)
        else:
            new = [[self.values[x][0] - other.values[x][0]] for x in range(len(self.values))]
            return Vector(new)

    def __rsub__(self, other):
        assert isinstance(other, Vector), 'Invalid vector operation with ' + str(type(other))
        return other.__sub__(self)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            raise NotImplemented("Division Vector / Vector is not defined here.")
        assert isinstance(other, int) or isinstance(other, float), 'only division with scalars'
        if other in {0, 0.0}:
            raise ZeroDivisionError("Division by zero")
        new = []
        for x in self.values:
            cr = []
            for y in x:
                cr.append(y / float(other))
            new.append(cr)
        return (new)

    def __rtruediv__(self, other):
        if isinstance(other, Vector):
            raise NotImplemented("Division Vector / Vector is not defined here.")
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, other):
        if isinstance(other, Vector):
            raise NotImplemented("Multiplication Vector * Vector is not defined here.")
        assert isinstance(other, int) or isinstance(other, float), 'only multiplication with scalars'
        new = []
        for x in self.values:
            cr = []
            for y in x:
                cr.append(y * float(other))
            new.append(cr)
        return (new)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        """Return the string of vector's values to print"""
        return f'{self.values}'

    def __str__(self):
        """Return the string of vector's values to print"""
        return f'{self.values}'


if __name__ == '__main__':
    v1 = Vector([[0.0], [1.0], [2.0]])
    print(v1.__dict__)
    try:
        v = Vector((1,4))
        print(v.__dict__)
        v3 = Vector([[1.0, 3.0]])
        v4 = Vector([[2.0, 4.0]])
        print(v3.dot(v4))
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        print(v1.dot(v2))
        print(v1, v2)
        print(v1 - v2)
        print(v2 - v1)
        print(v1 * 10)
        print(10 * v2)
    except AssertionError as msg:
        print('Error:', msg)
