import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_stepik_pytest_3_6_9(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('#add_to_basket_form [type="submit"]')
    assert button, "NO button!!!"