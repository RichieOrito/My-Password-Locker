import random
import string


class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,user_name,passowrd):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New user first name.
            last_name : New user last name.
            user_name: New user user_name.
            password: New user password.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = passowrd

    def save_user(self):
        '''
        save_user method saves user objects into the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,user_name):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: username to search for.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    # @classmethod
    # def user_exist(cls,user_name):
    #     '''
    #     Method that checks if a user_name exists from the user list.
    #     Args:
    #         user_name: User name to search if it exists
    #     Returns :
    #         Boolean: True or false depending if the user exists
    #     '''
    #     for user in cls.user_list:
    #         if user.user_name == user_name:
    #                 return True

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

        return False

class Credentials:
    '''
    class that generates new instances of credentials
    '''
    accounts = []
    
    def __init__(self,account_username,account_name,account_password):
        '''
        __init__ method that helps us define properties for our object
        '''
        self.account_username = account_username
        self.account_name = account_name
        self.account_password = account_password

    def save_account(self):
        '''
        saves user info into the accounts
        '''
        Credentials.accounts.append(self)

    def delete_account(self):
        '''
        delete user info from the accounts
        '''
        Credentials.accounts.remove(self)

    @classmethod
    def display_account(cls):
        '''
        method that retuns a list of the accounts
        '''
        return cls.accounts
    @classmethod
    def find_account(cls,account_name):
        '''
        Method that takes in a account_name and returns an account that matches that account_name
        '''
        for credentials in cls.accounts:
            if credentials.account_name == account_name:
                return credentials

    def generatePassword(stringLength=8):
        '''
        Method that generates a password 
        '''
        account_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "xoxo@123"
        return ''.join(random.choice(account_password) for i in range(stringLength))