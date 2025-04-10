import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    
    login_page = LoginPage(driver)
    login_page.enter_username("admin")
    login_page.enter_password("password")
    login_page.click_login()
    
    assert "dashboard" in driver.current_url
    driver.quit()
