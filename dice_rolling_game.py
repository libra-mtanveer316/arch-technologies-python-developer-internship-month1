
import random
import time
import sys

# Dice game with a visual twist:
# - shows real ASCII dice faces instead of just numbers
# - has a short "rolling..." animation before revealing the result

DICE_FACES = {
    1: ["┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"],
    2: ["┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"],
    3: ["┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"],
    4: ["┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"],
    5: ["┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"],
    6: ["┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"],
}

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def show_rolling_animation(rounds=8):
    # Prints a few random junk faces quickly, then erases them,
    # to fake the feeling of the dice tumbling before they land
    print("Rolling", end="", flush=True)
    for _ in range(rounds):
        time.sleep(0.15)
        print(".", end="", flush=True)
    print()

def print_dice_side_by_side(die1, die2):
    face1 = DICE_FACES[die1]
    face2 = DICE_FACES[die2]
    for line1, line2 in zip(face1, face2):
        print(f"  {line1}   {line2}")

def main():
    print("Welcome to the Dice Rolling Game!")
    print("Let's roll a pair of dice and see what you get.\n")

    while True:
        show_rolling_animation()
        die1, die2 = roll_dice()
        total = die1 + die2

        print_dice_side_by_side(die1, die2)
        print(f"\nYou rolled: {die1} and {die2}")
        print(f"Total: {total}")

        if die1 == die2:
            print("Nice, that's a double!")

        again = input("\nRoll again? (y/n): ").strip().lower()

        if again != "y":
            print("\nThanks for playing! See you next time.")
            break
        print()

if __name__ == "__main__":
    main()
