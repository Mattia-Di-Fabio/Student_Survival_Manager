from math import sqrt

from src.deadline import days_until
from src.filters import tasks_with_status


def panic_points(task, today):
    days_left = max(days_until(task, today), 0)
    points = task["difficulty"] / sqrt(days_left + 1)
    return points


def workload_effect(points):
    pair_total = 0
    for first in range(len(points)):
        for second in range(first + 1, len(points)):
            pair_total += points[first] * points[second]
    return pair_total / 5


def panic_totals(tasks, today):
    points = []
    for task in tasks_with_status(tasks, "active"):
        points.append(panic_points(task, today))
    base = sum(points)
    score = base + workload_effect(points)
    return base, score


def panic_level(score):
    if score == 0:
        level = "NO PANIC 😎"
    elif score < 5:
        level = "LOW 🙂"
    elif score < 15:
        level = "MEDIUM 😐"
    elif score < 30:
        level = "HIGH 😰"
    else:
        level = "CRITICAL 🚨"
    return level
