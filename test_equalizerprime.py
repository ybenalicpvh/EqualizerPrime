# test_equalizerprime.py
"""
Tests for EqualizerPrime module.
"""

import unittest
from equalizerprime import EqualizerPrime

class TestEqualizerPrime(unittest.TestCase):
    """Test cases for EqualizerPrime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EqualizerPrime()
        self.assertIsInstance(instance, EqualizerPrime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EqualizerPrime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
