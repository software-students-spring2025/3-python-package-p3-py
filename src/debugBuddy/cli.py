import sys
from debugBuddy import motivate

def motivate_cli():
    if len(sys.argv) < 2:
        print("Usage: motivate <name>")
        sys.exit(1)
    
    name = " ".join(sys.argv[1:])
    print(motivate(name))