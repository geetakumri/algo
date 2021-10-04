import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_termin(tor, termin):
    os.popen(tor)

    proxy = 'socks5://localhost:9050'
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % proxy)
    # options.add_argument('window-position=2900,0')

    driver = webdriver.Chrome(options=options)

    driver.get(termin)

    appointment_selector = "/html/body/div[2]/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div[4]/div[1]/div/div[2]/div/a"
    driver.find_element_by_xpath(appointment_selector).click()


    try:
        buchbar = driver.find_element_by_xpath('//td[@class="buchbar"]')
        if int(buchbar.text) > 15 and int(buchbar.text) > 22:
            buchbar.click()
        buchbar.click()
        time.sleep(10000)
    except NoSuchElementException:
        #nextpage = driver.find_element_by_xpath('//a[@title="nächster Monat ab (01-09-2021)"]')
        #nextpage.click()
        try:
            buchbar = driver.find_element_by_xpath('//td[@class="buchbar"]')
            if int(buchbar.text) > 15 and int(buchbar.text) > 22:
                buchbar.click()
            time.sleep(10000)
        except NoSuchElementException:
            driver.close()
            driver.quit()
    finally:
        os.system('taskkill /im tor.exe /f')


if __name__ == '__main__':
    tor_path = r'C:\Users\geeta\OneDrive\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe'
    #termin_path = input('Enter Termin URL: ')
    termin_path = "https://service.berlin.de/dienstleistung/120686"

    while True:
        get_termin(tor_path, termin_path)
