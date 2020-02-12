from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        print("Bot starting")
        self.driver = webdriver.Chrome("C:/Users/Derek/Downloads/chromedriver.exe")

    def login(self):
        print("Logging in")
        phone = "5146326676"
        self.driver.get("https://tinder.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/div[1]/button/span").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/input").send_keys(phone)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button/span").click()

        ''' TIME TO ACTIVATE CODE BY PHONE ''' 
        sleep(3)
        sleep(3)
        sleep(3)  
        print("Login timer done")

        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
        sleep(0.5)

        ''' AUTO - SWIPE ''' 
        print('Swiping')
        while True:
            sleep(0.5)
            try:
                self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]").click()
            except Exception:
                try:
                    self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button[2]/span").click()
                except Exception:
                    try:
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]/span").click()
                    except Exception:
                        while True:
                            sleep(2)

bot = TinderBot()
bot.login()
