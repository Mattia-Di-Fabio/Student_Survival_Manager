from datetime import date, timedelta

from src.task import make_task


TODAY = date(2026, 4, 10)


def example_task(task_id=1, description="Lab report", days=0, difficulty=3,
    module="Science", status="active"):
    deadline = TODAY + timedelta(days=days)
    task = make_task(task_id, description, deadline.isoformat(), difficulty, module, status)
    return task
