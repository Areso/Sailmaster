# test file
import unittest
import webserver_auth # tested module

class TestWebserAuth(unittest.TestCase):
    def setUp(self):
        self.widget = "test"
    # should start with test_
    def test_myloading(self):
        self.assertGreater(webserver_auth.myloading()[1],5)
