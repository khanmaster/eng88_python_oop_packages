# animal file to create Animal class
# use of pass
class Animal:

    def __init__(self): # self refers to this class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "nom nom nom nom "

    def move(self):
        return "moving all around the world! "

# create an object of our Animal class
# cat = Animal() # creating an object of our Animal class called cat
# print(cat.breath()) # breathing for cat is abstracted

