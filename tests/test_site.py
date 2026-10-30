from pathlib import Path
import unittest

class SiteTests(unittest.TestCase):
    def test_schedule_page(self):
        html = Path("site/index.html").read_text(encoding="utf-8")
        self.assertIn("<h1>Расписание занятий</h1>", html)
        self.assertIn("Понедельник", html)
