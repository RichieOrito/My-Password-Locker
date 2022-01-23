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

def find_user(user_name):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that user and return a Boolean
    '''
    return User.contact_exist(user_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()