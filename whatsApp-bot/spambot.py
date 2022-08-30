import pyautogui as pg
import time

time.sleep(10)

txt = open('whatsApp-bot/bot-fake-messages.txt','r')

a ="                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')
