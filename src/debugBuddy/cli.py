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

def ask_for_input_cli(): #jime
    if len(sys.argv) < 3:  #question and style exist 
        print("Usage: ask_for_input <question> <style>")
        print("Styles: encouraging, sarcastic, philosophical")
        sys.exit(1)
    question = " ".join(sys.argv[1:-1]).strip()  # everything - style so question
    style = sys.argv[-1].lower().strip()# last thing is the style
    if not question:  #question exists
        print("Error: Question cannot be empty.")
        sys.exit(1)
    try:
        print(ask_for_input(question, style))
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)