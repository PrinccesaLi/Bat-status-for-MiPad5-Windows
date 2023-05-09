import subprocess
import time
import win32gui
import win32con
import win32api
import os
import ctypes
import configparser

# Устанавливаем заголовок окна на "Bat-status"
win32gui.SetWindowText(win32gui.GetForegroundWindow(), "Bat-status")

# Функция для сворачивания программы в трей
def minimize_to_tray(hwnd):
    # Проверяем заголовок окна
    window_title = win32gui.GetWindowText(hwnd)
    if window_title != "Bat-status":
        return
    # Скрываем окно
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    # Создаем иконку в трее
    nid = (hwnd, 0, win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP, win32con.WM_USER + 20, win32gui.LoadImage(None, "icon.ico", win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE), "Bat-status")
    win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)

# Загружаем параметры из файла config.ini
config = configparser.ConfigParser()
config.read('config-bats.ini')

# Получаем значение порога батареи из файла config.ini
THRESHOLD = int(config['Battery']['Threshold'])

# Получаем путь к ярлыку из файла config.ini
shortcut_path = config['Shortcut']['Path']

# Бесконечный цикл для мониторинга заряда батареи
while True:
    # Получаем информацию о батарее через wmic
    result = subprocess.run(['wmic', 'Path', 'Win32_Battery', 'Get', 'EstimatedChargeRemaining'], capture_output=True, text=True)
    # Извлекаем процент заряда из вывода команды
    percent = int(result.stdout.strip().split()[-1])

    # Если заряд батареи меньше заданного порога, запустите ярлык
    if percent <= THRESHOLD:
        if os.path.exists(shortcut_path):
            if os.name == "nt":
                ctypes.windll.shell32.ShellExecuteW(None, "runas", shortcut_path, None, None, 1)
            else:
                raise Exception("This program only works on Windows.")
            hwnd = win32gui.GetForegroundWindow()
            minimize_to_tray(hwnd)
        else:
            print("Label not found.")

        break

    # Сворачиваем окно в трей
    hwnd = win32gui.GetForegroundWindow()
    minimize_to_tray(hwnd)

    # Задержка между проверками заряда батареи
    time.sleep(60)
