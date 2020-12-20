import pickle
import pprint
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def save_cookies(firefox, location):

    pickle.dump(firefox.get_cookies(), open(location, "wb"))


def load_cookies(firefox, location, url=None):

    cookies = pickle.load(open("C:\\Users\\ansas\\Desktop\\مشروع موقع الطباعة\\النص 2\\cookies.txt", "rb"))
    firefox.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    # firefox.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float 
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int 
        firefox.add_cookie(cookie)


def delete_cookies(firefox, domains=None):

    if domains is not None:
        cookies = firefox.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            firefox.delete_all_cookies()
            for cookie in cookies:
                firefox.add_cookie(cookie)
    else:
        firefox.delete_all_cookies()


# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "C:\\Users\\ansas\\Desktop\\مشروع موقع الطباعة\\النص 2\\cookies.txt"

# # Initial load of the domain that we want to save cookies for
# firefox = webdriver.Firefox()
# firefox.get("https://www.typingclub.com/login.html")
# WebDriverWait(firefox, 20).until(EC.presence_of_element_located((By.ID , "username")))
# firefox.find_element_by_xpath("//*[@id='username']").send_keys("ansas4565@gmail.com")
# firefox.find_element_by_xpath("//input[@id='password']").send_keys("B4gAf3UrA68jJAV")
# firefox.find_element_by_xpath("//button[@id='login-with-password']").click()
# save_cookies(firefox, cookies_location)
# firefox.quit()

# # Load of the page you cant access without cookies, this one will fail
# firefox = webdriver.Firefox()
# firefox.get("https://www.hackerrank.com/settings/profile")


# Load of the page you cant access without cookies, this one will go through
firefox = webdriver.Firefox()
firefox.get("https://www.typingclub.com/sportal/program-3.game")
WebDriverWait(firefox, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div/div[3]")))


firefox.add_cookie(cookie)

firefox.get("https://www.typingclub.com/sportal/program-3.game")

# firefox = webdriver.Firefox()
# firefox.get("https://google.com")
# time.sleep(2)
# pprint.pprint(firefox.get_cookies())
# print "=========================\n"
#
# delete_cookies(firefox, domains=["www.google.com"])
# pprint.pprint(firefox.get_cookies())
# print "=========================\n"
#
# delete_cookies(firefox)
# pprint.pprint(firefox.get_cookies())