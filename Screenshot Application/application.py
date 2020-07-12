import time
import pyautogui
import tkinter as tk


def screenshot():
    win.wm_state('iconic') #to minimize the tkinter gui 
    time.sleep(0.5)
    name = str(time.time())[-4:]
    name = f'{name}.png'
    img = pyautogui.screenshot(name)
    label = tk.Label(win,text = f'Screenshot Saved')
    label.grid(row = 1,column = 1)
    img.show()

win = tk.Tk()
win.geometry('300x150')

b1 = tk.Button(win,text = 'Take Screenshot',command = screenshot)
b1.grid(row = 2,column = 1)

b2 = tk.Button(win,text = 'Quit Application',command = quit)
b2.grid(row = 2,column = 2)

win.mainloop()
