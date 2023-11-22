from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value='cookie')
cursor = driver.find_element(By.CSS_SELECTOR, value='#buyCursor b')
grandma = driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b')
factory = driver.find_element(By.CSS_SELECTOR, value='#buyFactory b')
mine = driver.find_element(By.CSS_SELECTOR, value='#buyMine b')
shipment = driver.find_element(By.CSS_SELECTOR, value='#buyShipment b')
alchemy = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
portal = driver.find_element(By.CSS_SELECTOR, value='#buyPortal b')
time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')

prices = {}
def getPrices():
    cursor = driver.find_element(By.CSS_SELECTOR, value='#buyCursor b')
    print(int(cursor.text.split()[-1].replace(",", "")))
    grandma = driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b')
    factory = driver.find_element(By.CSS_SELECTOR, value='#buyFactory b')
    mine = driver.find_element(By.CSS_SELECTOR, value='#buyMine b')
    shipment = driver.find_element(By.CSS_SELECTOR, value='#buyShipment b')
    alchemy = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
    portal = driver.find_element(By.CSS_SELECTOR, value='#buyPortal b')
    time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
    prices["cursor"] = {"obj": cursor, "price": int(cursor.text.split()[-1].replace(",", ""))}
    prices["grandma"] = {"obj": grandma, "price": int(grandma.text.split()[-1].replace(",", ""))}
    prices["factory"] = {"obj": factory, "price": int(factory.text.split()[-1].replace(",", ""))}
    prices["mine"] = {"obj": mine, "price": int(mine.text.split()[-1].replace(",", ""))}
    prices["shipment"] = {"obj": shipment, "price": int(shipment.text.split()[-1].replace(",", ""))}
    prices["alchemy"] = {"obj": alchemy, "price": int(alchemy.text.split()[-1].replace(",", ""))}
    prices["portal"] = {"obj": portal, "price": int(portal.text.split()[-1].replace(",", ""))}
    prices["time_machine"] = {"obj": time_machine, "price": int(time_machine.text.split()[-1].replace(",", ""))}
    print(prices)
    min_key = min(prices, key=lambda k: prices[k]["price"])
    print(prices[min_key])
    return prices


def check_to_buy():
    money = driver.find_element(By.ID, value='money')
    cheapest_item = getPrices()
    if int(money.text) > cheapest_item["price"]:
        cheapest_item["obj"].click()


interval = .05
numberOfLoops = 0.0
while True:
    cookie.click()
    numberOfLoops += 1
    if numberOfLoops % 20 == 0:
        check_to_buy()
    time.sleep(interval)


