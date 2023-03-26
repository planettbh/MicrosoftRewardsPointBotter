import pyautogui
import time
import random
import string
import colorama
import os
import ctypes
import getpass
from colorama import Fore, Style

new_title = "MRPB by GloryDevelopment [Version: v2.0-SNAPSHOT]"

username = getpass.getuser()
ctypes.windll.kernel32.SetConsoleTitleW(new_title)
colorama.init()

pool = string.ascii_letters + string.digits
colors = [Fore.RED, Fore.CYAN, Fore.WHITE]
color_index = 0

os.system('cls')
print("   ________                 ____                 __                                 __ ")
print("  / ____/ /___  _______  __/ __ \___ _   _____  / /___  ____  ____ ___  ___  ____  / /_")
print(" / / __/ / __ \/ ___/ / / / / / / _ \ | / / _ \/ / __ \/ __ \/ __ `__ \/ _ \/ __ \/ __/")
print("/ /_/ / / /_/ / /  / /_/ / /_/ /  __/ |/ /  __/ / /_/ / /_/ / / / / / /  __/ / / / /_  ")
print("\____/_/\____/_/   \__, /_____/\___/|___/\___/_/\____/ .___/_/ /_/ /_/\___/_/ /_/\__/  ")
print("                  /____/                            /_/                               ")
print("")
print(" -> Welcome to Microsoft Rewards Point Botter by Glory Development, " + username + ".")
print(" -> Please tab into your browser.")
print("")

while True:
    random_string = ''.join(random.choices(pool, k=10))

    time.sleep(5)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.5)
    pyautogui.typewrite(random_string)
    pyautogui.hotkey('enter')

    message = "(Bot) Successfully searched '" + random_string + "' and received 5 points!"
    for line in message.split('\n'):
        color = colors[color_index]
        print(color + line, flush=True)
        color_index = (color_index + 1) % len(colors)
        time.sleep(0.05)
    print(Style.RESET_ALL)

    # Close tab for RAM
    time.sleep(7)
    pyautogui.hotkey('ctrl', 'w')
