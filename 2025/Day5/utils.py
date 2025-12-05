try:
    import logging
    import os
    import sys
    from enum import Enum

except ModuleNotFoundError or ImportError as e:
    print("Imports failed")
    print(e)




class Range_t:

    def __init__(self, range:str):
        self.lower, self.upper = self.parse_range_string(range)
        


    def parse_range_string(self, range_str):
        buf = range_str.split("-")

        lower = int(buf[0])
        upper = int(buf[1])

        return lower, upper
    

    def in_range(self, val):
        if val >= self.lower and val <= self.upper:
            return True
        
        else:
            return False

    def range_str(self):
        return "{}->{}".format(self.lower, self.upper)
    
    def calc_valid_id_count(self):
        
        return (self.upper-self.lower)+1

    def __repr__(self):

        return self.__str__()


    def __str__(self):
        
        return "<Range_t> {} to {}".format(self.lower, self.upper)
    

class IngredientStatus(Enum):
    SPOILT = 0,
    FRESH = 1,
    UNKNOWN = 2


class Ingredient_t:

    def __init__(self, id):
        self.id = id
        self.state = IngredientStatus.UNKNOWN

        self.applicable_ranges = []
        self.range_count = 0


    def add_range(self, range_to_add):
        self.applicable_ranges.append(range_to_add)
        self.range_count += 1

    def set_state(self, state):
        self.state = state



    def pretty_print(self):
        message = "<Ingredient_t> ID: {} ({}) in {}".format(self.id, self.state.name, self.applicable_ranges)

        print(message)


    def __repr__(self):

        return self.__str__()


    def __str__(self):
        
        return "<Ingredient_t> ID: {} ({})".format(self.id, self.state.name)