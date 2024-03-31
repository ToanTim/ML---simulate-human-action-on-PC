import pyautogui
from datetime import datetime
from utils import print_action
from BaseVariable import *


class Player:
    def __init__(self):
        # Initialize player parameters, such as jump power, movement speed, etc.
        pass

    def update(self, game_state):
        player_position = game_state["player_position"]
        obstacles = game_state["obstacles"]

        # Perform actions based on game state
        if self.is_obstacle_ahead(player_position, obstacles):
            self.jump()
        else:
            self.move_right()

    def press_keyboard(self, keyItem):
        # Simulate jump action
        pyautogui.press(keyItem)
        print_action(f"Press keyboard: {keyItem}")

    def right_click(self):
        # Simulate jump action
        pyautogui.rightClick()
        print_action("right click")

    def left_click(self):
        # Simulate jump action
        pyautogui.leftClick()
        print_action("left click")

    def move_to(self, x, y):
        # Simulate moving the pointer to the specified position
        pyautogui.moveTo(x, y, 2)
        print_action(f"Move to ({x}, {y})")

    def select_building(self, building_name):
        # Simulate selecting a building on the screen
        print_action(f"Selected building: {building_name}")

    def train_troops(self, troop_type, quantity):
        # Simulate training troops in the selected building
        print_action(f"Trained {quantity} {troop_type}")

    def gather_resources(self, resource_type, location):
        # Simulate gathering resources at the specified location
        print_action(f"Gathered {resource_type} at {location}")

    def enter_coordinate(self, xInput, yInput):
        for item in ENTER_COORDINATE:
            position = item["position"]
            x = item["coordinates"]["x"]
            y = item["coordinates"]["y"]
            self.move_to(x, y)
            self.left_click()
            if (position == "bar_x"):
                pyautogui.typewrite(f"{xInput}")

            if (position == "bar_y"):
                pyautogui.typewrite(f"{yInput}")

        # Simulate gathering resources at the specified location
        print_action(f"enter_coordinate start {x} at {y}")
