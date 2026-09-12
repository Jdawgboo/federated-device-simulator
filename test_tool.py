import unittest
from tool import aggregate


class FederatedTests(unittest.TestCase):
    def test_aggregates_by_device_weight(self):
        result = aggregate([{"w": 1.0, "b": 2.0}, {"w": 5.0, "b": 4.0}], [1, 3])
        self.assertEqual(result, {"b": 3.5, "w": 4.0})


if __name__ == "__main__":
    unittest.main()
