import re 
import time
import json
import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()



# global variables 
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)
wait2 = WebDriverWait(driver, 15)
#############################################################
# this function  will strip the page to the wanted text 
# page_source_code ----- page length
# num ---------- file name
def strip_page_2text(page_source_code, num ):
    if (len(page_source_code) == 0) :
        print("video or play page\n")
        file = open( str(num) +"_video_or_play_page.txt", "w")
        file.write(str(page_source_code))
        file.close()
    
    else:
        # print (page_source_code)
        # make file that has name as iteration number name 
        file = open( str(num) +".txt", "w")

        file.write(str(page_source_code))
        file.close()
        
        file = open( str(num)+".txt" , "r")
        
        content = file.readline()
        # page_source_code = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , page_source_code)
        
        y = re.sub("</span>"  , "</span>\n" , content)
        
        page_source_code=  re.sub("</span>"  , "\n" , y)
        page_source_code = re.sub("\n\n<span class=\"token_unit _clr\">"  , "\n" , page_source_code)
        # page_source_code = re.sub("</span>"  , "\n" , page_source_code) 
        page_source_code = re.sub("\[<span class=\"line\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , page_source_code)
        page_source_code = re.sub("<span class=\"token\"><span class=\"_toknmeta\">"  , "" , page_source_code)
        page_source_code = re.sub("\n"  , "" , page_source_code)
        page_source_code = re.sub("<span>"  , "" , page_source_code)
        page_source_code = re.sub("<span class=\"line\">"  , "" , page_source_code)
        page_source_code = re.sub("\n\n"  , "" , page_source_code)
        page_source_code = re.sub("<i> </i>"  , " " , page_source_code)
        page_source_code = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , page_source_code)
        page_source_code= re.sub("\["  , "" , page_source_code)
        page_source_code= re.sub("\]"  , "" , page_source_code)
        file = open( str(num) +".txt", "w")
        file.write(page_source_code)
        file.close()


#############################################################
# this function  will log into account 
def log_in():
    print("\nlogging in using your account!!!!...please wait.")
    print("==================================")
    driver.get("https://www.typingclub.com/login.html")
    wait.until(EC.presence_of_element_located((By.ID , "username")))
    driver.find_element_by_xpath("//input[@id='username']").send_keys("ansas4565@gmail.com")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("B4gAf3UrA68jJAV")
    # time.sleep(10)
    driver.find_element_by_xpath("//button[@class='btn log-in-with']").click()
    time.sleep(15)
    print("successfully logged in ")
    #############################################################
    # this block of code will reach to the page that you want to scrape from 
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body")))
    driver.get("https://www.typingclub.com/sportal/program-3.game")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='lsn_num']")))
    # lastpage = driver.find_element_by_xpath("//div[contains(text(),'683')]").send_keys(Keys.RETURN)

    print ("we reached to the page that you want")

#############################################################

#############################################################
# this function goes to the page that you want  scrape and click it to scrape  
def click_to_page(num):
    
    button = driver.find_element_by_xpath("//div[@class='lsn_num'][contains(text(),'%d')]" %num)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='lsn_num'][contains(text(),'%d')]" %num)))
    driver.maximize_window()
    # actions.move_to_element(button).perform()
    # actions = ActionChains(driver)
    print("wait .....")
    driver.execute_script('arguments[0].scrollIntoView(true);', button)
    # time.sleep(9)

    # button.click()
    driver.execute_script("arguments[0].click();", button)
#############################################################

#this function to back to the page
def back():
    driver.get("https://www.typingclub.com/sportal/program-3.game")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='lsn_num']")))

#############################################################

#############################################################
# this function  will log into account 
def start():
    print("opening the browser")
    print("==================================")
    log_in()
#############################################################

#############################################################

def get_page_contant():
    html = driver.execute_script("return document.body.outerHTML;")
    sel_soup = BeautifulSoup(html , 'html.parser')
    content = sel_soup.findAll('span' ,class_="line")
    return content
    
#############################################################

#############################################################
# click_to_page(1)
# wait2.until(EC.presence_of_element_located((By.XPATH, "//span[@class='token_unit  _clr']" )))


# print(get_page_contant()) 

#############################################################
start()
#############################################################
for x in range(354,685):

    
    # this function goes to the page that you want to scrape and click it to scrape 
    # num-----page number
    click_to_page(x)

    try:
        wait2.until(EC.presence_of_element_located((By.XPATH, "//span[@class='token_unit  _clr']" )))
        page_SC = get_page_contant()
    except :
        page_SC =''


    # this function  will strip the page to the wanted text 
    # page_source_code ----- page content
    # num ---------- file name
    print(x)
    strip_page_2text(page_SC , x)
    back()