import unittest


def suite():
    return unittest.TestLoader().discover("etc.tests", pattern="*.py")
