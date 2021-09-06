# 1 Feladat: Pitagorasz-tétel

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
driver.get(URL)

# tesztadatok:
ex_tc01 = ['', '', 'display: none;']
data_tc02 = [2, 3]
ex_tc02 = '10'
data_tc03 = ['', '']
ex_tc03 = 'NaN'


# mezők

def find_loc(id):
    return driver.find_element_by_id(id)


# kitöltő függvény
def input_wr(da):
    find_loc("a").clear()
    find_loc("a").send_keys(da[0])
    find_loc("b").clear()
    find_loc("b").send_keys(da[1])
    time.sleep(0.2)


# tc01 : Helyesen jelenik meg az applikáció betöltéskor:
def test_tc01():
    inp_list = []
    a = find_loc("a").get_attribute("value")
    inp_list.append(a)
    b = find_loc("b").get_attribute("value")
    inp_list.append(b)
    res = find_loc("results").get_attribute("style")
    inp_list.append(res)
    assert inp_list == ex_tc01


# tc02 : Számítás helyes, megfelelő bemenettel
def test_tc02():
    input_wr(data_tc02)
    find_loc("submit").click()
    assert find_loc("result").text == ex_tc02


# tc03 : Üres kitöltés:
def test_tc03():
    input_wr(data_tc03)
    find_loc("submit").click()
    assert find_loc("result").text == ex_tc03
    # a pytest hibásan fut, ha a driver zárását a globálban, és nem az utolsó tesztbe ágyazva adom meg
    time.sleep(2)
    driver.close()


# test_tc01()
# test_tc02()
# test_tc03()
