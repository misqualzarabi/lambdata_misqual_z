import random


class Product():
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = 10 / 20
        if ratio > 0.5:
            ('not so stealable')
        if ratio >= 0.5 or ratio < 1.0:
            print('kinda stealable')
        else:
            print('very stealable')
            return

    def explode(self):
        product = 0.5 * 20
        if product < 10:
            print('...fizzle')
        if product >= 10 or product < 50:
            print('boom')
        else:
            print('...BABOOM!!')
            return


class BoxingGlove(Product):
    def __init__(self, weight=10):
        super().__init__(
            name=None,
            price=10,
            flammability=0.5,
            identifier=random.randint(
                1000000,
                9999999))
        self.weight = weight

    def explode(self):
        print('...it is a glove')

    def punch(self):
        weight = 10
        if weight < 5:
            print('That tickles')
        if weight >= 5 or weight < 15:
            print('Hey that hurt')
        else:
            print('OOUCH')
            return


if __name__ == "__main__":
    prod = Product("A cool toy")
    print(prod.name)
    print(prod.price)
    print(prod.weight)
    print(prod.flammability)
    print(prod.identifier)
    prod.stealability()
    prod.explode()

    glove = BoxingGlove('Punchy the third')
    print(glove.weight)
    print(glove.price)
    glove.explode()
    glove.punch()
