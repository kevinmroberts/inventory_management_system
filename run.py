import os
import sys
from src.gui.login import main as run_gui_login

def setup_environment():
    # Add the parent directory of 'src/' to the Python module search path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)

def main():
    # Set up the environment
    setup_environment()

    # Run the GUI login script
    run_gui_login()

if __name__ == "__main__":
    main()
