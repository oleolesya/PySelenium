#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_google():
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 3).until(ec.title_is ("webdriver - Пошук Google"))
    driver.quit()