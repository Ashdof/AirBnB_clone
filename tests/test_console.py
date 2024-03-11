#!/usr/bin/python3
"""contains defbitions of unittests for console.py

classes:
    TestHBNBConsole

    """
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBConsole(unittest.TestCase):
    """Unittest for console commands"""

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("EOF  all  create  destroy  help  quit  show
                          update", output)

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("Show information about the specified object",
                          output)

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "")

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345 name 'John Doe'")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main()
