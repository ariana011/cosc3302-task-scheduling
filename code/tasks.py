import random

random.seed(1)

tasks = [random.randint(1, 10) for _ in range(50)]

print("Tasks:", tasks)
