import unittest


def suite():
    return unittest.TestLoader().discover("event_registrations.tests", pattern="*.py")
