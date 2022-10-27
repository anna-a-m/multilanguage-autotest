from selenium import webdriver
from selenium.webdriver.common.by import By
import time


LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    languages = browser.find_elements(By.CSS_SELECTOR, "#language_selector option")
    languages_dict = {l.text: l.get_attribute("value") for l in languages
                      if l.text}
    with open("lang_dict.txt", "w", encoding='utf-8') as file:
        lang_dict_to_str = str(languages_dict)[1:-1]
        lang_dict_to_str = lang_dict_to_str.replace(", ", ",\n")
        file.write(lang_dict_to_str)
finally:
    time.sleep(5)
    browser.quit()
