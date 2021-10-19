import pyperclip
import time
import pyautogui
pyperclip.copy('rtx')
pyautogui.click(457,1057)
pyautogui.moveTo(437,49)
pyautogui.doubleClick(437,49)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v') 
pyautogui.press ('enter')
