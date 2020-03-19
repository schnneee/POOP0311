import unittest


def fun(x):
    # return x + 2
    return x + 1


class MyTest(unittest.TestCase):
    def setUp(self):
        print("prepare something")
    def tearDown(self) -> None:
        print("clean, and store record")
    @classmethod
    def setUpClass(cls):
        print("one term startup")
    @classmethod
    def tearDownClass(cls) -> None:
        print("one term final house keeping")
    def test(self):
        print("run test")
        self.assertEqual(fun(3), 4)

    def test2(self):
        print("run test2")
        self.assertEqual(fun(-1), 0)

    def testSomehing(self):
        print("try test1")