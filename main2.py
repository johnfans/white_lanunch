import pyautogui
import win32gui
import win32con
import time
import numpy as np
import os
import tkinter as tk
import threading
import pygame

audio_paths = ['prey.wav', 'waiting.wav', 'by.wav']  # 替换为你的音频文件路径列表

# 初始化 pygame
pygame.mixer.init()

# 播放第一段音频
pygame.mixer.music.load(audio_paths[0])
pygame.mixer.music.play()
time.sleep(2.5)
pygame.mixer.music.load(audio_paths[1])
pygame.mixer.music.play(-1)



def set_window_topmost(window_title):
    while True:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0)
            print(f"成功将窗口'{window_title}'置于最顶层。")
            break
        else:
            print(f"未找到窗口'{window_title}'，等待窗口出现...")
            time.sleep(1)

def white():
    global window
    window = tk.Tk()

# 隐藏窗口标题栏
    window.overrideredirect(True)

    # 设置窗口大小为全屏
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")

    # 设置窗口背景颜色为白色
    window.configure(bg="white")

    # 将窗口置于最顶层
    window.attributes("-topmost", True)
    window.after(20000, close_window)
    window.mainloop()

def close_window():
    window.destroy()

    

def waiting(window_title):
        global window
        while True:
            hwnd = win32gui.FindWindow("UnityWndClass", window_title)
            if hwnd:
                print("launched")
                time.sleep(1)
                break
            else:
                time.sleep(0.1)
        
        start_time = time.time()
        while time.time() - start_time < 5:
            win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0, 1)
            time.sleep(0.1)
        return hwnd

white_thread=threading.Thread(target=white)

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
while True:
    # 获取屏幕截图
    screenshot = pyautogui.screenshot().convert('L')
    screenshot_array = np.array(screenshot)
    # 计算亮度均值
    brightness = np.mean(screenshot_array)

    # 如果亮度均值小于等于某个阈值，可以判断为白色
    threshold = 251
    if brightness >= threshold:
        # 执行某一命令，这里只打印了一条消息作为示例
        white_thread.start()
        time.sleep(0.2)
        pyautogui.hotkey('win', 'm')
        os.startfile('D:/Program Files/Genshin Impact/Genshin Impact Game/YuanShen.exe')
        pygame.mixer.music.load(audio_paths[2])
        pygame.mixer.music.play()
        break
    print(brightness)
    time.sleep(0.01)
time.sleep(1)
#等待ys窗口创建
hwnd=waiting("原神")

#提上ys窗口
print("break1")

print("break2")
#关闭white
print("break3")
window.attributes("-topmost",False)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 1)
window.destroy()
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 1)
print("finish")
