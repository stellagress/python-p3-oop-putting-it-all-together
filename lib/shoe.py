#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand = "Adidas", size = 9, condition = "New"):
        self.brand = brand
        self.size = size
        self.condition = condition



    def get_size(self):
        return self._size
    

    def set_size(self, size):
        if (type(size) == int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)


    def cobble(self):
        print("Your shoe is as good as new!")
        # print("says that the shoe has been repaired.") +



    def cobble_makes_new(self, condition):
        return condition == "New"









        #    def test_cobble_makes_new(self):
        # '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        # stan_smith = Shoe("Adidas", 9)
        # stan_smith.cobble()
        # assert(stan_smith.condition == "New")

