import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

final = ''


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()
    print(final)  # напечатать ответ про Сов в конце всей сессии

def test_authorization(browser):
    browser.get(link)
    WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, "ember33"))).click()
    email = data_load["email_stepik"]
    password = data_load["password_stepik"]
    browser.find_element(By.CSS_SELECTOR, "input#id_login_email").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "input#id_login_password").send_keys(password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой