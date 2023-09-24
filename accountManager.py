# -*- coding: utf-8 -*-

import pickle

class Account:
    def __init__(self, username, password, device_id, is_registered, horse_girl_card_list):
        self.username = username
        self.password = password
        self.device_id = device_id
        self.is_registered = is_registered
        self.horse_girl_card_list = horse_girl_card_list


class AccountManager:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, account):
        if not any(acc.username == account.username for acc in self.accounts):
            self.accounts.append(account)
            return True
        else:
            return False

    def save_accounts(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.accounts, f)


    def load_accounts(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.accounts = pickle.load(f)
        except FileNotFoundError:
            pass

    def get_account(self, username):
        for account in self.accounts:
            if account.username == username:
                return account
        return None

    def set_account(self, username, password=None, device_id=None, is_registered=None, horse_girl_card_list=None):
        account = self.get_account(username)
        if account is not None:
            if password is not None:
                account.password = password
            if device_id is not None:
                account.device_id = device_id
            if is_registered is not None:
                account.is_registered = is_registered
            if horse_girl_card_list is not None:
                account.horse_girl_card_list = horse_girl_card_list
        else:
            account = Account(username, password, device_id, is_registered, horse_girl_card_list)
            self.accounts.append(account)
    
    def get_accounts_by_device_id(self, device_id):
        return [account for account in self.accounts if account.device_id == device_id and (account.is_registered is False or account.is_registered is None)]
    

    def get_a_free_account(self):
        for account in self.accounts:
            if account.device_id is None:
                return account
        return None
            
    
    def print_accounts(self):
        for account in self.accounts:
            print(f"Username: {account.username}, Password: {account.password}, Device ID: {account.device_id}, Registered: {account.is_registered}, Horse Girl Card List: {account.horse_girl_card_list}")
    

