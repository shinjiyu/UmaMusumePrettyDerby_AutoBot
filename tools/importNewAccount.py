# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from accountManager import AccountManager , Account

account_manager = AccountManager()

ACCOUNT_DATA_PATH = "../Data/account.data";
account_manager.load_accounts(ACCOUNT_DATA_PATH);

with open('../NewData/newAccount.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if '卡号：' in line:
            data = line.split('----')
            username = data[0].split('：')[1]
            password = data[1]
            account_id = None
            device_id = None
            is_registered = None
            horse_girl_card_list = None
            account = Account(username, password, account_id, device_id, is_registered, horse_girl_card_list)
            account_manager.add_account(account)

account_manager.save_accounts(ACCOUNT_DATA_PATH)
