#!/usr/bin/env python3

import sys
import json
import subprocess as sp


accounts  = {}

def choice(options):
    for i in range(len(options)):
        print(i+1, options[i])
    input_is_valid = False
    while input_is_valid == False:
        user_input = input()
        try:
            val = int(user_input)
            if val > 0 and val <= len(options):
                input_is_valid = True
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Sorry, the number must be between 1 and ", len(options))
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        except:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Sorry, you must enter a number!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    return (val-1)

def main_menu():
    ##displays error message with menu if error = true
    error = False
    while True:
        if error == False:
            sp.call('clear',shell=True)
        
        print("#########################################")
        print("#                                       #")
        print("# Would you like to sign in or sign up? #")
        print("#          PRESS 1 TO SIGN IN           #")
        print("#          PRESS 2 TO SIGN UP           #")
        print("#          PRESS X TO EXIT              #")
        print("#                                       #")
        print("#########################################")
        user_input = input()
        if user_input == "1":
            account_number = login_menu()
            if account_number == "ERROR":
                continue
            else:
                operations_menu(account_number)
        elif user_input == "2":
            signup_menu()
        elif user_input == "X" or user_input == "x":
            print("Thank you for using our bank. Have a good day!")
            sys.exit()
        else:
            sp.call('clear',shell=True)
            error = True
            print("Please enter '1', '2' or 'X'!")



def signup_menu():
    ##displays error message with menu if error = true
    error = False
    while True:
        if error == False:
            sp.call('clear',shell=True)
        global accounts
        name = input("Enter your name: ")
        new_account_number = str(int(max(accounts.keys()))+1)
        accounts[new_account_number]=[name, 0.0]
        print(f"Thank you for choosing our bank! Your account number is {new_account_number}")
        user_input = input("Press X to Exit or M for Main Menu")
        if user_input == "M" or user_input == "m":
            main_menu()
        elif user_input == "X" or user_input == "x":
            f = open("accounts.json", "w")
            json.dump(accounts, f)
            f.close()
            sys.exit()
        else: ##displays error message with menu if error = true
            sp.call('clear',shell=True)
            error = True

            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Please enter 'M', or 'X'!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")




def login_menu():
    error = False
    while True:
        if error == False:
            sp.call('clear',shell=True)
        global accounts
        account_number = input("Enter Your Account Number: ")
        if account_number in accounts.keys():
            print(f"Hello {accounts[account_number][0]}")
            return account_number
        else:
            error = True
            sp.call('clear',shell=True)

            print("----------------------")
            print("No such account exists")
            print("----------------------")
            return "ERROR"





def operations_menu(account_number):
    while True:
        error = False
        while True:
            if error == False:
                sp.call('clear',shell=True)
            print("##########################################")
            print("#                                        #")
            print("# Would you like to Deposit or Withdraw? #")
            print("#         1 --- DEPOSIT                  #")
            print("#         2 --- WITHDRAW                 #")
            print("#         3 --- VIEW BALANCE             #")
            print("#         X --- Exit                     #")
            print("#                                        #")
            print("##########################################")
            user_input = input()
            if user_input == "1":
                deposit_menu(account_number)
            elif user_input == "2":
                withdraw_menu(account_number)
            elif user_input == "3":
                balance_menu(account_number)
            elif user_input == "X" or user_input == "x":
                return
            else:
                error = True
                sp.call('clear',shell=True)

                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Please enter '1', '2' or 'X'!")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def deposit_menu(account_number):
    error = False
    while True:
        if error == False:
            sp.call('clear',shell=True)
        print("###################################################################")
        print("#                                                                 #")
        print("#      Enter amount to Deposit, or press any letter to exit:      #")
        print("#                                                                 #")
        print("###################################################################")
        deposit_input = input("Deposit: ")
        try:
            deposit_amount = float(deposit_input)
        except ValueError:
            error = True
            sp.call('clear',shell=True)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Invalid input. Returning...")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return
        if deposit_amount > 1000000 or deposit_amount < 0:
            error = True
            sp.call('clear',shell=True)
            print("!!!!!!!!!!!!!!!!!")
            print("not a valid input")
            print("!!!!!!!!!!!!!!!!!")
            return
        amount = accounts[account_number][1]
        amount += deposit_amount
        accounts[account_number][1] = amount
        f = open("accounts.json", "w")
        json.dump(accounts, f)
        f.close()
        print("+-------------------------------------------------------------+")
        print("|                                                             |")
        print("|                                                             |")
        print(f"|         Thank You for your deposit of {deposit_amount:12.2f}             |")
        print("|                                                             |")
        print("|                                                             |")
        print("+-------------------------------------------------------------+")
        input("press any key to return to operations menu: ")
        return


def withdraw_menu(account_number):
    error = False
    while True:
        if error == False:
            sp.call('clear',shell=True)
        withdraw_input = input("Enter amount to Withdraw, or press any letter to exit: ")
        try:
            withdraw_amount = float(withdraw_input)
        except ValueError:
            sp.call('clear',shell=True)
            error = True
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Invalid input. Returning...")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return
        if withdraw_amount > 1000000 or withdraw_amount < 0:
            sp.call('clear',shell=True)
            error = True
            print("!!!!!!!!!!!!!!!!!")
            print("not a valid input")
            print("!!!!!!!!!!!!!!!!!")
            return
        amount = accounts[account_number][1]
        if withdraw_amount > amount:
            sp.call('clear',shell=True)
            error = True
            print("!!!!!!!!!!!!!!!!!!")
            print("Insufficient Funds")
            print("!!!!!!!!!!!!!!!!!!")
            return
        amount -= withdraw_amount
        accounts[account_number][1] = amount
        f = open("accounts.json", "w")
        json.dump(accounts, f)
        f.close()
        print("+---------------------------------------------------------------+")
        print("|                                                               |")
        print("|                                                               |")
        print(f"|         Thank You for your withdrawal of {withdraw_amount:12.2f}         |")
        print("|                                                               |")
        print("|                                                               |")
        print("+---------------------------------------------------------------+")
        input("press any key to return to operations menu: ")
        return

def balance_menu(account_number):
    sp.call('clear',shell=True)
    amount = accounts[account_number][1]
    print("+------------------------------------------+")
    print("|                                          |")
    print("|                                          |")
    print(f"|      Your balance is {amount:12.2f}        |")
    print("|                                          |")
    print("|                                          |")
    print("+------------------------------------------+")
    input("press any key to return to operations menu: ")
    return




def main():
    global accounts
    f = open("accounts.json", "r")
    accounts = json.load(f)
    f.close()
    print(accounts)
    main_menu()


if __name__ == '__main__':
    main()
