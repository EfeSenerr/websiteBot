from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

import time
from notify_run import Notify
from datetime import datetime

from bs4 import BeautifulSoup

notify = Notify()

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browserpcs = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://www.hp.com/de-de/shop/product.aspx?id=44W06EA&opt=ABD&sel=DTP')
browserpcs.get('https://www.hp.com/de-de/shop/list.aspx?sel=DTP&ctrl=f&fc_seg_gaming=1')

time.sleep(5)

while True:
    try:
        if browserpcs.find_element_by_xpath("//*[contains(text(), '25L')]") \
                or not browser.find_element_by_xpath("//*[contains(text(), 'NICHT LAGERND ')]"):
            for x in range(18):
                notify.send('PC BULUNDU')
                print('yes', datetime.now())
                time.sleep(10)
            else:
                notify.send('YES')
                browser.close()
                browserpcs.close()
            break
        else:
            print('bulmadi')
            time.sleep(10)
    except NoSuchElementException:
        print('bulmadi', datetime.now())
        time.sleep(45)
        browser.refresh()
        browserpcs.refresh()
        time.sleep(10)
        pass

    soup = BeautifulSoup(browser.page_source, "html.parser")
    if soup.find(string="Nicht lagernd") == "Nicht lagernd":
        print('bulmadi v2', datetime.now())
        time.sleep(45)
        pass
    else:
        print('buldu v2', datetime.now())
        notify.send('yes v2')
        break
