import sys
import os

# Add the parent directory to the path so we can find 'main.py'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import the app. Vercel will automatically detect 'app' and run it as ASGI.
from main import app