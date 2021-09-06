# 5 Feladat: 5 Feladat: Bingo

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"
driver.get(URL)


# tesztadatok:'
ex_tc01 = [25, 75]


# mezők def:
chb_table = driver.find_elements_by_xpath("//input[@name='number']")
print(len(chb_table))

chb_num = driver.find_elements_by_xpath("//ol[@id='numbers-list']//input[@type='checkbox']")
print(len(chb_num))

chb_mar_num = driver.find_elements_by_xpath("//ol[@id='numbers-list']//li[@class='checked']")
print(len(chb_mar_num))

play_button = driver.find_element_by_id('spin')
play_init =  driver.find_element_by_id('init')

bingo_text = driver.find_elements_by_xpath("//ul[@id='messages']/li")


# tc01 teszt: Az applikáció helyesen megjelenik:
def test_tc01():
    ex_data = []
    ex_data.append(len(chb_table))
    ex_data.append(len(chb_num))
    assert ex_data == ex_tc01
    # a pytest hibásan fut, ha a driver zárását a globálban, és nem az utolsó tesztbe ágyazva adom meg
    time.sleep(2)
    driver.close()


# tc02 teszt: Bingo számok ellenőzrzése:
"""
Elfogyott az időm:
a megoldáshoz egy végtelen ciklusban nyomogattam volna a gombot, amíg a "Bingo" felirat meg nem jelenik.
Majd kiolvastam volna a megjelőlt számokat egy listába (chb_mar_num) , és összehasonlítottam volna a táblázat számait tartalmazó listával.
"""

# tc03 teszt: Új játékot tudunk indítani:
def test_tc03():
    play_init.click()

#test_tc01()