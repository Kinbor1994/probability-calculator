import copy
import random

class Hat:
    """
    Represents a hat containing balls of various colors.

    Attributes:
        contents (list): A list of strings representing the balls in the hat.
    """

    def __init__(self, **balls):
        """
        Initializes the Hat object with a variable number of balls of each color.

        Args:
            **balls: Arbitrary keyword arguments representing the number of balls of each color.
        """
        self.contents = [color for color, count in balls.items() for _ in range(count)]
    
    def draw(self, num_balls):
        """
        Draws a specified number of balls from the hat at random.

        Args:
            num_balls (int): The number of balls to draw from the hat.

        Returns:
            list: A list of strings representing the drawn balls.
        """
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []
            return drawn_balls
            
        drawn_balls = []
        for _ in range(num_balls):
            choice = random.choice(self.contents)
            self.contents.remove(choice)
            drawn_balls.append(choice)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Performs a number of experiments to determine the probability of drawing
    a specific group of balls from the hat.

    Args:
        hat (Hat): A Hat object containing balls to be drawn.
        expected_balls (dict): A dictionary indicating the group of balls to attempt to draw.
        num_balls_drawn (int): The number of balls to draw out of the hat in each experiment.
        num_experiments (int): The number of experiments to perform.

    Returns:
        float: The probability of drawing the expected balls.
    """
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {color: drawn_balls.count(color) for color in expected_balls}
    
        success = all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items())
        if success:
            success_count += 1
    return success_count / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,expected_balls={'red': 2, 'green': 1},num_balls_drawn=5,num_experiments=2000)

print(probability)

