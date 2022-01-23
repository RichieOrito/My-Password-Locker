class User:
    '''
    Class that generates new instances of contacts
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