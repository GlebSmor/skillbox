import math


class MyMath:
    @classmethod
    def circle_len(cls, radius):
        return math.pi * radius * 2

    @classmethod
    def circle_sqr(cls, radius):
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, side):
        return side ** 3

    @classmethod
    def sphere_sqr(cls, radius):
        return math.pi * 4 * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sqr(radius=6)
res_3 = MyMath.cube_volume(side=5)
res_4 = MyMath.sphere_sqr(radius=5)
print(res_1, res_2, res_3, res_4, sep='\n')
