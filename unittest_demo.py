import time
import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Run method setUp()...")
        time.sleep(1)

    def tearDown(self):
        print("Run method tearDown()...")
        time.sleep(1)

    def test_case_1(self):
        print("Run method for test TC1")
        time.sleep(1)

    def test_case_2(self):
        print("Run method for test TC2")
        self.metoda_auxiliara()
        time.sleep(1)


    def metoda_auxiliara(self):
        print("Perform the auxiliary method")

    @unittest.skip
    def test_case_3(self):
        print("Run method for test TC3")
        time.sleep(1)
