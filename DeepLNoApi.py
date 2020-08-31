import time
from selenium import webdriver 
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager

text=input("Type in a text for translation: ")
lang_1=input("Set first language: ")
lang_2=input("Set second language: ")

text = text.replace(" ", "%20")
load_url = f'https://www.deepl.com/en/translator#{lang_1}/{lang_2}/{text}'
driver = webdriver.Chrome(ChromeDriverManager().install())
"""
After installing ChromeDriver, replace the ChromeDriverManager().install() [driver = webdriver.Chrome('PATH_HERE')] with the webdriver installation path (this path is written in terminal)
"""
driver.get(load_url)

while 1:
    Output_selector = "#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__translations_as_text > p > button.lmt__translations_as_text__text_btn"
    Outputtext = driver.find_element_by_css_selector(Output_selector).get_attribute("textContent")
    if Outputtext != "" :
        break
    time.sleep(1)

print("Translation: " + Outputtext)
driver.close()
driver.quit()
