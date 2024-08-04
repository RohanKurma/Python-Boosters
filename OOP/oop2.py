class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    
    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

"""
Class: template for creating objects. All objects created using the same class will have the same
        characteristics.
Objects: an instance of a class.
Instantiate: Create an instance of a class.
Method: a function defines in a class.
Attribute: a variable bound to an instance of a class. 
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*"*80)

kenwood.power = 1.4
print(kenwood.power)

print(hamilton.power)

