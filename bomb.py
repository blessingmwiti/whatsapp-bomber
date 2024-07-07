import pyautogui as pg
import time

# Just enough time to open the WhatsApp Chat, otherwise, there will be chaos
time.sleep(8)

# Change 500 to your desired number of resending the message
for i in range(50):
    pg.write("Hello world!")
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
