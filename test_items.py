import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Note that first you get on the catalogue page and only then on the page above
# due to config script
@pytest.mark.required
def test_bascet_button_presence(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    assert EC.presence_of_element_located((By.CSS_SELECTOR,
                                "#add_to_basket_form button")), "The button is not present"
    time.sleep(10)

@pytest.mark.optional
def test_bascet_button_to_be_clickable(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    assert EC.element_to_be_clickable((By.CSS_SELECTOR,
                                "#add_to_basket_form button")), "The button is not clickable"

@pytest.mark.optional
def test_right_language_use_en(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    element = browser.find_element(By.CSS_SELECTOR,
                                   "#product_description h2")
    assert element.text == "Product Description", "The site is not in English"

@pytest.mark.optional
def test_right_language_use_fr(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    element = browser.find_element(By.CSS_SELECTOR,
                                   ".dropdown.active a")
    assert element.text == "Parcourir le magasin", "The site is not in French"
