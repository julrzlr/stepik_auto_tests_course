import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(
        By.CSS_SELECTOR,
        "#input_value",
    )
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split()[-1])
finally:
    time.sleep(3)
    browser.quit()
