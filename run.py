#!/usr/bin/env python3.9
from re import A
from user import User
from user import Credentials
from random import *

def create_user(fname,lname,uname,upassword):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,uname,upassword)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to del user
    '''
    user.del_user()

def find_user(user_name):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(user_name)

def create_account(account_username,account_name,account_password):
    new_account = Credentials(account_username,account_name,account_password)
    return new_account

def save_account(user):
    user.save_account()

def delete_account(credentials):
    credentials.delete_account()

def find_account(account_name):
    return Credentials.find_account(account_name)

def display_account():
    return Credentials.display_account()

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that user and return a Boolean
    '''
    return User.User_exist(user_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password

def main():
    print("Hello Welcome to your Password Locker list. \n What is your name?")
    user_name = input()
    print("\n")

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                print("Use these short codes :\n ca - create User Account,\n lg - log into account User Account,\n ex -exit Account ")

                pick = input().lower()

                if pick == 'ca':
                        print("Create Account")
                        print("-"*15)

                        print ("Enter Your First name ...")
                        f_name = input()

                        print("Enter Last name ...")
                        l_name = input()

                        print("Enter User name ...")
                        u_name = input()

                        print("Enter Password ...")
                        u_password = input()


                        save_user(create_user(f_name,l_name,u_name,u_password)) # create and save new User.
                        print ('\n')
                        print(f"User Created Successfully {f_name} {l_name} {u_name} {u_password} created")
                        print ('\n')

                elif pick == 'lg':
                    print("your Username..")
                    u_name = input()

                    print("your Password..")
                    u_password = input()

                    if find_user(u_name):
                        print("\n")

                        print("You can create Your Social Accounts (ma) \n view them after creating (va) \n del- Delete Account")
                        print("-"*60)
                        print("ma or va")
                        pick = input()
                        print("\n")

                        if pick == "ma":
                            print("Add Your Credentials account")
                            print("-"*25)

                            account_username=u_name
                            print("Account Name")

                            account_name = input()
                            print("\n")

                            print("Generate Password(g) or Create new Password(c)?")
                            pick = input()

                            if pick == "g":
                                account_password = generate_Password()
                                print(f"password: {account_password}")
                                print("\n")

                            elif pick == "c":
                                print("Enter your Password")
                                account_password=input()

                            else:
                                print("please put in a valid choice")
                            save_account(create_account(account_username,account_name,account_password))
                            print("\n")
                            print(f"Username:{account_username}\n Account Name: {account_name}\n password: {account_password}")
                            print("\n")

                        elif pick == "va":
                            if display_account():
                                print("Here is a list of your created accounts:")
                                print("-"*25)
                                for credentials in display_account():
                                    print(f" Account name : {credentials.account_name} \n Account Username: {credentials.account_username} \n Account password: {credentials.account_password}")
                                    print('\n')
                                else:
                                     print("Account Does not Exist")


                        elif pick == "del":
                            print("Enter the account name of the Credentials you want to delete")
                            account_name = input()
                            print("\n")

                            if find_account(account_name):
                                account_name = find_account(account_name)
                                print("_"*50)
                                account_name.delete_account()
                                print('\n')
                                print(f"Your stored credentials for : {account_name.account_name} has been successfully deleted")
                                print('\n')
                            else:
                                print("That Credential you want to delete does not exist in your store yet")
                                print("\n")

                    else:
                        print("Invalid credentials")
                        print("\n")
                 
                elif pick == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()            