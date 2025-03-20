#import debugBuddy.debug as debug
import sys
from .cli import motivate_cli, error_message_help_cli, ask_for_input_cli, debug_hint_cli

def main():
    if len(sys.argv) < 2:
        print("debugBuddy - A debugging helper package")
        print("Available commands:")
        print("  motivate <name>")
        print("  error_message_help <ErrorType>")
        print("  ask_for_input <question> <style>")
        print("  debug_hint [issue_type] [experience_level]")
        return

    command = sys.argv[1]
    # Remove the command from sys.argv
    sys.argv = [sys.argv[0]] + sys.argv[2:]

    if command == "motivate":
        motivate_cli()
    elif command == "error_message_help":
        error_message_help_cli()
    elif command == "ask_for_input":
        ask_for_input_cli()
    elif command == "debug_hint":
        debug_hint_cli()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()