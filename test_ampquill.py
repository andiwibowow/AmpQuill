# test_ampquill.py
"""
Tests for AmpQuill module.
"""

import unittest
from ampquill import AmpQuill

class TestAmpQuill(unittest.TestCase):
    """Test cases for AmpQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AmpQuill()
        self.assertIsInstance(instance, AmpQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AmpQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
