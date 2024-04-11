import os
import sys
from src.views.login import main as run_gui_login

def setup_environment():
    """
    Set up the Python environment by adding the parent directory of 'src/' to the Python module search path.

    This function gets the current directory of the script, finds its parent directory, and inserts it at the beginning
    of the Python module search path to allow importing modules from the 'src/' directory.
    """
    # Add the parent directory of 'src/' to the Python module search path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)

def main():
    """
    The main function to set up the environment and run the GUI login script.

    This function first sets up the Python environment by calling setup_environment() to ensure that the necessary
    modules can be imported. Then, it runs the GUI login script.
    """
    # Set up the environment
    setup_environment()

    # Run the GUI login script
    run_gui_login()

if __name__ == "__main__":
    main()
