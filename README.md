# 🎓 Student_Survival_Manager

## 📘 Description

**Student Survival Manager** is a small Python application designed to help students manage their university tasks, deadlines and workload.

Instead of only showing a normal to-do list, the application calculates **Panic Points** based on how close a deadline is and how difficult the task is. This gives students a simple and funny way to see which tasks need their attention first.

## 🎯 Problem

A student struggles to organize the multiple tasks assigned and fails exams :)

## 🧩 Scenario

Student Survival Manager manages students' workload by tracking tasks, checking deadlines and using **Panic Points** to see which tasks are the most urgent.

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

---

## 📋 User Stories

### US-01: View the dashboard

**As a** student, **I want** to see a summary of my current workload, **so that** I can understand my situation immediately.

**Acceptance criteria**

- *Given* the application contains active and completed tasks, *when* the student opens the dashboard, *then* the number of active and completed tasks is displayed.
- *Given* there are 3 active tasks and 2 completed tasks, *when* the dashboard is displayed, *then* it shows `Active tasks: 3` and `Completed tasks: 2`.
- *Given* active tasks exist, *when* the dashboard is displayed, *then* the Base Panic Points, Overall Panic Score and Panic Level are displayed.
- *Given* no active tasks exist, *when* the dashboard is displayed, *then* the Panic Score is `0.00` and the Panic Level is `NO PANIC 😎`.

---

### US-02: See current panic level

**As a** student, **I want** to see my "panic level", **so that** I can quickly understand my current workload.

**Acceptance criteria**

- *Given* active tasks exist, *when* the Panic Score is calculated, *then* the Panic Points of all active tasks are added.
- *Given* multiple active tasks exist, *when* the Panic Score is calculated, *then* the concurrency effect is added.
- *Given* a Panic Score has been calculated, *when* the result is displayed, *then* both the numerical Panic Score and Panic Level are shown.
- *Given* a task is completed, *when* the Panic Score is recalculated, *then* that task no longer contributes to the Base Panic Points or number of active tasks.

---

### US-03: Add tasks

**As a** student, **I want** to add a task with a description, **so that** I can keep track of my university work.

**Acceptance criteria**

- *Given* the student selects the option to add a task, *when* a valid description, deadline and difficulty are entered, *then* a new task is created.
- *Given* a task is created, *when* it is added to the application, *then* its initial status is `active`.
- *Given* the description is empty, *when* the student tries to create the task, *then* the task is not created and an error message is displayed.
- *Given* difficulty is lower than `1` or higher than `5`, *when* the student tries to create the task, *then* the value is rejected.
- *Given* the deadline is not a valid date, *when* the student tries to create the task, *then* the task is not created.

---

### US-04: Save tasks to a file

**As a** student, **I want** my tasks to be saved, **so that** I do not lose them.

**Acceptance criteria**

- *Given* a new task is created, *when* it is saved, *then* its description, deadline, difficulty and status are written to a file.
- *Given* tasks were saved during a previous session, *when* the application starts again, *then* the saved tasks are loaded.
- *Given* a task is edited, *when* the changes are confirmed, *then* the stored information is updated.
- *Given* a task is marked as completed, *when* the application is closed and restarted, *then* the task remains completed.

---

### US-05: Show the prioritized tasks

**As a** student, **I want** to prioritize my tasks, **so that** I can see them organized.

**Acceptance criteria**

- *Given* multiple active tasks exist, *when* the prioritized task list is opened, *then* all active tasks are displayed.
- *Given* two tasks have different Panic Points, *when* the list is displayed, *then* the task with more Panic Points appears first.
- *Given* a task has been completed, *when* the prioritized list is displayed, *then* that task is not included.
- *Given* no active tasks exist, *when* the prioritized list is opened, *then* the message `No active tasks.` is displayed.

---

### US-06: View task description

**As a** student, **I want** to see the task description, **so that** I can check what the task is about.

**Acceptance criteria**

