from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('q@q.ru')

    element = browser.find_element(By.XPATH, "// input[@type = 'file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_name = "/Users/julia/Desktop/file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

