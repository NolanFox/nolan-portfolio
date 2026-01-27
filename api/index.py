import sys
import os

# CURRENT FIX: Add the parent directory to Python's path
# This allows Vercel to "see" main.py and the components folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app