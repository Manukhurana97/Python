import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")# to dissable window
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=options, executable_path= r'C:\\Users\\Manu khurana\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get("http://www.isstracker.com/")

d={}
while True:
    try:

        d['lon']=driver.find_element_by_id('longitudeValue').text
        d['lat']=driver.find_element_by_id('latitudeValue').text
        d['speed']=driver.find_element_by_id('velocityValue').text
        d['alt']=driver.find_element_by_id('altitudeValue').text
        print(d)
        time.sleep(1)
    except KeyboardInterrupt:
        #get out of while loop on control-c
        driver.quit()
        print('Exit program')
        break

    finally:
        pass