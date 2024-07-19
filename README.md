# Probability Calculator

This project demonstrates the use of probability simulation in Python to estimate the probability of drawing certain balls randomly from a hat. The `Hat` class and the `experiment` function perform repeated experiments to calculate the desired probability.

## Classes

### Hat

The `Hat` class represents a hat containing balls of different colors.

#### Methods

- **`__init__(self, **balls)`**: Initializes the hat with a specified number of balls of each color.

  - **Arguments**:
    - `**balls`: Arbitrary keyword arguments representing the number of balls of each color.
- **`draw(self, num_balls)`**: Draws a specified number of balls from the hat randomly.

  - **Arguments**:
    - `num_balls`: The number of balls to draw from the hat.
  - **Returns**:
    - A list of strings representing the drawn balls.

### Experiment Function

The `experiment` function performs multiple experiments to estimate the probability of drawing a specified set of balls from the hat.

#### Parameters

- **`hat`**: A `Hat` object containing the balls to draw from.
- **`expected_balls`**: A dictionary indicating the exact group of balls to attempt to draw from the hat for the experiment.
- **`num_balls_drawn`**: The number of balls to draw out of the hat in each experiment.
- **`num_experiments`**: The number of experiments to perform.

#### Returns

- **`float`**: The estimated probability of drawing the specified set of balls.

## Usage

Here are some examples of how to use the `Hat` class and the `experiment` function:

### Examples

```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)  #Output 0.356

hat = Hat(yellow=3, blue=2, green=6)
probability = experiment(hat=hat,
                         expected_balls={'blue': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=1000)
print(probability)  #Output 0.492

hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'striped': 3},
                         num_balls_drawn=6,
                         num_experiments=5000)
print(probability)  #Output 0.274

Note: The actual output may vary slightly due to the random nature of the experiments.
```
