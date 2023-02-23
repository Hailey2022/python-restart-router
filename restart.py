from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(300)
    driver.get("http://192.168.1.1")
    while True:
        password = driver.find_element(by=By.ID, value="userpassword_ctrl")  # noqa
        password.send_keys("password")
        password.send_keys(Keys.RETURN)
        restart = driver.find_element(by=By.CLASS_NAME, value="resstart")  # noqa
        restart.click()
        restart = driver.find_element(by=By.ID, value="content_device_rebootnoticecontinue")  # noqa
        restart.click()
        # time.sleep(200)

    # driver.close()


if __name__ == '__main__':
    main()
