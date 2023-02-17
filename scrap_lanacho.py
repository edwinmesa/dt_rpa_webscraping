from RPA.Desktop.Windows import Windows
from RPA.Desktop import Desktop
import pyautogui
import mouse
from rich.pretty import pprint
from rich.progress import Progress
from rich.progress import track
import time as t

windows = Windows()
desktop = Desktop()


def process_data():
    t.sleep(0.03)

def key_down(key_down):
    i = 0
    while i <= key_down:
        key1 = desktop.press_keys("down")
        i += 1
        t.sleep(0.03)

def drag_categoryMenu():
    t.sleep(2)
    mouse.move(190, 340)
    print(mouse.get_position())
    mouse.press(button='left')
    mouse.drag(340, 330, 20, 340, duration=1)

def process_track(process):
    for _ in track(range(100), description=f'[green]Iniciando Scraping... {process}'):
        process_data()

def navigate_to_shoop(coord_x, coord_y, message):
    click = windows.mouse_click_coords(coord_x, coord_y, "click", 5.0)
    process_track(message)

def navigate_to_category(coord_x, coord_y, message, down):
    process_track(message)
    click = windows.mouse_click_coords(coord_x, coord_y, "click", 5.0)
    key_down(down)

def navigate_to_back(coord_x, coord_y, message):
    process_track(message)
    click = windows.mouse_click_coords(coord_x, coord_y, "click", 5.0)


categories = {'Whisky':'85,360', 'Tequila': '200, 360', 'Ron':'310, 360', 'Cerveza':'200, 480', 'Vino': '85,360'}

navigate_to_shoop(250, 230, "La Nacho") #  1

navigate_to_category(75, 265, "Wisky", 300)

navigate_to_back(25, 110, "En Otra Categoria") 

drag_categoryMenu()


