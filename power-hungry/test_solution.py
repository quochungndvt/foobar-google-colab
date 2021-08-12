# coding=utf-8
import unittest
from solution import *

class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertAlmostEqual(solution([2, 0, 2, 2, 0]),8)
        self.assertAlmostEqual(solution([-2, -3, 4, -5]),60)
        self.assertAlmostEqual(solution([2, 0]),2)
        self.assertAlmostEqual(solution([0,-1, -10]),10)
        self.assertAlmostEqual(solution([0,-1, 0, -10, 2, 5]),100)
        self.assertAlmostEqual(solution([0, 10, -10, 1]),10)
        

if __name__ == '__main__':
    unittest.main()