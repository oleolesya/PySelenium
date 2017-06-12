from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_google():
    driver = webdriver.Chrome()
    page = "http://localhost/litecart/admin/"
    userName = "admin"
    password = "admin"
    #driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(page)
    driver.find_element_by_name("username").send_keys(userName)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").submit
    WebDriverWait(driver, 3).until(ec.title_is ("MyStore"))
    #driver.quit()