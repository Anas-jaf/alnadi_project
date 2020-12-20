import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re 

#############################################################
# this function  will strip the page to the wanted text 
# web_page ----- page length
# num ---------- file name
def strip_page_2text(web_page, num ):
	
	if (len(web_page) == 0) : 

	
		file = open( str(num) +"_empty page.txt", "w")
		file.write(str(web_page))
		file.close()
	
	else:
		# print (web_page)
		# make file that has name as iteration number name 
		file = open( str(num) +".txt", "w")

		file.write(str(web_page))
		file.close()
		
		file = open( str(num)+".txt" , "r")
		
		content = file.readline()
		# web_page = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , web_page)
		
		y = re.sub("</span>"  , "</span>\n" , content)
		
		web_page=  re.sub("</span>"  , "\n" , y)
		web_page = re.sub("\n\n<span class=\"token_unit _clr\">"  , "\n" , web_page)
		# web_page = re.sub("</span>"  , "\n" , web_page) 
		web_page = re.sub("\[<span class=\"line\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , web_page)
		web_page = re.sub("<span class=\"token\"><span class=\"_toknmeta\">"  , "" , web_page)
		web_page = re.sub("\n"  , "" , web_page)
		web_page = re.sub("<span>"  , "" , web_page)
		web_page = re.sub("<span class=\"line\">"  , "" , web_page)
		web_page = re.sub("\n\n"  , "" , web_page)
		web_page = re.sub("<i> </i>"  , " " , web_page)
		web_page = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , web_page)
		web_page= re.sub("\["  , "" , web_page)
		web_page= re.sub("\]"  , "" , web_page)
		
		file = open( str(num) +".txt", "w")
		file.write(web_page)
		file.close()

#############################################################
# this function  will log into account 
def log_in():
	print("logging in using your account!!!!...please wait.")
	print("==================================")
	driver.get("https://www.typingclub.com/login.html")
	wait.until(EC.presence_of_element_located((By.ID , "username")))
	driver.find_element_by_xpath("//input[@id='username']").send_keys("ansas4565@gmail.com")
	driver.find_element_by_xpath("//input[@id='password']").send_keys("B4gAf3UrA68jJAV")
	# time.sleep(10)
	driver.find_element_by_xpath("//button[@class='btn log-in-with']").click()
	time.sleep(2)
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
	print("wait a while")
	driver.execute_script('arguments[0].scrollIntoView(true);', button)
	# time.sleep(9)

	# button.click()
	driver.execute_script("arguments[0].click();", button)
	#############################################################


# this function  will log into account 
log_in()


for x in range(1,685):

	
	# this function goes to the page that you want  scrape and click it to scrape 
	# num-----page number
	click_to_page(x)

	page_SC =wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='token_unit  _clr']" )))
	# page_SC = driver.page_source



	# this function  will strip the page to the wanted text 
	# web_page ----- page content
	# num ---------- file name
	strip_page_2text(page_SC , num)








