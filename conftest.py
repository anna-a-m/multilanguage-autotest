import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


# first we get info about all available languages
# they were written to .txt file in script 'get_language_dict.py'
DIR = '\\'.join(__file__.split('\\')[:-1]) + '\\'
with open(DIR + "lang_dict.txt", encoding='utf-8') as file:
    CONTAINS = file.read()
    LANG_DICT = {re.findall(r': \'(.+)\'', c)[0]:
                 re.findall(r'\'(.+)\':', c)[0]
                 for c in CONTAINS.split('\n')}


def pytest_addoption(parser):
    """Add parameters browser_name and language to config"""
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help=f"Choose language from dict\n{{{CONTAINS}}}\nNote that item is the argument")

def set_language(browser, lang):
    """Change language on the site by choosing it from list
    Args:
        browser - selenium.webdriver
        lang - str - short name of language chosen
    Returns:
        browser - selenium.webdriver
    (help function)
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    browser.get(link)
    option_lang = browser.find_element(By.CSS_SELECTOR,
                                f'#language_selector option[value="{lang}"]')
    option_lang.click()
    button = browser.find_element(By.CSS_SELECTOR, "#language_selector button")
    button.click()
    return browser

@pytest.fixture(scope="function")
def browser(request):
    """Pytest fixture:
    1. Choose browser and open it
    2. Choose language
    3. Quit browser
    """
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    if browser and language in LANG_DICT:
         browser = set_language(browser, language)
    elif language not in LANG_DICT:
        raise pytest.UsageError(f'--language should be one of the following dict items\n{{{CONTAINS}}}')
    yield browser
    browser.quit()

