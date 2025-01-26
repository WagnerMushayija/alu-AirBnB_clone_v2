import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console."""

    def setUp(self):
        """Set up test environment."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after each test."""
        pass

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Check if an ID is returned

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertIn(model_id, output)  # Check if the ID is in the output

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {model_id}")
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertIn("** no instance found **", output)  # Check if instance is deleted

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)  # Check if BaseModel is listed

    def test_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f'update BaseModel {model_id} name "test"')
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertIn("name", output)  # Check if attribute is updated

    def test_count(self):
        """Test count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            # Create a BaseModel instance
            self.console.onecmd("create BaseModel")
            # Clear the buffer to remove the ID of the created object
            f.truncate(0)
            f.seek(0)
            # Run the count command
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")  # Check if count is correct

if __name__ == "__main__":
    unittest.main()