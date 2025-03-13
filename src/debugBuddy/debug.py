#File for all of our methods
# Sarah
import random

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


#Jimena's Rubber Ducky Method 
def ask_for_input(question, style="encouraging"):
    #question is a string
        #diff styles 
        #encouraging
        #sarcastic
        #philosophical

    encouragingResponses = [
        "Let's break this down step by step. Make sure to check all areas of your code.",
        "You're close! Walk through your logic. Where does it start behaving unexpectedly?",
        "Think about the inputs. Could any unexpected values be sneaking in?",
        "You got it, just try again!",
        "If you had to explain this to a complete beginner, how would you phrase it?",
    ]

    sarcasticResponses = [
        "Maybe your loop just really likes running. Have you checked the condition?",
        "Oh, your code works perfectly—just not in this universe...",
        "Did you remember to tell your loop it’s allowed to stop?",
        "Ah yes, the classic 'works in my head' bug. Try printing some values!",
        "Have you tried learning how to code."
    ]

    philosophicalResponses = [
        "Does a loop truly end, or does it just move on to a different state of being?",
        "If a function runs in a program and no one is around to call it, does it even exist?",
        "If you don't re-start the program, did it ever stop to begin with? ",
        "Maybe the loop is working as expected, and it's your expectations that are wrong.",
        "If an exception is raised in a forest of print statements, can it still be caught?",
        "Are your variable names formatted correctly for what is even in a name?"
    ]

    responseOptions = {
        "encouraging": encouragingResponses,
        "sarcastic": sarcasticResponses,
        "philosophical": philosophicalResponses
    }

    if style not in responseOptions:
        raise ValueError(f"Invalid style '{style}'. Choose from 'encouraging', 'sarcastic', or 'philosophical'.")

    return random.choice(responseOptions[style])

# Example question -> print(ask_for_input("Why isn't my loop breaking?", "sarcastic"))

