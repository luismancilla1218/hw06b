# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(6,3,4),'Scalene','6,3,4 should be scalene')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,3),'Isoceles','2,3,3 should be isoceles')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(2,-3,3),'InvalidInput','2,-3,3 should be invalid')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(2,399,3),'InvalidInput','2,399,3 should be invalid')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(2,"X",3),'InvalidInput','2,X,3 should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

