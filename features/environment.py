from webdriver_manager.chrome import ChromeDriverManager

from Logger.LogGen import LogGen

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def before_all(context):
    logger = LogGen.loggen()
    logger.info("I am inside before all")
    # browser_type = context.config.userdata.get("browser")
    # context.browser_type = browser_type


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    logger = LogGen.loggen()
    logger.info("I am inside before scenario")
    # context.driver = webdriver.get_webdriver("chrome")
    # context.driver.maximize_window()


def after_scenario(context, scenario):
    logger = LogGen.loggen()
    logger.info("I am inside after scenario")
    # context.driver.close()
