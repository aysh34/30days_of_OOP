class A:
    def identity(self):
        print("I am A")


class B(A):
    def identity(self):
        print("I am B")
        super().identity()


class C(A):
    def identity(self):
        print("I am C")
        super().identity()


class D(B, C):
    def identity(self):
        print("I am D")
        super().identity()


d = D()
d.identity()
print(D.__mro__)
