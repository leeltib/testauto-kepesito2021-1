# 4 Feladat: Műveletek karakterekkel

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
driver.get(URL)


# tesztadatok:'
ex_tc01 = '!"' + "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


# mezők def:
rand_abc = driver.find_element_by_xpath("//div[@class='flex-child']/p[3]")


# tc01 teszt: Helyesen betöltődik az applikáció::
def test_tc01():
    assert rand_abc.text == ex_tc01


# tc02 teszt: Megjelenik egy érvényes művelet:

# tc03 teszt: Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:


#test_tc01()



