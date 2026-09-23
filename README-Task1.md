
# DICE ROLLING GAME

A console-based Python program that simulates rolling a pair of six-sided dice. Built during Month 1 of my Python Development internship at **Arch Technologies**.

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
python dice_rolling_game.py
```

Optional visual version with ASCII dice faces and a rolling animation:

```
python dice_rolling_game_visual.py
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
Roll two dice (random.randint(1, 6) each)
  |
  v
Show both results and the total
  |
  v
If die1 == die2 -> print "Nice, that's a double!"
  |
  v
Ask: Roll again? (y/n)
  |
  v
"y" -> loop back to roll again
anything else -> print goodbye message and exit
```

---

## Concepts Applied

| # | Concept |
|---|---------|
| 1 | `random` module |
| 2 | Functions |
| 3 | `while` loops |
| 4 | Conditional logic |
| 5 | f-strings |
| 6 | User input handling |

---

## Example Session

```
Welcome to the Dice Rolling Game!
Let's roll a pair of dice and see what you get.

You rolled: 3 and 3
Total: 6
Nice, that's a double!

Roll again? (y/n): n

Thanks for playing! See you next time.
```

---

## Notes

- `random.randint(1, 6)` is used because it's inclusive on both ends, matching exactly what a real six-sided die can land on.
- Input is cleaned with `.strip().lower()` so `Y`, `y`, or a stray space all behave the same way.
- The double-detection message and the ASCII visual version are both extras added on top of the original task — they don't change the core random-number logic, only what's displayed.

---

## Files

| File | Purpose |
|------|---------|
| `dice_rolling_game.py` | Main program — run this |
| `dice_rolling_game_visual.py` | Optional version with ASCII dice faces + rolling animation |
| `requirements.txt` | Dependency list (none — standard library only) |
| `README.md` | This file |

## Author

**Muhammad Tanveer**
Python Development Intern — Arch Technologies
