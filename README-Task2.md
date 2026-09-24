
# TO-DO LIST APPLICATION

A console-based Python program that lets you add tasks, view your current list, and remove tasks once they're completed — with a live progress bar tracking how much you've finished. Built during Month 1 of my Python Developer internship at **Arch Technologies**.

**Repository:** https://github.com/libra-mtanveer316/arch-technologies-python-developer-internship-month1

---

## Quick Start

### 1. Install requirement

No external packages needed — this program uses only Python's standard library.

```
pip install -r requirements.txt
```

### 2. Run the program

```
python todo_app.py
```

---

## How It Works

```
Start
  |
  v
Print welcome message
  |
  v
Show menu (Add / View / Complete / Exit)
  |
  v
Read user's choice
  |
  +--> "1" -> Ask for task name -> Add to tasks list
  |
  +--> "2" -> Print pending tasks -> Show progress bar
  |
  +--> "3" -> Show tasks -> Ask which number is done
  |             -> Remove it from tasks -> increase completed_count
  |             -> Show updated progress bar
  |
  +--> "4" -> Print goodbye message -> Exit
  |
  v
Loop back to menu (unless Exit was chosen)
```

---

## Concepts Applied

| # | Concept |
|---|---------|
| 1 | Lists (`tasks.append`, `tasks.pop`) |
| 2 | Functions |
| 3 | `while` loops |
| 4 | Conditional logic |
| 5 | f-strings |
| 6 | `enumerate()` |
| 7 | `try` / `except` for input validation |
| 8 | Global variables (`completed_count`) |

---

## Example Session

```
Welcome to your To-Do List app!

----- To-Do List -----
1. Add a task
2. View tasks
3. Complete a task (removes it from the list)
4. Exit
Choose an option (1-4): 1
Enter the task: Finish Python assignment
Added: Finish Python assignment

----- To-Do List -----
1. Add a task
2. View tasks
3. Complete a task (removes it from the list)
4. Exit
Choose an option (1-4): 3

Your tasks:
1. Finish Python assignment
Progress: [--------------------] 0% (0/1 completed)

Which task number is done? 1
Nice, 'Finish Python assignment' is done and removed from your list.
Progress: [####################] 100% (1/1 completed)

----- To-Do List -----
1. Add a task
2. View tasks
3. Complete a task (removes it from the list)
4. Exit
Choose an option (1-4): 4
Alright, closing the app. Have a productive day!
```

---

## Notes

- `completed_count` is tracked separately from the `tasks` list, so the progress bar keeps an accurate record even after a task is removed.
- The progress bar is calculated against `completed_count + len(tasks)` — the total number of tasks ever added — so it never resets to 0% just because you completed everything.
- Input for completing a task is wrapped in `try`/`except`, so typing something that isn't a valid task number (letters, an out-of-range number, etc.) won't crash the program.
- Tasks are stored in memory only for this version — closing the program clears the list. That's intentional to keep the core logic simple and focused on the assignment requirements.

---

## Files

| File | Purpose |
|------|---------|
| `todo_list_app.py` | Main program — run this |
| `requirements.txt` | Dependency list (none — standard library only) |
| `README-Task2.md` | This file |

## Author

**Muhammad Tanveer**
Python Development Intern — Arch Technologies
