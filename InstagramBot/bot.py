from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self):
        print("Bot starting")
        self.driver = webdriver.Chrome("C:/Users/Derek/Downloads/chromedriver.exe")
        '''
        self.driver.get("https://temp-mail.org/en/")
        sleep(3)
        element = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/input")
        email = element.get_attribute("value")
        '''
        email = "jeanguy1"
        password = "jesuschrist123"
        firstName = "jean"
        lastName="guy"
        year = "1990"
        month="j"
        day = "1"
        self.driver.get("https://hotmail.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/header/div/div/section/div/div[2]/a/span").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div/div[1]/div[1]/fieldset/div/div[3]/div[2]/div/input[1]").send_keys(email)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div/div[1]/div[2]/div/div/div/div[3]/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div[1]/div[3]/div/input[2]").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div[1]/div/div[3]/div[1]/input").send_keys(firstName)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div[1]/div/div[3]/div[2]/input").send_keys(lastName)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div[2]/div/div/div/div[2]/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div/div[1]/div[4]/div[3]/div[1]/select").send_keys(year)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div/div[1]/div[4]/div[3]/div[2]/select").send_keys(month)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div/div[1]/div[4]/div[3]/div[3]/select").send_keys(day)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[5]/div/div/form/div/div[2]/div/div/div/div[2]/input").click()

        while True :
            sleep(3)

        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(email)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/div/label/input").send_keys("jean")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[5]/div/label/input").send_keys("jeanguyOignons")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[5]/div/div/div/button/span").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/div/label/input").send_keys("password1234")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button").click()
        
        while True :
            sleep(3)
InstaBot()