- *Given* an existing task is selected, *when* the student opens its details, *then* the task description is displayed.
- *Given* the student selects a task that does not exist, *when* the application searches for it, *then* the message `Task not found.` is displayed.

---

### US-07: View task deadline

**As a** student, **I want** to see the task deadline, **so that** I can check how much time I have left.

**Acceptance criteria**

- *Given* an existing task has a deadline, *when* the student opens the task details, *then* the deadline is displayed.
- *Given* the deadline has already passed, *when* the task is viewed, *then* the application indicates that the task is overdue.

---

### US-08: View difficulty level of the task

**As a** student, **I want** to see the task difficulty level, **so that** I can check the effort that I have to put into it.

**Acceptance criteria**

- *Given* a task has a difficulty value, *when* its details are displayed, *then* the difficulty is shown.

---

### US-09: Edit a task

**As a** student, **I want** to edit the task, **so that** I can correct or update its information.

**Acceptance criteria**

- *Given* an existing task is selected, *when* the student changes its description, *then* the new description replaces the previous one.
- *Given* an existing task is selected, *when* the student changes its deadline, *then* the new deadline is saved.
- *Given* an existing task is selected, *when* the student changes its difficulty, *then* the new difficulty is saved.
- *Given* a task has been successfully edited, *when* the operation is completed, *then* `Task updated successfully.` is displayed.

---

### US-10: Calculate panic points

**As a** student, **I want** the application to calculate panic points, **so that** I know how urgent my tasks are.

**Acceptance criteria**

- Each active task receives a numerical Panic Points value.
- Panic Points depend only on task difficulty and the exact number of days remaining before the deadline.
- Panic Points are rounded to two decimal places when displayed.

The calculation uses:

```text
Days Left = max(Deadline - Today, 0)

Panic Points = Difficulty / √(Days Left + 1)
```

- *Given* difficulty is `5` and the task is due today, *when* Panic Points are calculated, *then* the result is `5.00`.
- *Given* difficulty is `5` and the task is due in 1 day, *when* Panic Points are calculated, *then* the result is `3.54`.
- *Given* difficulty is `5` and the task is due in 14 days, *when* Panic Points are calculated, *then* the result is `1.29`.
- *Given* a task is overdue, *when* Panic Points are calculated, *then* Days Left is treated as `0`.
- *Given* a completed task exists, *when* the current workload is calculated, *then* the completed task is not included.

---

### US-11: Mark a task as completed

**As a** student, **I want** to mark the task as completed, **so that** I can keep track of my progress.

**Acceptance criteria**

- *Given* an active task is selected, *when* the student marks it as completed, *then* its status changes from `active` to `completed`.
- *Given* a task is completed, *when* the prioritized task list is displayed, *then* that task is not included.
- *Given* a task is completed, *when* the dashboard is displayed, *then* the active-task count decreases and the completed-task count increases.
- *Given* a completed task previously contributed Panic Points, *when* the Panic Score is recalculated, *then* those Panic Points are removed.
- *Given* the number of active tasks decreases, *when* the Panic Score is recalculated, *then* the concurrency effect is recalculated.
- *Given* a task is successfully completed, *when* the operation finishes, *then* `Task marked as completed ✅.` is displayed.

---

### US-12: Saving the result as a PDF

**As a** student, **I want** to save the results as a PDF, **so that** I can see an overview after closing the application.

**Acceptance criteria**

- * Given the results are displayed, when the student selects the option to save as PDF, then a PDF file is created.
- * Given the student saves the results as a PDF, when the PDF is opened, then it contains an overview of the results.
- * Given the PDF has been successfully created, when the saving process is completed, then the message `Successfully saved to PDF` is displayed.

**Example output**

```text

```

---

## 🛠️ Use Cases

- Show Dashboard
- Create Task
- Show task's description, deadline and difficulty
- Mark task as completed
- Calculate Panic Points
- Display "Panic Level"
