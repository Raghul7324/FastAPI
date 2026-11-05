import pyautogui
import pyperclip
import time
from datetime import datetime
from openpyxl import Workbook
import pyscreeze



pyautogui.FAILSAFE = True  # Enable fail-safe feature

# Open browser and go to any public website 
pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)
pyautogui.typewrite('https://www.screener.in/')  # Type 'screener' in the Run dialog
time.sleep(1)
pyautogui.press('enter')  # Press Enter to open the website
time.sleep(2)
pyautogui.typewrite('jio')  # Type 'jio' in the search bar
time.sleep(1)
pyautogui.press('enter')  # Press Enter to search for 'jio'
time.sleep(2)

#Copy the important piece of information from the page
pyautogui.hotkey('ctrl', 'a')  # Select all text on the page
time.sleep(1)   
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text
time.sleep(1)
stock_data = pyperclip.paste() #hotkeys return none, so we use pyperclip to get the copied text
pyautogui.hotkey('ctrl', 'w')  # Close the browser tab

# Create a new Excel workbook and add a sheet
workbook = Workbook()
sheet = workbook.active
sheet_title = "Stock Data"
sheet.append(["Date & Time", "Stock Data", "Comment"])  # Add headers to the sheet
file_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_date = datetime.now().strftime("%Y-%m-%d")
sheet.append([file_timestamp, stock_data, "Jio stock price"])  # Add data to the sheet
pyautogui.screenshot(f"daily_stock_price_{file_date}.png")  # Take a screenshot and save it with the current date
workbook.save(f"daily_stock_price_{file_date}.xlsx")  # Save the workbook

