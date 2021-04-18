# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 23:25:22 2021

@author: guill
"""

from selenium import webdriver


if __name__ == '__main__':
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--ignore-ssl-errors=yes')
    chromeOptions.add_argument('--ignore-certificate-errors')
    preferences = {"download.default_directory": "./"}
    chromeOptions.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome("chromedriver.exe",options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
    driver.get("https://www.youtube.com/watch?v=2lAe1cqCOXo")
    driver.find_elements_by_css_selector('.VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc IIdkle').click()
    