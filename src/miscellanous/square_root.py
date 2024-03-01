import math


def square_root(*numbers):
    list1 = []
    for number in numbers:
        calc = int(math.sqrt((2 * 50 * number) // 30))
        list1.append(calc)
    return ', '.join(str(x) for x in list1)


print(square_root(100, 150, 180))
print(square_root(100, 150, 180, 10, 180, 10, 180, 10, 180, 10, 180))
