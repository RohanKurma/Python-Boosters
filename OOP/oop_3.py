class Kettle(object):
    #Class Attribute.
    power_souce = 'electricity'
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

#print(hamilton.power)

print(Kettle.power_souce)
print(kenwood.power_souce)
print(hamilton.power_souce)
print('Changing to Atomic Power')

Kettle.power_souce = 'Atomic'

print(Kettle.power_souce)
print(kenwood.power_souce)
print(hamilton.power_souce)

print('changing the power source of kenwood.')

# When we change the power source of kenwood, instead of changing the 
# global variable power_source, it creates it's own local variable
# power_source which can be viewed in __dict__

kenwood.power_souce = 'gas'

print(kenwood.power_souce)
print(hamilton.power_souce)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
