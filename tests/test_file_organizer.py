import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.file_organizer import organize_files

def test_organize_files_runs():
    try:
        organize_files()
        assert True
    except Exception as e:
        assert False, f"organize_files raised an exception: {e}"