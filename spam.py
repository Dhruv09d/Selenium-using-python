from selenium import webdriver
import time
import random

list = ['Hacked', 'hii', 'hehe', 'ohhooo', 'lalalalalal'] #set ur msg accordingly

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://web.whatsapp.com/')
time.sleep(6)
name = 'Target_name_same_as_whats_app' #do paste same emoji if name have any
meme_lords =  driver.find_element_by_xpath("//span[@title='{}']".format(name)).click()
msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
time.sleep(2)
nom = int(input("enter the no of msg to be send: "))
i = 0
while i < nom:
    a = random.randint(0, 4)
    msg.send_keys(list[a])
    try:
        send_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    except:
        continue
    print(i)
    i+=1
    #time.sleep(2)
