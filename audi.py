import pygame
import time

audio_paths = ['prey.wav', 'waiting.wav', 'by.wav']  # 替换为你的音频文件路径列表

# 初始化 pygame
pygame.mixer.init()

# 播放第一段音频
pygame.mixer.music.load(audio_paths[0])
pygame.mixer.music.play()
time.sleep(2.5)
pygame.mixer.music.load(audio_paths[1])
pygame.mixer.music.play()
pygame.mixer.music.queue(audio_paths[2])
pygame.mixer.music.play()
while True:
    continue






