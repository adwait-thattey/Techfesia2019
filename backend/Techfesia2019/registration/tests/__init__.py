import unittest


def suite():
    return unittest.TestLoader().discover("registration.tests", pattern="*.py")
