# -*- coding: utf-8 -*-

import logging
import asyncio
from .baseTask import BaseTask

class LoginTask(BaseTask):
    def __init__(self, name):
        super().__init__(name)

    async def start(self):
        await self.adb_click_anywhere(3)

        await self.adb_click(453, 923 , 1)
        #同意协议
        await self.adb_click(266, 957, 1)
        #B站登陆
        await self.adb_click(454, 899, 1)
        #用户名
        await self.adb_click(331, 723, 1)
        await self.adb_input_string(self.user_name, 1)

        #密码
        await self.adb_click(356, 815, 1)
        await self.adb_input_string(self.pwd, 1)

        #登陆
        await self.adb_click(465, 979, 5)

        #人工打码
        #失败了反正不需要重新输入

        i = 0
        while True:
            tmpPath = f"tmp{i}.png"
            await self.adb_screenshot(tmpPath)
            # 尝试在tmp.png上查找 workspace/database/qiehuanzhanghao.png
            qhzh = self.find_image_position(tmpPath, "workspace/database/qiehuanzhanghao.png")
            if not qhzh == None:
                self.save_image_as_b(tmpPath,"zhanghao.png")
                break 

            i = i + 1
            await asyncio.sleep(0.5)

        
        

        





        
    
