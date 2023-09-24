# -*- coding: utf-8 -*-


import asyncio
import os

from tasks.login import LoginTask

MAX_ACCOUNT_COUNT = 7

LOGIN_TASK_NAME = "loginTask"


class Device:
    def __init__(self, port):
        self.port = port
        self.cur_account = 0
        self.accounts = []
        self.device_width = 0
        self.device_height = 0
        self.task_map = {}
        self.cur_task_name = ""
        self.cur_task = None

    def initialTasks(self):
        loginTask = LoginTask(LOGIN_TASK_NAME);
        loginTask.set_account(self.accounts[0]['account'],self.accounts[0]['pwd'])
        self.addTask(loginTask)

    def addTask(self, task):
        task.set_workspace(f"workspace/{self.port}")
        task.set_solution(self.device_width, self.device_height)
        task.set_port(self.port)

        self.task_map[task.task_name] = task

    def add_account(self, account, pwd):
        if len(self.accounts) >= MAX_ACCOUNT_COUNT:
            return False
        self.accounts.append({'account': account, 'pwd': pwd})
        if len(self.accounts) == 1:
            self.cur_account = account
        return True

    def get_account_index(self, account):
        for i, acc in enumerate(self.accounts):
            if acc['account'] == account:
                return i
        return None

    async def async_task(self):
        task = self.task_map.get(self.cur_task_name)
        if task:
            await task.start()

    def run(self, task_name):
        self.cur_task_name = task_name
        self.cur_task = asyncio.create_task(self.async_task())

    async def finished(self):
        await self.cur_task

    def get_task_status(self):
        return self.cur_task.done()

    def connect(self):
        cmd = f"adb connect 127.0.0.1:{self.port}"
        result = os.popen(cmd).read()
        self.device_width, self.device_height = self.get_resolution()
        self.initialTasks()
        return result

    def get_resolution(self):
        cmd = f"adb -s 127.0.0.1:{self.port} shell  wm size"
        result = os.popen(cmd).read()
        result = result.strip().split(" ")[-1]
        width, height = result.split("x")
        return int(width), int(height)

