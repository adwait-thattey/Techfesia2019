import unittest


def suite():
    return unittest.TestLoader().discover("management.tests", pattern="*.py")
