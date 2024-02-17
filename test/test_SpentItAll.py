import unittest
import sys
sys.path.append('/Users/quocchic/Dev/Code-Challanges/Online Assessment/Spent It All')
from solve import countPurchases


class TestCountPurchases(unittest.TestCase):

    def test_empty_cost_array(self):
        """Test with empty cost array."""
        cost = []
        budget = 10
        expected = 0
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected)

    def test_single_item_purchase(self):
        """Test with a single item that fits the budget."""
        cost = [5]
        budget = 10
        expected = 1
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected)

    def test_multiple_purchases(self):
        """Test with multiple items where some fit the budget."""
        cost = [5, 3, 3, 20]
        budget = 12
        expected = 3
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected)

    def test_budget_too_small(self):
        """Test with a budget that cannot afford any items."""
        cost = [10, 20, 30]
        budget = 5
        expected = 0
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected)

    def test_large_inputs(self):
        """Test with a larger array and budget to ensure scalability."""
        cost = [2,11, 5,20, 7, 9, 11, 13, 15]
        budget = 45
        expected = 5  # Should buy 5 items from the first 5 elements
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected)

    
    def test_max_n_min_cost(self):
        cost = [1] * (2*10**5)
        budget = 2*10**5
        expected = 2*10**5
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected, "Should be able to purchase each item once with the minimum cost")
    
    def test_boundary_budget(self):
        cost = [3, 5, 7]
        budget = sum(cost)
        expected = len(cost)
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected, "Should purchase all items once when budget equals sum of costs")
    def test_zero_budget(self):
        cost = [10, 20, 30]
        budget = 0
        expected = 0
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected, "Should not be able to make any purchases with a budget of zero")
    def test_one_item_just_below_budget(self):
        budget = 180
        expected = 20
        actual = countPurchases(cost, budget)
        self.assertEqual(actual, expected, "Should be able to make one purchase when one item is just below the budget")


