import time
import pyautogui

# Задаем время обновления в секундах
refresh_interval = 120

while True:
  # Нажимаем F5 для обновления страницы
  pyautogui.press('f5')

  # Ждем время обновления
  time.sleep(refresh_interval)
