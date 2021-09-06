# 2 Feladat: Színes reakció

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
driver.get(URL)


# mezők def

def find_loc(id):
    return driver.find_element_by_id(id)


color_all = driver.find_element_by_id('allcolors').text
print(color_all)


# tesztadatok:
ex_tc01 = [find_loc('randomColorName').text, '[     ]', '']
ex_result_tc03 = ['Incorrect!', 'Correct!']

# a jobb oldal aktuális állapota
def act_test():
    col_act = []
    col_test = find_loc('testColor').text
    col_name_test = find_loc('testColorName').text
    col_act.append(col_test)
    col_act.append(col_name_test)
    return col_act


def act_color(id):
    return find_loc(id).text


def res_text(id):
    return find_loc(id).text

# tc01 teszt: Helyesen jelenik meg az applikáció betöltéskor:
def test_tc01():
    start_list = []
    col_ran = find_loc('randomColorName').text
    start_list.append(col_ran)
    col_test = find_loc('testColor').text
    start_list.append(col_test)
    col_name_test = find_loc('testColorName').text
    start_list.append(col_name_test)
    assert start_list == ex_tc01


# tc02 teszt: El lehet indítani a játékot a start gommbal. Ha elindult a játék akkor a stop gombbal le lehet állítani.
def test_tc02():
    col_st = act_test()
    find_loc('start').click()
    time.sleep(2)
    find_loc('stop').click()
    col_stop = act_test()
    assert col_st != col_stop


# tc03 teszt: Eltaláltam, vagy nem találtam el.
def test_tc03():
    find_loc('start').click()
    time.sleep(2)
    find_loc('stop').click()
    ac = act_color('randomColorName')
    print(ac)
    stop_co = act_color('testColorName')
    print(stop_co)
    try:
        assert ac != stop_co
        print(ac)
        print(stop_co)
        assert res_text('result') == ex_result_tc03[0]
        print(res_text('result'))
        print(ex_result_tc03[0])
    except:
        assert ac == stop_co
        assert res_text('result') == ex_result_tc03[1]
    finally:
        # a pytest hibásan fut, ha a driver zárását a globálban, és nem az utolsó tesztbe ágyazva adom meg
        time.sleep(2)
        driver.close()


# test_tc01()
# test_tc02()
# test_tc03()

