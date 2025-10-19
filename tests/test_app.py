import unittest
import os
import json
import sys

# Ensure app.py is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import add_task, delete_task, list_tasks, save_tasks, load_tasks, TASKS_FILE

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.test_file = TASKS_FILE
        save_tasks([])

    def test_add_task(self):
        add_task("Test Task")
        tasks = load_tasks()
        self.assertIn("Test Task", tasks)

    def test_delete_task(self):
        save_tasks(["Task 1", "Task 2"])
        delete_task(1)
        tasks = load_tasks()
        self.assertNotIn("Task 1", tasks)

    def test_list_tasks(self):
        save_tasks(["Task A", "Task B"])
        tasks = load_tasks()
        self.assertEqual(tasks, ["Task A", "Task B"])  # ✅ Added assertion

    def test_save_and_load(self):
        save_tasks(["Save Test"])
        tasks = load_tasks()
        self.assertEqual(tasks, ["Save Test"])

    def test_delete_invalid_index(self):
        save_tasks(["Only Task"])
        delete_task(5)  # Invalid index
        tasks = load_tasks()
        self.assertEqual(tasks, ["Only Task"])  # Should remain unchanged

    def test_add_empty_task(self):
        add_task("")
        tasks = load_tasks()
        self.assertIn("", tasks)

    def test_save_empty_list(self):
        save_tasks([])
        tasks = load_tasks()
        self.assertEqual(tasks, [])

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()