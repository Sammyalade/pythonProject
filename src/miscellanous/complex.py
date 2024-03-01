class Complex:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __eq__(self, other):
        return Complex(self.left == other.left, self.right == other.right)

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __lt__(self, other):
        return self.left < other.left and self.right < other.right

    def __ge__(self, other):
        return self.left >= other.left and self.right >= other.right

    def __le__(self, other):
        return self.left <= other.left and self.right <= other.right

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.right
        return self

    def __isub__(self, other):
        self.left -= other.left
        self.right -= other.right
        return self

    def __repr__(self):
        return f"{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i"


x = Complex(2, 8)
y = Complex(9, -5)

print(x)
print(y)

print(x + y)
print(x - y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
x += y
print(x)
x = Complex(2, 8)
x -= y
print(x)
