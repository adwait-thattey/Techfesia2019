import unittest


def suite():
    return unittest.TestLoader().discover("events.tests", pattern="*.py")
