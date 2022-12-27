import time
from selenium import webdriver

def login(driver, email, password): 
    # Next, you will need to open the web page containing the form you want to fill out:
    driver.get("https://www.linkedin.com/login")

    time.sleep(3)

    # Find the form and fill it out:
    username_field = driver.find_element("id","username")
    username_field.send_keys(email)

    password_field = driver.find_element("id", "password")
    password_field.send_keys(password)

    # click sign in 
    login_button = driver.find_element("xpath", '/html/body/div/main/div[3]/div[1]/form/div[3]/button')
    login_button.click()

    # Wait for the login process to complete (you may need to adjust this value)
    time.sleep(3)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    login()
    driver.close()