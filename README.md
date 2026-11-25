# 🎓 Student_Survival_Manager

## 📘 Description

**Student Survival Manager** is a small Python application designed to help students manage their university tasks, deadlines and workload.

Instead of only showing a normal to-do list, the application calculates **Panic Points** based on how close a deadline is and how difficult the task is. This gives students a simple and funny way to see which tasks need their attention first.

## 🎯 Problem

Students often have several assignments, projects and exams at the same time. Some tasks are more difficult than others, and deadlines can be very close together. This makes it difficult to decide what to work on first, especially when several important tasks compete for the student's time.

A normal to-do list shows what needs to be done, but does not help much with prioritization. Student Survival Manager combines task difficulty, deadlines and the number of active tasks to give students a clearer overview of their workload.

## 🧩 Scenario

A student has a programming assignment due tomorrow, a mathematics exercise due in three days and an economics report due next week.

1. The student opens Student Survival Manager and adds the three tasks with their descriptions, deadlines, difficulties and university modules.
2. The student checks the dashboard to see the number of active tasks and the current Panic Score and Panic Level.
3. The student opens the prioritized list to see which task needs attention first.
4. The student filters tasks by module or upcoming deadline and opens a task to check its details.
5. After finishing the programming assignment, the student marks it as completed. The dashboard and prioritized list update automatically.
6. The student exports a text report. When the application is opened again, the saved tasks are loaded from the file.

## 👤 User Roles

| Role | Description |
| --- | --- |
| **Student** | Creates and prioritizes tasks |

---

## 🧮 Panic Calculation

Each task receives **Panic Points** based on its difficulty and the number of days remaining:

```text
Panic Points = Difficulty / √(Days Left + 1)
```

For example, a difficulty `5` task has `5.00` points if due today, `3.54` if due tomorrow and `2.50` if due in 3 days.

### Overall Panic Level

The overall Panic Level is calculated by combining the Panic Points of all active tasks and adding an extra workload effect when several tasks are active at the same time.

```text
Panic Score = Σ Panic Points + (1 / 5) × Σ(Panic Pointᵢ × Panic Pointⱼ)
```

The second term considers every pair of active tasks. The value `5` represents the maximum possible Panic Points for one task.

This represents the additional pressure created by having multiple tasks competing for the student's time and attention.

For example, if three tasks have `5`, `2` and `1` Panic Points:

```text
Base Panic Points = 5 + 2 + 1 = 8

Concurrency effect =
(5×2 + 5×1 + 2×1) / 5
= 3.4

Panic Score = 8 + 3.4 = 11.4
```

This makes the Panic Score grow faster when several important tasks are active at the same time, while low-priority tasks have a smaller effect.

### Panic Level boundaries

| Panic Score | Panic Level |
| --- | --- |
| `0` | `NO PANIC 😎` |
| Greater than `0` and below `5` | `LOW 🙂` |
| From `5` (included) to below `15` | `MEDIUM 😐` |
| From `15` (included) to below `30` | `HIGH 😰` |
| `30` or more | `CRITICAL 🚨` |

For the example above, a Panic Score of `11.40` gives a `MEDIUM` Panic Level. Calculations use full precision; results are rounded to two decimal places only when displayed.

### Overdue tasks

```text
Days Left = max(Deadline - Today in whole days, 0)
Panic Points = Difficulty / √(Days Left + 1)
```

**Chosen rule:** An overdue task receives the same Panic Points as a task due today. For example, a difficulty `5` task due yesterday has `5.00` points. This keeps the original formula unchanged. Overdue tasks are clearly marked `OVERDUE` and appear before tasks due today when their Panic Points are equal. Completed tasks do not contribute to the Panic Score.

---

## 📋 User Stories

### US-01: View the dashboard   --    Iga Gawronska

**As a** student, **I want** to see a summary of my current workload, **so that** I can understand my situation immediately.

**Acceptance criteria**

