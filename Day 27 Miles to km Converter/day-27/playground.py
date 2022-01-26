def add(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result


print(add(5, 6, 9, 5))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=4)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Skoda")

print(my_car.make, my_car.model)
