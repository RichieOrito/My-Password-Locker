import unittest
from user import User
from user import Credentials

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
        self.new_user = User("Richie","Orito","Rish","1234") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Richie")
        self.assertEqual(self.new_user.last_name,"Orito")
        self.assertEqual(self.new_user.user_name,"Rish")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving new user
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","rish","1234") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    # def test_find_user_by_username(self):
    #     '''
    #     test to check if we can find a user by username and display information
    #     '''

    #     self.new_user.save_user()
    #     test_user = User("Test","user","1234") # new user
    #     test_user.save_user()

    #     found_user = User.find_by_user_name("abcd")

    #     self.assertEqual(found_user.first_name,test_user.first_name)

    # def test_user_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the user.
    #     '''

    #     self.new_user.save_user()
    #     test_user = User("Test","user","1234") # new user
    #     test_user.save_user()

    #     user_exists = User.user_exist("abcd")

    #     self.assertTrue(user_exists)    

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.Testcase: TestCase class that helps in creating text cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Richie","Instagram","1234") # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_username,"Richie")
        self.assertEqual(self.new_credentials.account_name,"Instagram")
        self.assertEqual(self.new_credentials.account_password,"1234")

    def test_save_account(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the account []
        '''
        self.new_credentials.save_account() # saving new credentials
        self.assertEqual(len(Credentials.accounts),2)

    def test_delete_account(self):
        '''
        test_delete_credentials to test if we can remove a user from our user list
        '''
        self.new_credentials.save_account()
        test_credentials = Credentials("Richie","Instagram","1234") # new credential
        test_credentials.save_account()

        self.new_credentials.delete_account()# Deleting credentials object
        self.assertEqual(len(Credentials.accounts),1)


if __name__ == '__main__':
    unittest.main()