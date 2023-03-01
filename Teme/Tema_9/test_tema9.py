import unittest
from tema9 import Login
from curs10 import Alerts
import HtmlTestRunner


class TestTema9Suite(unittest.TestCase):
    def test_tema9_suite(self):
        test_tema = unittest.TestSuite()
        test_tema.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Login),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Alerts)])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='My first report',
                                               report_name='My first report name', open_in_browser=True)
        runner.run(test_tema)