- *Given* the application contains active and completed tasks, *when* the student opens the dashboard, *then* the number of active and completed tasks is displayed.
- *Given* there are 3 active tasks and 2 completed tasks, *when* the dashboard is displayed, *then* it shows `Active tasks: 3` and `Completed tasks: 2`.
- *Given* active tasks exist, *when* the dashboard is displayed, *then* the Base Panic Points, Overall Panic Score and Panic Level are displayed.
- *Given* no active tasks exist, *when* the dashboard is displayed, *then* the Panic Score is `0.00` and the Panic Level is `NO PANIC 😎`.
- *Given* an Overall Panic Score of `15.00`, *when* the dashboard is displayed, *then* the Panic Level is `HIGH 😰`.

---

### US-02: View completed tasks   --    Iga Gawronska

**As a** student, **I want** to see my completed tasks, **so that** I can keep track of what I have already finished.

**Acceptance criteria**

- *Given* completed and active tasks exist, *when* the student opens the completed task list, *then* only completed tasks are displayed.
- *Given* completed tasks exist, *when* the list is displayed, *then* each task's description, module and deadline are shown.
- *Given* no completed tasks exist, *when* the student opens the list, *then* the message `No completed tasks.` is displayed.

---

### US-03: Add tasks   --    Iga Gawronska

**As a** student, **I want** to add a task with a description, **so that** I can keep track of my university work.

**Acceptance criteria**

- *Given* the student selects the option to add a task, *when* a valid description, deadline and difficulty are entered, *then* a new task is created with a unique ID.
- *Given* a task is created, *when* it is added to the application, *then* its initial status is `active`.
- *Given* a student enters a university module, *when* the task is created, *then* the module is saved with the task; if no module is entered, it is set to `Unassigned`.
- *Given* the description is empty, *when* the student tries to create the task, *then* the task is not created and an error message is displayed.
- *Given* difficulty is lower than `1` or higher than `5`, *when* the student tries to create the task, *then* the value is rejected.
- *Given* the deadline is not a valid date, *when* the student tries to create the task, *then* the task is not created.

---

### US-04: Search tasks   --    Catia Lopes

**As a** student, **I want** to search for a task by its description, **so that** I can quickly find a particular assignment.

**Acceptance criteria**

- *Given* tasks exist, *when* the student enters a word that appears in a task description, *then* all matching tasks are displayed.
- *Given* a task is completed, *when* its description matches the search, *then* it is included and its status is shown.
- *Given* the student uses uppercase or lowercase letters, *when* searching, *then* the results are the same.
- *Given* no tasks match the search, *when* it is performed, *then* `No matching tasks.` is displayed.

---

### US-05: Show the prioritized tasks   --    Catia Lopes

**As a** student, **I want** to prioritize my tasks, **so that** I can see them organized.

**Acceptance criteria**

- *Given* multiple active tasks exist, *when* the prioritized task list is opened, *then* all active tasks are displayed.
- *Given* two tasks have different Panic Points, *when* the list is displayed, *then* the task with more Panic Points appears first.
- *Given* two tasks have equal Panic Points, *when* the list is displayed, *then* the task with the earlier deadline appears first.
- *Given* a task has been completed, *when* the prioritized list is displayed, *then* that task is not included.
- *Given* no active tasks exist, *when* the prioritized list is opened, *then* the message `No active tasks.` is displayed.

---

### US-06: View task details   --    Catia Lopes

**As a** student, **I want** to see a task's description, deadline and difficulty, **so that** I can check what the task is about and how much time I have left.

**Acceptance criteria**

- *Given* an existing task is selected, *when* the student opens its details, *then* the task description, module, deadline, difficulty, status and Panic Points are displayed.
- *Given* the deadline has already passed and the task is active, *when* the task is viewed, *then* the application indicates that the task is `OVERDUE`.
- *Given* the student selects a task that does not exist, *when* the application searches for it, *then* the message `Task not found.` is displayed.

---

### US-07: Filter tasks by module   --    Mattia Di Fabio

**As a** student, **I want** to filter tasks by university module, **so that** I can focus on one subject at a time.

**Acceptance criteria**

- *Given* tasks from different modules exist, *when* the student selects a module by number, *then* only tasks from that module are displayed, including active and completed tasks.
- *Given* two tasks belong to the same module, *when* that module is selected, *then* both tasks are shown.
- *Given* no tasks belong to the selected module, *when* the filter is applied, *then* `No matching tasks.` is displayed.

