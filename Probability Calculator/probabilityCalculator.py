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

        # use sample instead of choices as we need without replacement
        random_elements = random.sample(self.contents, k = number)
        
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
    # expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. {}
    
    successful_experiments = 0

    for i in range(num_experiments):
        # copy the hat for this experiment
        hat_copy = copy.deepcopy(hat)

        # draw the ball
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # count the balls drawn
        count_balls_drawn = {}
        for ball in balls_drawn:
            if ball in count_balls_drawn:
                count_balls_drawn[ball] += 1
            else:
                count_balls_drawn[ball] = 1
        
        # verify if we got the expected balls or not
        success = True
        for ball, count in expected_balls.items():
            if ball not in count_balls_drawn or count_balls_drawn[ball] < count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    return successful_experiments / num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat1.draw(15)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(f'Probability: {probability}' )
