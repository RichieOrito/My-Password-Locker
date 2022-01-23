import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.Testcase: TestCase class that helps in creating text cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Richie","Orito","1234") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Richie")
        self.assertEqual(self.new_user.password,"1234")


if __name__ == '__main__':
    unittest.main()