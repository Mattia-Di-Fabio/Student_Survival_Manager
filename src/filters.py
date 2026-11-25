

def tasks_with_status(tasks, status):
    matches = []
    for task in tasks:
        if task["status"] == status:
            matches.append(task)
    return matches
