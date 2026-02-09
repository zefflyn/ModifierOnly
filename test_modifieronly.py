# test_modifieronly.py
"""
Tests for ModifierOnly module.
"""

import unittest
from modifieronly import ModifierOnly

class TestModifierOnly(unittest.TestCase):
    """Test cases for ModifierOnly class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModifierOnly()
        self.assertIsInstance(instance, ModifierOnly)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModifierOnly()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
