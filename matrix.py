__author__ = 'student'
class Matrix:
    def _init_(self, m, n=None):
        assert type('m') == list
        assert type('n') == list
        if n==0:
            assert self == list
        else:
            assert self == Matrix(m,n)
        pass

    def determinant(self):
        pass

    def __eq__(self, other):
        assert type('other') == Matrix
        pass

    def get(self, i, j):
        pass

    def get_m(self):
        assert type('m') == list
        pass

    def get_n(self):
        assert type('n') == list
        pass

    def get_size(self):
        n=self.get_n
        m=self.get_m
        print(m,n)
        pass

    def invert(self):
        pass

    def __mul__(self, other):
        assert type('other') == Matrix
        pass

    def set(self, i, j, value):
        pass

    def __sub__(self, other):
        assert type('other') == Matrix
        pass

    def transpose(self):
        n=self.get_n
        m=self.get_m
        self = Matrix(n,m)
        pass

    def __truediv__(self, other):
        assert type('other') == Matrix
        pass



