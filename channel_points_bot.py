import pyautogui 
import keyboard

continue_session = True
while continue_session:
    pyautogui.click(2325, 1375)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('Exiting')
        continue_session = False
