import pystray
import sys
import threading
import subprocess
import os
from PIL import Image
from playsound import playsound
import psutil
import time
# 创建系统托盘图标
def create_tray_icon():
    # 从图片文件中加载图标
    image = Image.open("pipe.png")

    # 创建系统托盘菜单
    menu = (
        pystray.MenuItem("开发中...", lambda: open_app()),
        # TODO tk菜单
        pystray.MenuItem("退出", lambda: exit_app())
    )

    # 创建系统托盘图标
    tray_icon = pystray.Icon("app_name", image, "Pipe-Patch", menu)

    # 设置图标的提示文本
    tray_icon.tooltip = "Pipe-Patch"

    # 显示系统托盘图标
    tray_icon.run()

# 点击“打开应用”菜单项的事件处理函数
def open_app():
    # TODO: 打开应用的具体逻辑
    pass

# 点击“退出”菜单项的事件处理函数
def exit_app():
    # TODO: 退出应用的具体逻辑
    os._exit(0)

def is_explorer_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'explorer.exe':
            return True
    return False


def selove():
    flag = 0
    while True:
        if flag == 0:
            if is_explorer_running() == False:
                playsound('pipe.mp3')
                flag = 1
        else:
            if is_explorer_running() == True:
                flag = 0
        time.sleep(2)



if __name__ == "__main__":
    thread1 = threading.Thread(target=create_tray_icon)
    thread2 = threading.Thread(target=selove)
    thread2.start()
    thread1.start()

