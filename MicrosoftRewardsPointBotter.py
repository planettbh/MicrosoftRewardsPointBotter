import pyautogui
import time
import random
import string
import os
import ctypes
import getpass
import pygetwindow as gw

new_title = "MRPB by GloryDevelopment [Version: v2.0-SNAPSHOT]"
ctypes.windll.kernel32.SetConsoleTitleW(new_title)
pool = string.ascii_letters + string.digits
os.system('cls')

print("   ________                 ____                 __                                 __ ")
print("  / ____/ /___  _______  __/ __ \___ _   _____  / /___  ____  ____ ___  ___  ____  / /_")
print(" / / __/ / __ \/ ___/ / / / / / / _ \ | / / _ \/ / __ \/ __ \/ __ `__ \/ _ \/ __ \/ __/")
print("/ /_/ / / /_/ / /  / /_/ / /_/ /  __/ |/ /  __/ / /_/ / /_/ / / / / / /  __/ / / / /_  ")
print("\____/_/\____/_/   \__, /_____/\___/|___/\___/_/\____/ .___/_/ /_/ /_/\___/_/ /_/\__/  ")
print("                  /____/                            /_/                                ")
print("")
print(" -> Welcome to Microsoft Rewards Point Botter by Glory Development.")
print(" -> Please make sure you are tabbed into Microsoft Edge.")
print(" -> Once you hit Enter, you will have 10 seconds to be tabbed into Edge.")
print("")
input(" -> Press Enter to start the bot...")
time.sleep(1)
print(gw.getActiveWindow())
time.sleep(10)

while True:
    print(gw.getActiveWindow())
    # Check if Microsoft Edge is the active window
    active_window = gw.getActiveWindow()
    if "Microsoft Edge" or "Microsoft Edge - Chromium" in active_window:
        random_string = ''.join(random.choices(pool, k=10))
        time.sleep(5)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(0.5)
        pyautogui.typewrite(random_string)
        pyautogui.hotkey('enter')
        print(" -> Searched '" + random_string + "'")
        time.sleep(7)
        pyautogui.hotkey('ctrl', 'w')
    else:
        print(" -> Microsoft Edge is not the active window. Please switch to Microsoft Edge and try again.")
        break
