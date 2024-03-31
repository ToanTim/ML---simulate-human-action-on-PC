import time
from player import Player
import pyautogui
import sys
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
parent_folder_path = os.path.abspath(os.path.join(
    parent_directory, '..'))+"\ML---simulate-human-action-on-PC\src"
sys.path.append(parent_folder_path)


class Game:
    def __init__(self):
        self.player = Player()
        # Initialize game environment, such as screen resolution, game window coordinates, etc.

    def run(self):
        time.sleep(3)
        while True:
            self.player.enter_coordinate(104, 1130)
            """ self.player.right_click()   """
            """ print(parent_folder_path) """
            # Adjust the delay as needed to control the game loop speed
            time.sleep(3)

    def detect_game_state(self):
        # Capture screenshot of game window and process to extract relevant game state
        # For simplicity, let's assume it returns a dictionary with player position, obstacles, etc.
        return {"player_position": (100, 200), "obstacles": [(150, 220), (200, 220)]}


if __name__ == "__main__":
    game = Game()
    game.run()
