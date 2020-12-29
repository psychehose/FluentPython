from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #객체를 문자열로 표현 repr 내장메서드에 의해 호출 if not 구현, <Vector object at 0x...>으로 출력
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


    #산술 연산자
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)



v = Vector(3, 4)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
print(abs(v))
