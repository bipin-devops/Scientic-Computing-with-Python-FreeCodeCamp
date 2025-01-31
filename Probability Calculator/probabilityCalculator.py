import copy
import random

class Hat:
    contents: list
    
    def __init__(self, **kwargs):
        self.contents = [color for color, count in kwargs.items() for _ in range(count)]

    def draw(self,number):
        if number > len(self.contents):
            all_balls = self.contents.copy()
            self.contents = []
            return all_balls
            
        random_elements = random.choices(self.contents, k = number)
        
        # dictionary to count occurence in random_element
        count_to_remove = {}
        for item in random_elements:
            if item in count_to_remove:
                count_to_remove[item] += 1
            else:
                count_to_remove[item] = 1
        
        # list of index to remove
        index_to_remove = []
        for i, item in enumerate(self.contents):
            if item in count_to_remove and count_to_remove[item] > 0:
                index_to_remove.append(i)
                count_to_remove[item] -= 1

        # Remove element starting from highest index 
        for index in sorted(index_to_remove, reverse = True):
            self.contents.pop(index)
        return random_elements


        

    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability: float
    hat_copy = copy.copy(hat)
    
    

hat1 = Hat(yellow=3, blue=2, green=6)
hat1.draw(15)