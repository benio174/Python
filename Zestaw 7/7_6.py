import itertools
import random

zero_one_cycle = itertools.cycle([0, 1])

for _ in range(10):
    print(next(zero_one_cycle))

for _ in range(5):
    print(next(random.choice(['N', 'S', 'W', 'E']) for _ in iter(int, 1)))

week_days_cycle = itertools.cycle(range(7))

for _ in range(15):
    print(next(week_days_cycle))