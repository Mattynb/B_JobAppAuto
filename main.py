from time import sleep
from selenium import webdriver
from gui import GUI
from login import login
from find_jobs import find_job
from selenium.webdriver.firefox.options import Options

def main():
    # Options
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--single-process')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.set_capability('moz:firefoxOptions', {'headless': False})  # run in headless mode
    options.set_capability('dom.webdriver.enabled', False)  # disable WebDriver API
    options.set_capability('useAutomationExtension', False)  # disable automation extension

    # input login credentials
    email, password, phone = GUI()

    # start driver with options
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.linkedin.com/feed")
    sleep(2)

    # make sure youre signed in
    if driver.current_url != "https://www.linkedin.com/feed":
        login(driver, email, password)
    sleep(14)

    find_job(driver, phone)

    # close the driver once its done
    driver.quit()


if __name__ == '__main__':
    main()