#import debugBuddy.debug as debug
import random

def main():
    pass

if __name__ == "__main__":
    main()

def motivate(name):

    messages = [
        f"Keep going, {name}!",
        f"Hang in there, {name}!",
        f"Don't give up, {name}!",
        f"You're almost there, {name}!",
        f"You're doing amazing, {name}!",
        
    ]

    return random.choice(messages)