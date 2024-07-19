import unittest
from client3 import getRatio, getDataPoint


class TestGetDataPoint(unittest.TestCase):
    def test_getDataPoint(self):
        """Test that getDataPoint returns the correct tuple"""
        quote = {
            "stock": "AAPL",
            "top_bid": {"price": "117.50", "size": 100},
            "top_ask": {"price": "118.50", "size": 100}
        }
        expected = ("AAPL", 117.50, 118.50, 118.00)
        result = getDataPoint(quote)
        self.assertEqual(result, expected)

    def test_getDataPoint_with_same_bid_ask(self):
        """Test getDataPoint when bid and ask prices are the same"""
        quote = {
            "stock": "GOOG",
            "top_bid": {"price": "1500.00", "size": 50},
            "top_ask": {"price": "1500.00", "size": 50}
        }
        expected = ("GOOG", 1500.00, 1500.00, 1500.00)
        result = getDataPoint(quote)
        self.assertEqual(result, expected)

    def test_getDataPoint_with_negative_prices(self):
        """Test getDataPoint with negative price values"""
        quote = {
            "stock": "TSLA",
            "top_bid": {"price": "-720.50", "size": 100},
            "top_ask": {"price": "-719.50", "size": 100}
        }
        expected = ("TSLA", -720.50, -719.50, -720.00)
        result = getDataPoint(quote)
        self.assertEqual(result, expected)


class TestGetRatio(unittest.TestCase):
    def test_ratio_normal(self):
        """Test that it returns correct ratio with normal inputs"""
        self.assertEqual(getRatio(10, 2), 5)

    def test_ratio_zero_denominator(self):
        """Test that it returns None when price_b is 0"""
        self.assertIsNone(getRatio(10, 0))

    def test_ratio_zero_numerator(self):
        """Test that it returns 0 when price_a is 0"""
        self.assertEqual(getRatio(0, 10), 0)

    def test_ratio_negative(self):
        """Test that it handles negative inputs correctly"""
        self.assertEqual(getRatio(-10, 2), -5)
        self.assertEqual(getRatio(10, -2), -5)
        self.assertEqual(getRatio(-10, -2), 5)

    def test_ratio_float(self):
        """Test that it handles float inputs correctly"""
        self.assertAlmostEqual(getRatio(1.5, 0.5), 3)


if __name__ == '__main__':
    unittest.main()
