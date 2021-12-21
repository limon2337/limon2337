import pyautogui
import time
import pyperclip
n=int(input("Номер вкладки.небольше 9"))
pyautogui.moveTo(401,1055)
pyautogui.doubleClick(401,1055)
time.sleep(1)
for step in range(1,n):
    pyautogui.hotkey('ctrl', 't')