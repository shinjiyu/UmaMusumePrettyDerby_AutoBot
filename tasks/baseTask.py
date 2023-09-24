# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
import asyncio
import logging


class BaseTask:
    def __init__(self, name):
        self.task_name = name
        self.work_space = ""
        self.device_width = 0
        self.device_height = 0
        self.port = 0

    def set_workspace(self, workspace):
        if not os.path.exists(workspace):
            os.makedirs(workspace)
        self.work_space = workspace

    def set_port(self, port):
        self.port = port

    def set_solution(self, width, height):
        self.device_width = width
        self.device_height = height

    def set_account(self, user_name, password):
        self.user_name = user_name
        self.pwd = password

    def run_cmd(self, cmd):
        logging.info(f"cmd: {cmd}")
        result = os.popen(cmd).read()
        logging.info(f"result: {result}")

    async def adb_input_string(self, string, delay):
        cmd = f"adb -s 127.0.0.1:{self.port} shell input text {string}"
        self.run_cmd(cmd)
        await asyncio.sleep(delay)

    async def adb_click(self, x, y, delay):
        cmd = f"adb -s 127.0.0.1:{self.port} shell input tap {x} {y}"
        self.run_cmd(cmd)
        await asyncio.sleep(delay)

    async def adb_click_anywhere(self, delay):
        await self.adb_click(self.device_width/2, self.device_height/2, delay)

    async def adb_screenshot(self, filename):
        cmd = f"adb -s 127.0.0.1:{self.port} shell screencap -p /sdcard/{filename}"
        self.run_cmd(cmd)
        cmd = f"adb -s 127.0.0.1:{self.port} pull /sdcard/{filename} {self.work_space}/{filename}"
        self.run_cmd(cmd)
        await asyncio.sleep(1)

    def save_image_as_b(self, img_a_path, img_b_path):
        # Load the image
        img_a = cv2.imread(f"{self.work_space}/{img_a_path}")

        # Check if image is loaded properly
        if img_a is None:
            return None

        # Save the image as B
        cv2.imwrite(f"{self.work_space}/{img_b_path}", img_a)

    def find_image_position(self, img_a_path, img_b_path):

        # Load the images
        img_a = cv2.imread(f"{self.work_space}/{img_a_path}", 0)
        img_b = cv2.imread(img_b_path, 0)

        # Check if images are loaded properly
        if img_a is None or img_b is None:
            return None

        logging.info("[shinjiyu] 1")
        # Check for similarities between the two images
        res = cv2.matchTemplate(img_a, img_b, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8

        
        logging.info("[shinjiyu] 2")
        # Store the coordinates of matched area in a numpy array
        loc = np.where(res >= threshold)


        
        logging.info("[shinjiyu] 3")
        # If no match is found, raise an exception
        if len(loc[0]) == 0:
            return None


        
        logging.info("[shinjiyu] 4")
        # The function should return the top-left corner of the matched region
        return loc[0][0], loc[1][0]
