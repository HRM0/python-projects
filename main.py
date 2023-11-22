from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
eventArray = []
eventDic = {}
# Split the text into lines
event_lines = events.text.split('\n')

# Iterate over the lines
for event in event_lines:
    eventArray.append(event)

# Populate in dictionary
for i in range(0, len(eventArray)-1, 2):
    eventDic[i] = {"time": str(eventArray[i]), "name": str(eventArray[i+1])}

print(eventDic)
#driver.close()
driver.quit()