import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, number):
        number = min(number, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(number)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        if all(drawn_balls.count(color) >= count for color, count in expected_balls.items()):
            count += 1

    return count / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)