# creating a reptile class to Inherit everything from Animal class

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        # we have keyword called SUPER which inherits everything from parent class at the time of initialisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # not all reptiles are tetrapod
        self.heart_chambers = [3, 4]


    def seek_heat(self):
        return "it's rainy and windy, where is the sun......."

    def hunt(self):
        return "keep hunting for food until you get it "

    def use_venom(self):
        return "if I've got it I'm using it"

reptile_object = Reptile()

print("This function is from Reptile class " + reptile_object.hunt())
print("This function is Inherited from an Animal class " + reptile_object.eat())
# This is the amazing benefit of using OOP and Ineritance