import requests, json, time
from fake_useragent import UserAgent
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class gozle_disk:
    space_usage_api = 'https://disk.gozle.com.tm/api/v1/user/space-usage'


    def auth(email, password):
        driver = Driver(uc=True, headless=True)
        print('Logged in to the site')
        driver.get('https://disk.gozle.com.tm/login')
        username_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#\:r0\:')))
        password_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#\:r1\:')))
        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > main > div.rounded-lg.max-w-440.px-40.pt-40.pb-32.w-full.mx-auto.bg-paper.shadow.md\:shadow-xl > form > button')))
        username_button.send_keys(email)
        print('Sent an email')
        password_button.send_keys(password)
        print('Sent a password')
        continue_button.click()
        time.sleep(1)
        cookies = driver.get_cookies()
        with open('cookies.txt', 'w') as f:
            for cookie in cookies:
                f.write(f"{cookie['name']}={cookie['value']}\n")
        with open('data.txt', 'w', encoding='utf-8') as file:
            file.write(str(email) + '\n' + str(password))
        print('You are logged in')
        driver.quit()

    def __auth_if_outdate(email, password):
        driver = Driver(uc=True, headless=True)
        print('Logged in to the site')
        driver.get('https://disk.gozle.com.tm/login')
        username_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#\:r0\:')))
        password_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#\:r1\:')))
        continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#root > main > div.rounded-lg.max-w-440.px-40.pt-40.pb-32.w-full.mx-auto.bg-paper.shadow.md\:shadow-xl > form > button')))
        username_button.send_keys(email)
        print('Sent an email')
        password_button.send_keys(password)
        print('Sent a password')
        continue_button.click()
        time.sleep(1)
        cookies = driver.get_cookies()
        with open('cookies.txt', 'w') as f:
            for cookie in cookies:
                f.write(f"{cookie['name']}={cookie['value']}\n")
        print('You are logged in')
        driver.quit()

    def get_account_space_usage_info():
        ua = UserAgent()
        with open('cookies.txt', 'r') as f:
            lines = f.readlines()
            remember_web = lines[2].strip() + ';'
            XSRF_TOKEN = lines[1].strip() + ';'
            gozle_sessions = lines[0].strip()
            cookie = remember_web + XSRF_TOKEN + gozle_sessions

        headers = {
            "Cookie": cookie,
            "Referer": "https://disk.gozle.com.tm/drive",
            "User-Agent": ua.random
        }
        responce = requests.get(gozle_disk.space_usage_api, headers=headers)
        if responce.status_code == 403:
            try:
                print('Cookies are out of date. We begin to re-login. After this action please restart the function.')
                with open('data.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    email = lines[0]
                    password = lines[1]
                gozle_disk.__auth_if_outdate(email, password)
            except:
                pass
        else:
            print(responce.json())


    def get_info_profile(user_api):
        ua = UserAgent()
        with open('cookies.txt', 'r') as f:
            lines = f.readlines()
            remember_web = lines[2].strip() + ';'
            XSRF_TOKEN = lines[1].strip() + ';'
            gozle_sessions = lines[0].strip()
            cookie = remember_web + XSRF_TOKEN + gozle_sessions

        headers = {
            "Cookie": cookie,
            "Referer": "https://disk.gozle.com.tm/drive",
            "User-Agent": ua.random
        }
        responce = requests.get(user_api, headers=headers)
        if responce.status_code == 403:
            print('Cookies are out of date. We begin to re-login. After this action please restart the function.')
            with open('data.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                email = lines[0]
                password = lines[1]
            gozle_disk.__auth_if_outdate(email, password)
        else:
            print(responce.json())