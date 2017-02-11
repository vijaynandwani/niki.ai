import unittest
import phone

class Test(unittest.TestCase):
    def test_add(self):
        self.indianNumberList = phone.main('tests/data', '*.csv', r"[789]\d{9}")
        self.indianNumberExpectedList = ['8398179293','7423042850','9469713007','7222260175','8193787617','9428392698','8453049371','7847294067','7538938233','9009074482','7073838633','7847447291','9072067184','7824099886']
        self.assertListEqual(self.indianNumberList, self.indianNumberExpectedList)

if __name__ == '__main__':
    unittest.main()


