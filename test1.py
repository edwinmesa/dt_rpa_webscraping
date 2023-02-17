from RPA.Desktop.Windows import Windows
from RPA.Desktop import Desktop
win = Windows()
desktop = Desktop()
import time


def ClickNacho():
    click1 = win.mouse_click_coords(274, 207,"click", 5.0)
    click2 = win.mouse_click_coords(90, 355,"click", 5.0)
    click3 = win.mouse_click_coords(30, 266,"click", 5.0)
    i = 0
    while i <= 50:
        key1   = desktop.press_keys("down")
        i += 1
        time.sleep(0.5)
ClickNacho()  