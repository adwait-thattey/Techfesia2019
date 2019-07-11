import unittest


def suite():
    return unittest.TestLoader().discover("tickets.tests", pattern="*.py")
