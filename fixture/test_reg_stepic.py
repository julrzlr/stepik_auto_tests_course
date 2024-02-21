import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json


@pytest.fixture(scope="session")
def data_load():
    with open('config.json', 'r') as f:
        return json.load(f)


@pytest.fixture(scope="function")
def answer():
    return math.log(int(time.time()))

@pytest.mark.parametrize('link', [
                                "https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"
                                ]
                         )
def test_authorization(browser, data_load, link, answer):


    browser.get(link)
    WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, "ember33"))).click()
    email = data_load["email_stepik"]
    password = data_load["password_stepik"]
    browser.find_element(By.CSS_SELECTOR, "input#id_login_email").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "input#id_login_password").send_keys(password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    time.sleep(5)
    textarea = browser.find_element(By.CSS_SELECTOR, '.quiz-component textarea')

    textarea.clear()

    textarea.send_keys(answer)

    #time.sleep(10)
    WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    time.sleep(10)
    result = browser.find_element(By.CSS_SELECTOR, "div .smart-hints__hint").text
    print("!!!!", result)
    assert result == "Correct!"


