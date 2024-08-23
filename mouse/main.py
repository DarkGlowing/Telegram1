import pyautogui
import random
import time

# Получаем размеры экрана
screen_width, screen_height = pyautogui.size()

def move_mouse_randomly():
    while True:
        # Генерация случайных координат
        random_x = random.randint(0, screen_width - 1)
        random_y = random.randint(0, screen_height - 1)
        
        # Перемещение мышки на случайные координаты
        pyautogui.moveTo(random_x, random_y, duration=0.5)  # duration - время перемещения в секундах
        
        # Пауза перед следующим перемещением
        time.sleep(1)  # пауза в 1 секунду

if __name__ == "__main__":
    try:
        move_mouse_randomly()
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")
