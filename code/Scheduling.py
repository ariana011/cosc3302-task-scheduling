import random

# create 50 tasks
tasks = [random.randint(1, 10) for _ in range(50)]

# Sequential (one processor)
T1 = sum(tasks)

# Parallel (4 processors)
processors = [1, 2, 4, 8]

for task in tasks:
    # find processor with least work
    min_index = processors.index(min(processors))
    processors[min_index] += task

Tp = max(processors)

# Basic metrics
speedup = T1 / Tp
efficiency = speedup / 4

# Output
print("Tasks:", tasks)
print("Sequential Time (T1):", T1)
print("Parallel Time (Tp):", Tp)
print("Speedup:", round(speedup, 2))
print("Efficiency:", round(efficiency, 2))
