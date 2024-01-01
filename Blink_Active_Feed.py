## in the right half of the screen
continue_button_x_value = 1915
##########################################
continue_button_y_value = 744
##########################################
continue_button_red_value = 23
##########################################
continue_button_green_value = 8
##########################################
continue_button_blue_value = 4
##########################################
play_button_x_value = 1918
##########################################
play_button_y_value = 450
##########################################
play_button_red_value = 25
##########################################
play_button_green_value = 9
##########################################
play_button_blue_value = 5
##########################################
# Do not touch below text unless you know what you are doing! #
##########################################


import time
import pyautogui

while True:
    continueButton = pyautogui.pixelMatchesColor(continue_button_x_value, continue_button_y_value, (continue_button_red_value, continue_button_green_value, continue_button_blue_value))
    playButton = pyautogui.pixelMatchesColor(play_button_x_value, play_button_y_value, (play_button_red_value, play_button_green_value, play_button_blue_value))
    if continueButton == True:
        pyautogui.click(continue_button_x_value, continue_button_y_value)
    elif playButton == True:
        pyautogui.click(play_button_x_value, play_button_y_value)
    else:
       time.sleep(5)
