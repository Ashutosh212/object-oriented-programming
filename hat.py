import random
class Hat:
    # not going to initiate __init__ dunder, bcz not need instance of this class
    houses = ['patna', 'mumbai', 'pune'] # there is only one copy of this and all will share the same
    
    @classmethod
    def sort(cls, name):
         print(name, "is in", random.choice(cls.houses))

# hat = Hat()
# hat.sort("Ashu")
Hat.sort("Ashu")