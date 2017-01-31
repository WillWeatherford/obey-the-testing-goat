"""Functional tests for the Goat web app."""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

FIREFOX_PATH = '/home/will/firefox'


browser = webdriver.Firefox(
    firefox_binary=FirefoxBinary(firefox_path=FIREFOX_PATH)
)

browser.get('http://localhost:8000')

assert 'Django' in browser.title
