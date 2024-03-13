import time
import keyboard
import win32api, win32con

def add_hotkey():
    keyboard.add_hotkey('alt+p', toggle, suppress = True, trigger_on_release = True)

def toggle():
    global is_Activated
    if is_Activated:
        print('Deactivated')
    else:
        print('Activated')
    is_Activated = not is_Activated

def fast_left_click():
    if is_Activated == True:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

is_Activated = False

add_hotkey()

while True:
    fast_left_click()