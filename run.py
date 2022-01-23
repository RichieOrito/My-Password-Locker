#!/usr/bin/env python3.9
from user import User

def create_user(fname,lname,uname,upassword):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,uname,upassword)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to del user
    '''
    user.del_user()