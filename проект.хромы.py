import pyautogui
import time
import pyperclip
name=input("Введите запрос")
num=int(input("Номер вкладки.небольше 5"))
chrom=input("Выберите : google, yandex , firefox.")
pyperclip.copy(name)
if chrom=="google":
    pyautogui.moveTo(401,1055)
    pyautogui.doubleClick(401,1055)
    if num==5:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
    elif num==4:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
    elif num==3:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
    elif num==2:
        pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    pyautogui.press ('enter')
elif chrom=="yandex":
    pyautogui.moveTo(579,1050)
    pyautogui.doubleClick(579,1050)
    time.sleep(3)
    if num==5:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
    elif num==4:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
    elif num==3:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('1')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
    elif num==2:
        pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'v') 
    pyautogui.press ('enter')
elif chrom=="firefox":
    pyautogui.moveTo(209,1055)
    pyautogui.doubleClick(209,1055)
    time.sleep(3)
    if num==5:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
    elif num==4:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 't')
    elif num==3:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 't')
    elif num==2:
        pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    pyautogui.press ('enter')