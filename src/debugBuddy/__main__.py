#import debugBuddy.debug as debug
import random

def main():
    pass

if __name__ == "__main__":
    main()

def motivate(name):

    messages = [

        f"Hang in there, {name}!",
        f"Don't give up, {name}!",
        f"Almost there, {name}!",
        f"You're one function away from being done, {name}!",
        f"Think about how satisfied you'll feel when you're done, {name}!",
        f"One bug at a time, {name}!",
        f"Your code might be broken, {name}, but you're not! Keep going!",

    ]

    return random.choice(messages)