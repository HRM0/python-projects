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
    grandma = driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b')
    factory = driver.find_element(By.CSS_SELECTOR, value='#buyFactory b')
    mine = driver.find_element(By.CSS_SELECTOR, value='#buyMine b')
    shipment = driver.find_element(By.CSS_SELECTOR, value='#buyShipment b')
    alchemy = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
    portal = driver.find_element(By.CSS_SELECTOR, value='#buyPortal b')
    time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
    prices["cursor"] = {"obj": cursor, "price": int(cursor.text.split()[-1].replace(",", "")), "amount": 1}
    prices["grandma"] = {"obj": grandma, "price": int(grandma.text.split()[-1].replace(",", "")), "amount": 5}
    prices["factory"] = {"obj": factory, "price": int(factory.text.split()[-1].replace(",", "")), "amount": 20}
    prices["mine"] = {"obj": mine, "price": int(mine.text.split()[-1].replace(",", "")), "amount": 50}
    prices["shipment"] = {"obj": shipment, "price": int(shipment.text.split()[-1].replace(",", "")), "amount": 100}
    prices["alchemy"] = {"obj": alchemy, "price": int(alchemy.text.split()[-1].replace(",", "")), "amount": 500}
    prices["portal"] = {"obj": portal, "price": int(portal.text.split()[-1].replace(",", "")), "amount": 10000}
    prices["time_machine"] = {"obj": time_machine,
                              "price": int(time_machine.text.split()[-1].replace(",", "")),
                              "amount": 20000}
    return prices


def check_to_buy():
    money = int(driver.find_element(By.ID, value='money').text.replace(",", ""))
    item_to_buy = {"obj": "blank", "price": float('inf'), "amount": 1}
    item_list = getPrices()
    for item_name, item_info in item_list.items():
        ratio = item_info["price"]/item_info["amount"]
        curr_ratio = item_to_buy["price"]/item_to_buy["amount"]
        if ratio < curr_ratio and item_info["price"] < (money*1.75):
            item_to_buy = item_info
    if item_to_buy["price"] < money and item_to_buy["obj"] != "blank":
        item_to_buy["obj"].click()


interval = .01
numberOfLoops = 0.0
while True:
    cookie.click()
    numberOfLoops += 1
    if numberOfLoops % 50 == 0:
        check_to_buy()
    time.sleep(interval)


