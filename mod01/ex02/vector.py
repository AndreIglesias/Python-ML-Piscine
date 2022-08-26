

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

    def dot(self):
        pass

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

    def __repr__(self):
        """Return the string to print with the recipe info"""
        return f'{self.values}'

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f'{self.values}'



if __name__ == '__main__':
    v = Vector([[0.0], [1.0], [2.0]])
    print(v.__dict__)
    try:
        v = Vector(10)
        print(v.__dict__)
        print(v.T())
        print(v)
    except AssertionError as msg:
        print('Error:', msg)
