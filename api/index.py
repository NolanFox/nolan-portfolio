import sys
import os

# 1. Get the absolute path to the current folder (api/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Get the parent folder (nolan-portfolio/)
parent_dir = os.path.dirname(current_dir)

# 3. Add the parent folder to the system path
# This allows 'from main import app' to work even though main.py is up one level
sys.path.append(parent_dir)

# 4. Import the app
from main import app