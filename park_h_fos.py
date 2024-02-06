from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    link = "https://demo:demo@mozdrav.dev.redramka.ru/clinics/park-health-tsentr-sovremennoy-meditsiny/"
    browser = webdriver.Chrome()
    browser.get(link)

    btn_open = browser.find_element(By.CSS_SELECTOR, ".clinic-map-card__body  .primary-button__content")
    btn_open.click()
    time.sleep(1)
    name = browser.find_element(By.CSS_SELECTOR, ".j-err_requestCallForm_name .custom-input__value")
    name.send_keys("Ivan")
    phone = browser.find_element(By.CSS_SELECTOR, ".j-err_requestCallForm_phone .custom-input__value")
    phone.send_keys("1234567890")
    agreement = browser.find_element(By.CSS_SELECTOR, "#requestCallForm .checkbox")
    agreement.click()

    btn_send = browser.find_element(By.CSS_SELECTOR, ".popup-form__button > .j-button-click")
    btn_send.click()
    time.sleep(5)
    success_text_elem = browser.find_element(By.CSS_SELECTOR, ".j-request-call .j-popup-form-success h3")
    success_text = success_text_elem.text

    assert "Заявка принята" == success_text

finally:
    time.sleep(1)
    browser.quit()

