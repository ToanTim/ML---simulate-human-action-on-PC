import pyautogui as au
import time
from BaseVariable import *

GAME_COMMAND = [
    {
        "position": "top_left",
        "coordinates": {"x": 323, "y": 193}
    },
    {
        "position": "top_right",
        "coordinates": {"x": 1596, "y": 193}
    },
    {
        "position": "bottom_left",
        "coordinates": {"x": 322, "y": 904}
    },
    {
        "position": "bottom_right",
        "coordinates": {"x": 1598, "y": 908}
    }
]


def whereNotRun():
    for frame in BASE_GAME_FRAME:
        position = frame["position"]
        coordinates = frame["coordinates"]
        print(
            f"Position: {position}, Coordinates: x={coordinates['x']}, y={coordinates['y']}")
        au.moveTo(coordinates['x'], coordinates['y'], 2)


x = 0

while x == 0:
    time.sleep(3)
    """ print(pyautogui.size()) """
    print(au.position())
    """ au.press("F5")
    x = 1 """
    """ au.press("left")
    au.click(100, 100, 3, 3, button="left") """
