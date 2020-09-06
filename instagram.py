from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import bs4
import time
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
try:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
except:
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=r'C:\\Users\CLEMENT\Downloads\chromedriver_win32\chromedriver.exe')

def open(username,password):
    driver.get('https://www.instagram.com/')
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(str(username))
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(str(password))
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
    time.sleep(3)
    driver.get('https://www.instagram.com/')
    time.sleep(3)
    try:
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    except NoSuchElementException as e:
        print(e)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
    # driver.get('https://www.instagram.com/blacksheeptamil')
    time.sleep(2)
    followers=getFollwers()
    following=getFollowing()
    notfollowing=[]
    for f in following:
        if f not in followers:
            notfollowing.append(f)
    print(len(notfollowing))
    for nonfollower in notfollowing:
        unfollow(nonfollower)
        time.sleep(0.05)
    time.sleep(4)
    driver.get('https://www.instagram.com/angel__francis/following/')
def getFollwers():
    n = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')
    n=n.split(',')
    n=('').join(n)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(4)
    scrolling(n)
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('.isgrP').scrollTo(0, document.querySelector('.isgrP').scrollHeight);")
    list = driver.find_elements(By.CLASS_NAME, "FPmhX")
    time.sleep(2)
    follower=[]
    for i in range(0, len(list)):
        follower.append(list[i].text)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
    time.sleep(2)
    return follower

def getFollowing():
    n=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
    scrolling(n)
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('.isgrP').scrollTo(0, document.querySelector('.isgrP').scrollHeight);")
    list = driver.find_elements(By.CLASS_NAME, "FPmhX")
    time.sleep(2)
    print(list[2])
    following=[]
    for i in range(0, len(list)):
        following.append(list[i].text)
    return following
def unfollow(user):
    driver.get('https://www.instagram.com/'+user)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button').click()
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
def scrolling(n):
    present=True
    while(present):
        try :
            time.sleep(0.1)
            driver.execute_script("document.querySelector('.isgrP').scrollTo(0, document.querySelector('.isgrP').scrollHeight);")
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(int(n)-5)+']')
            present = False
        except NoSuchElementException:
            present = True
username=input('enter username : ')
password=input('enter password : ')
try:
    open(username,password)
except:
    print('Error occured')

