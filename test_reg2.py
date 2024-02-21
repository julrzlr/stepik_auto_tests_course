import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link',["http://suninjuly.github.io/registration1.html","http://suninjuly.github.io/registration2.html"])
def test_reg_1(browser, link):
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > .first ")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > .second")
    last_name.send_keys("Ivanov")
    last_name = browser.find_element(By.CSS_SELECTOR, ".third_class > .third")
    last_name.send_keys("q@q.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text= browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!"
