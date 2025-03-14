# Python Package Exercise
# debugBuddy

## Description
debugBuddy is your emotional support companion when debugging code. We all know debugging can be frustrating, demoralizing, and sometimes downright infuriating. debugBuddy is designed to make those moments a little more bearable by providing:

* Motivational messages when you feel like giving up
* Practical debugging tips tailored to your experience level and problem type
* A rubber duck debugging experience that talks back
* Comforting responses to scary error messages

Unlike traditional debugging tools that focus solely on fixing technical issues, debugBuddy addresses the emotional and psychological aspects of debugging, helping you maintain sanity and motivation throughout the process.

## Team
* [Jake Chang](https://github.com/jakechang1284)
* []
* []
* []

## Installation
[Link to PyPl]()

```bash
pip install debugBuddy
```
```python
import debugBuddy.debug as debug
```
## Functions
### Function 1

### Function 2

### Function 3
#### debug_hint(issue_type="general", experience_level="intermediate")
* Provides specific debugging tips and strategies based on the type of issue you're facing and your experience level.

##### Parameters:
issue_type (str, optional): Type of debugging issue you're facing. Options:
* "general": General debugging advice
* "syntax": Help with syntax errors
* "logic": Help with logical errors
* "runtime": Help with runtime errors
* "performance": Help with performance issues
* Default is "general"
experience_level (str, optional): Your programming experience level. Options:
* "beginner": For new programmers
* "intermediate": For programmers with some experience
* "advanced": For experienced programmers
* Default is "intermediate"

#### Returns:
* A string containing a debugging tip relevant to the specified issue type and experience level

#### Raises:
* ValueError: If an invalid issue_type or experience_level is provided

```python
import debugBuddy.debug as debug

# get a general debugging hint for intermediate programmers
hint = debug.debug_hint()
print(hint)
# output might be: "Try commenting out sections of code to isolate the issue"

# get a syntax debugging hint for beginners
beginner_hint = debug.debug_hint("syntax", "beginner")
print(beginner_hint)
# output might be: "Check for missing colons at the end of if, for, while, def statements"

# get a performance debugging hint for advanced programmers
advanced_hint = debug.debug_hint("performance", "advanced")
print(advanced_hint)
# output might be: "Profile your code to identify bottlenecks"
```

### Function 4

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.
