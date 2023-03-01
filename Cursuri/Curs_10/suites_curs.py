import unittest
from alerts import Alerts

import HtmlTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Alerts))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='My first report', report_name='My first report name')
        runner.run(test_derulat)
































