# -*- coding: utf-8 -*-

from deviceAgent import Device,LOGIN_TASK_NAME
import logging
import asyncio

class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def get_devices(self):
        return self.devices

    def get_device(self, device_index):
        if len(self.devices) <= device_index:
            return  None
        return self.devices[device_index]


    def add_account(self, device_index, account , pwd):
        device = self.get_device(device_index)
        if device == None:
            return False
        return device.add_account(account, pwd)


    def create_device(self,port):
        device = Device(port)
        self.add_device(device)

    def connect(self):
        for device in self.devices:
            ret = device.connect()
            logging.info("Device connection result: %s", ret)
            ret = device.get_resolution()
            logging.info("ret: %s", ret)
    

    async def start(self):
        #await asyncio.gather(*[device.run(LOGIN_TASK_NAME) for device in self.devices])
        while True:
            shouldReturn = True
            for device in self.devices:
                if device.cur_task == None:
                    device.run(LOGIN_TASK_NAME)
                #这个值也太不准了.
                elif not device.get_task_status():
                    shouldReturn = False
            
    
            await asyncio.sleep(1)
                    
    
    
            
            
