import sys
from debugBuddy import motivate, error_message_help, ask_for_input, debug_hint

def motivate_cli():
    if len(sys.argv) < 2:
        print("Usage: motivate <name>")
        sys.exit(1)
    
    name = " ".join(sys.argv[1:])
    print(motivate(name))

def error_message_help_cli():
    if len(sys.argv) != 2:
        print("Syntax: error_message_help <ErrorType>")
        sys.exit(1)
    print(error_message_help(sys.argv[1]))

