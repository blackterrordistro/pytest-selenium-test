import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize the WebDriver instance
    driver = webdriver.Chrome() 
    yield driver

    driver.quit()

def test_title(browser):

    browser.get('https://www.exante.eu')


    assert browser.title == "Exante Domain"

def test_search_functionality(browser):
    browser.get('https://www.exante.eu')


def test_page_content(browser):
    browser.get('https://www.exante.eu')

    assert "Welcome to Example Domain" in browser.page_source
    assert "This domain is for use in illustrative examples" in browser.page_source

def test_form_submission(browser):
    browser.get('https://exante.eu/ru/company/contact_us/')

   
    name_input = browser.find_element_by_name('name')
    email_input = browser.find_element_by_name('email')
    message_input = browser.find_element_by_name('message')
    submit_button = browser.find_element_by_css_selector('input[type="submit"]')

    name_input.send_keys("QA Engineer")
    email_input.send_keys("test@example.com")
    message_input.send_keys("Some test message.")
    submit_button.click()

