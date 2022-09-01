import datetime
import unittest

from main import AchievementManager


class AchievementManagerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = AchievementManager("entries_mock.csv")

    def test_get_achievements(self):
        self.assertEqual(self.manager.get_achievements(""), None)
        self.assertEqual(len(self.manager.get_achievements("year")), 0)
        self.assertEqual(len(self.manager.get_achievements("year", datetime.date(2019, 1, 1))), 1)


if __name__ == '__main__':
    unittest.main()
