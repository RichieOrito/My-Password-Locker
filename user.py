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

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user_name exists from the user list.
        Args:
            user_name: User name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False