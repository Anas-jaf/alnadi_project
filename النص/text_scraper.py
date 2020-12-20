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







driver = webdriver.Firefox()
num =436

# for x in range( 116,551):
for x in range( 467 , 489 ):

	url ="https://www.typingclub.com/sportal/program-3/" + str(x) +".play"


	web_r= requests.get(url)
	web_soup = BeautifulSoup(web_r.text , 'html.parser')

	driver.get(url)
	time.sleep(1)
	html = driver.execute_script("return document.body.outerHTML;")

	sel_soup = BeautifulSoup(html , 'html.parser')
	# print(sel_soup.findAll('span' ,class_="line"))
	z = sel_soup.findAll('span' ,class_="line")

	print (z)
	
	# file = open(file_name , "w")
	# file.write(str(x))
	# file.close()

	# file = open(file_name , "r")

	# content = file.readline()




	if (len(z) == 0) : 

	
		file = open( str(num) +"_empty page.txt", "w")
		file.write(str(z))
		file.close()
	
	else:
		# print (z)
		# make file that has name as iteration number name 
		file = open( str(num) +".txt", "w")

		file.write(str(z))
		file.close()
		
		file = open( str(num)+".txt" , "r")
		
		content = file.readline()
		# z = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , z)
		
		y = re.sub("</span>"  , "</span>\n" , content)
		
		z=  re.sub("</span>"  , "\n" , y)
		z = re.sub("\n\n<span class=\"token_unit _clr\">"  , "\n" , z)
		# z = re.sub("</span>"  , "\n" , z) 
		z = re.sub("\[<span class=\"line\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , z)
		z = re.sub("<span class=\"token\"><span class=\"_toknmeta\">"  , "" , z)
		z = re.sub("\n"  , "" , z)
		z = re.sub("<span>"  , "" , z)
		z = re.sub("<span class=\"line\">"  , "" , z)
		z = re.sub("\n\n"  , "" , z)
		z = re.sub("<i> </i>"  , " " , z)
		z = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , z)
		z= re.sub("\["  , "" , z)
		z= re.sub("\]"  , "" , z)
		
		print (z)
		file = open( str(num) +".txt", "w")
		file.write(z)
		file.close()

	num += 1
	

# 	# x = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , content)
# 	# x = re.sub("</span>"  , "</span>\n" , content)
# 	# y=  re.sub("</span>"  , "\n" , content)
# 	# x = re.sub("<span class=\"token_unit _clr\">"  , "\n" , y)
# 	# z = re.sub("</span>"  , "\n" , x) 
# 	# x = re.sub("\[<span class=\"line\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "\n" , z)
# 	# y = re.sub("<span class=\"token\"><span class=\"_toknmeta\">"  , "" , x)
# 	# z = re.sub("<span>"  , "" , y)
# 	# x = re.sub("<span class=\"line\">"  , "" , z)
# 	# y = re.sub("\n\n"  , "" , x)
# 	# z = re.sub("<i> </i>"  , " " , y)
# 	# x = re.sub("<span class=\"line active\"><span class=\"token _fcs\"><span class=\"_toknmeta\">"  , "" , z)
# 	# y= re.sub("\["  , "" , x)
# 	# z= re.sub("\]"  , "" , y)
	





# 	# file = open(file_name , "w")
# 	# file.write(z)
# 	# file.close()


driver.close()

