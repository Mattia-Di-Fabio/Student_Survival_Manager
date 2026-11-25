from math import sqrt

from src.deadline import days_until


def panic_points(task, today):
    days_left = max(days_until(task, today), 0)
    points = task["difficulty"] / sqrt(days_left + 1)
    return points
