# 3 Feladat: Alfanumerikus mező

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
driver.get(URL)


# tesztadatok:
data_tc01 = 'abcd1234'
ex_tc01 = ''
data_tc02 = 'title: teszt233@'
ex_tc02 = 'Only a-z and 0-9 characters allewed'
data_tc03 = 'abcd'
ex_tc03 = 'Title should be at least 8 characters; you entered 4.'


# mezők def

def find_inp():
    return driver.find_element_by_id('title')


def find_title_mes():
    return driver.find_element_by_xpath('/html/body/form/span')


# tc01 teszt: Helyes kitöltés esete:
def test_tc01():
    find_inp().send_keys(data_tc01)
    time.sleep(0.2)
    assert find_title_mes().text == ex_tc01


# tc02 teszt: Illegális karakterek esete:
def test_tc02():
    driver.refresh()
    find_inp().send_keys(data_tc02)
    time.sleep(0.2)
    assert find_title_mes().text == ex_tc02


# tc03 teszt: Túl rövid bemenet esete:
def test_tc03():
    driver.refresh()
    find_inp().send_keys(data_tc03)
    time.sleep(0.2)
    assert find_title_mes().text == ex_tc03
    # a pytest hibásan fut, ha a driver zárását a globálban, és nem az utolsó tesztbe ágyazva adom meg
    time.sleep(2)
    driver.close()


# test_tc01()
# test_tc02()
# test_tc03()

