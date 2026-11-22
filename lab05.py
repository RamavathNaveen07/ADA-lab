from dataclasses import dataclass
from typing import List


# ---------- Fractional Knapsack ----------

def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    profit = 0.0

    for ratio, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            profit += value
            capacity -= weight
        else:
            profit += ratio * capacity
            capacity = 0

    return profit


# ---------- Job Scheduling ----------

@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    jobs.sort(key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    slots = [None] * (max_deadline + 1)

    for job in jobs:
        for slot in range(job.deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job.id
                break

    return [job_id for job_id in slots[1:] if job_id is not None]


# ---------- Main Program ----------

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Fractional Knapsack Maximum Profit:",
      fractional_knapsack(weights, values, capacity))


jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)

print("Optimal Job Sequence:", sequence)

total_profit = sum(
    job.profit for job in jobs if job.id in sequence
)

print("Maximum Job Scheduling Profit:", total_profit)