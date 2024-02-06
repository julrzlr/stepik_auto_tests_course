import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    book = browser.find_element(By.ID, "book")
    book.click()

    x_element = browser.find_element(
        By.CSS_SELECTOR, "#input_value"
    )
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split()[-1])

finally:
    time.sleep(10)
    browser.quit()