---

### US-08: View overdue tasks   --    Mattia Di Fabio

**As a** student, **I want** to see a list of overdue tasks, **so that** I know which deadlines I have missed.

**Acceptance criteria**

- *Given* an active task has a deadline before today, *when* the student opens the overdue task list, *then* the task appears with the label `OVERDUE`.
- *Given* a task is due today, *when* the overdue list is displayed, *then* it is not considered overdue.
- *Given* an overdue task is completed, *when* the overdue list is opened, *then* that task is not included.
- *Given* no overdue tasks exist, *when* the student opens the list, *then* `No overdue tasks.` is displayed.

---

### US-09: Edit a task   --    Mattia Di Fabio

**As a** student, **I want** to edit the task, **so that** I can correct or update its information.

**Acceptance criteria**

- *Given* an existing task is selected, *when* the student changes its description, *then* the new description replaces the previous one.
- *Given* an existing task is selected, *when* the student changes its deadline, *then* the new deadline is saved.
- *Given* an existing task is selected, *when* the student changes its difficulty, *then* the new difficulty is saved.
- *Given* an existing task is selected, *when* the student changes its university module, *then* the new module is saved.
- *Given* invalid information is entered, *when* the student tries to save the changes, *then* the invalid change is rejected.
- *Given* a task has been successfully edited, *when* the operation is completed, *then* `Task updated successfully.` is displayed.

---

### US-10: Filter tasks by upcoming deadline   --    Lirim Emërllahu

**As a** student, **I want** to see tasks due within the next few days, **so that** I can plan my upcoming work.

**Acceptance criteria**

- *Given* active tasks with different deadlines exist, *when* the student chooses the next `7` days, *then* only tasks due from today through the next seven days are displayed.
- *Given* a task is completed or overdue, *when* the upcoming deadline filter is applied, *then* it is not included.
- *Given* the student enters a negative or non-integer number of days, *when* the filter is applied, *then* an error message is displayed.
- *Given* no tasks are due within the selected period, *when* the filter is applied, *then* `No matching tasks.` is displayed.

---

### US-11: Mark a task as completed   --    Lirim Emërllahu

**As a** student, **I want** to mark the task as completed, **so that** I can keep track of my progress.

**Acceptance criteria**

- *Given* an active task is selected, *when* the student marks it as completed, *then* its status changes from `active` to `completed`.
- *Given* a task is completed, *when* the prioritized task list is displayed, *then* that task is not included.
- *Given* a task is completed, *when* the dashboard is displayed, *then* the active-task count decreases and the completed-task count increases.
- *Given* a completed task previously contributed Panic Points, *when* the Panic Score is recalculated, *then* those Panic Points are removed.
- *Given* the number of active tasks decreases, *when* the Panic Score is recalculated, *then* the concurrency effect is recalculated.
- *Given* a task is successfully completed, *when* the operation finishes, *then* `Task marked as completed ✅.` is displayed.

---

### US-12: Save the results as a text report   --    Lirim Emërllahu

**As a** student, **I want** to save the results as a text report, **so that** I can see an overview after closing the application.

**Acceptance criteria**

- *Given* the student selects the option to export a report, *when* the report is generated, *then* a `.txt` file is created.
- *Given* the report is opened, *when* the student reads it, *then* it contains the report date, the active and completed task counts, Base Panic Points, Overall Panic Score, Panic Level and a prioritized list of active tasks with their descriptions, modules, deadlines, difficulties, Panic Points and overdue status.
- *Given* no active tasks exist, *when* the report is exported, *then* it shows `0` active tasks, a Panic Score of `0.00` and `NO PANIC`.
- *Given* the report has been saved successfully, *when* the operation finishes, *then* `Report saved successfully.` is displayed.

A simple **TXT report** is the required output
---

## 🛠️ Use Cases

- Show Dashboard
- Create Task
- View completed tasks
- Show task's description, deadline and difficulty
- Search and filter tasks
- Show prioritized and overdue tasks
- Edit a task
- Mark task as completed
- Calculate Panic Points
- Display "Panic Level"
- Export a text report

