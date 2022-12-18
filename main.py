import os
import time
# from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import winsound
import undetected_chromedriver as uc


def init_webdriver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Режим без интерфейса
    # chrome_options.add_argument("--start-maximized")
    #в режиме headless без user-agent не загружает страницу
    # chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    #                             "like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    # self.driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)

    # ls = ['--remote-debugging-host=127.0.0.1', '--remote-debugging-port=59417',
    #       '--user-data-dir=C:\\Users\\user\\AppData\\Local\\Temp\\tmp4zf_5ca2', '--lang=ru-RU',
    #       '--no-default-browser-check', '--no-first-run', '--log-level=0']
    # chrome_options.add_argument(ls[0])
    # chrome_options.add_argument(ls[1])
    # chrome_options.add_argument(ls[2])
    # chrome_options.add_argument(ls[3])
    # chrome_options.add_argument(ls[4])
    # chrome_options.add_argument(ls[5])
    # chrome_options.add_argument(ls[6])

    # driver = webdriver.Chrome('C:\\install\\chromedriver.exe', options=chrome_options)
    driver = uc.Chrome(driver_executable_path='C:\\install\\chromedriver.exe', options=chrome_options)

    driver.get(url)

    return driver




def main(url):
    driver = init_webdriver()
    driver.get(url)

    # Не получилось задать город через Куки
    # driver.delete_cookie('city_path')
    # driver.add_cookie({'domain': '.dns-shop.ru', 'httpOnly': False, 'name': 'city_path', 'path': '/', 'secure': False, 'value': 'krasnoyarsk'})
    # a = (driver.get_cookies())
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(1)
    driver.find_element(By.CLASS_NAME, 'pull-right').click()     # Выбрать другой город всплывающем окне
    send_city = driver.find_element(By.XPATH, '//*[@id="select-city"]/div[1]/div[2]/div/input')
    send_city.send_keys('Красноярск')
    driver.find_element(By.XPATH, '//*[@id="select-city"]/div[4]/ul[5]/li[1]/a').click()
    driver.save_screenshot('./image.png')
    price = driver.find_element(By.CSS_SELECTOR, 'div[class=product-buy__price]').text.strip()
    price = int(price[:-2].replace(' ', ''))
    if price < 4199:
        # sound()
        print(f'\nцена снизилась - {price} р')
    if price > 4199:
        # sound()
        print(f'\nцена выросла - {price} р')
    elif price == 4199:
        print(f'\nцена не изменилась - {price} р')
    # time.sleep(5)
    # driver.close()
    driver.quit()

if __name__ == '__main__':
    # url = 'https://www.dns-shop.ru/product/8310230f9b642eb1/provodnaa-garnitura-logitech-g333-belyj/'
    url = 'https://cdek.shopping/products?page=2'
    main(url)


    token = os.getenv("Token")
    print(token)