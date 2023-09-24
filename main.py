# -*- coding: utf-8 -*-
from accountManager import AccountManager , Account
from deviceManager import DeviceManager
import logging
import asyncio
import os
log_file = os.path.join(os.getcwd(), 'log.txt')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.FileHandler(log_file, 'w', 'utf-8'), logging.StreamHandler()])


ACCOUNT_DATA_PATH = "Data/account.data";

#初始化account
account_manager = AccountManager()
account_manager.load_accounts(ACCOUNT_DATA_PATH);
logging.info("Accounts loaded from %s", ACCOUNT_DATA_PATH)
def add_account(account,pwd):
    new_account = Account(account, pwd, None, None, [])
    account_manager.add_account(new_account)
    logging.info("Account %s added", account)

account_manager.print_accounts()

#初始化device
device_manager = DeviceManager()
logging.info("Device manager initialized")

DEVICE_COUNT = 2
DEVICE_START_PORT = 16384
DEVICE_PORT_STEP = 32
for i in range(DEVICE_COUNT):
    port = DEVICE_START_PORT + i * DEVICE_PORT_STEP
    device_manager.create_device(port)
    logging.info("Device created with port %s", port)

#分配帐号
for i in range(DEVICE_COUNT):
    
    accounts = account_manager.get_accounts_by_device_id(i)
    logging.info("Accounts retrieved for device id %s", i)

    bAddSuccess = True
    for account in accounts:
        if not device_manager.add_account(i, account.username, account.password):
            bAddSuccess = False
            break
        logging.info("Account %s added to device %s", account.username, i)
    
    if not bAddSuccess:
        logging.error("Failed to add account %s with password %s to device %s", account.username, account.password, i)
        continue
    
    while True:
        account = account_manager.get_a_free_account()
        if account is None:
            break
        if not device_manager.add_account(i, account.username, account.password):
            break

        account_manager.set_account(account.username, device_id = i)
        logging.info("Free account %s added to device %s", account.username, i)
    
    account_manager.save_accounts(ACCOUNT_DATA_PATH)

device_manager.connect()

asyncio.run(device_manager.start()) 


