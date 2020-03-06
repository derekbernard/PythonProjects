from selenium import webdriver
from time import sleep

class Bot():
    def __init__(self):
        print("Bot starting")
        self.driver = webdriver.Chrome("C:/Users/Derek/Downloads/chromedriver.exe")

    def login(self):
        print("Starting")
        #self.driver.get("https://duproprio.com/en/search/list?search=true&regions%5B0%5D=13&regions%5B1%5D=15&regions%5B2%5D=6&regions%5B3%5D=16&max_price=1000000&is_for_sale=1&with_builders=1&parent=1&pageNumber=1&sort=-published_at")
        self.driver.get("https://duproprio.com/en/search/list?search=true&regions%5B0%5D=13&regions%5B1%5D=15&regions%5B2%5D=6&max_price=1000000&type%5B0%5D=house&type%5B1%5D=cottage&type%5B2%5D=multiplex&type%5B3%5D=terr&type%5B4%5D=farm&subtype%5B0%5D=1&subtype%5B1%5D=2&subtype%5B2%5D=4&subtype%5B3%5D=5&subtype%5B4%5D=6&subtype%5B5%5D=7&subtype%5B6%5D=9&subtype%5B7%5D=10&subtype%5B8%5D=11&subtype%5B9%5D=13&subtype%5B10%5D=15&subtype%5B11%5D=17&subtype%5B12%5D=18&subtype%5B13%5D=19&subtype%5B14%5D=20&subtype%5B15%5D=21&subtype%5B16%5D=97&subtype%5B17%5D=98&subtype%5B18%5D=99&subtype%5B19%5D=100&subtype%5B20%5D=8&subtype%5B21%5D=40&subtype%5B22%5D=52&subtype%5B23%5D=53&subtype%5B24%5D=55&subtype%5B25%5D=56&subtype%5B26%5D=54&subtype%5B27%5D=57&subtype%5B28%5D=58&subtype%5B29%5D=59&subtype%5B30%5D=60&subtype%5B31%5D=61&subtype%5B32%5D=62&subtype%5B33%5D=93&subtype%5B34%5D=94&subtype%5B35%5D=95&subtype%5B36%5D=40&subtype%5B37%5D=103&subtype%5B38%5D=104&is_for_sale=1&with_builders=1&parent=1&pageNumber=1&sort=-published_at")
        sleep(3)
        pageNumber = 1

        while True: 
            self.iterateTroughList()
            sleep(1)
            pageNumber= pageNumber + 1
            print(pageNumber)
            self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[3]/div/nav/div[2]/a").click() # next page button

    def iterateTroughList(self):
        listOfHouse =  self.driver.find_elements_by_class_name("search-results-listings-list__item-image-link") # list of house div
        for i in range(len(listOfHouse)):
            listOfHouse =  self.driver.find_elements_by_class_name("search-results-listings-list__item-image-link")
            while True:
                try:
                    print("Trying to click house in list")
                    listOfHouse[i].click()
                    print("clicked")
                    sleep(3)
                    self.executeAnalysis()
                    break
                except:
                    print("couldnt clicked house listing")
                    sleep(3)
                    try:
                        self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div/div/div[1]").click()   # pop up close button
                        print("popup closed, continuing")
                        sleep(2)
                    except:
                        print("unexcepted error, exiting")
                        print(i)
                        break
            print("done")
            self.driver.back()
            sleep(3)
         
    def executeAnalysis(self):
        print("analysis")
        text = self.driver.find_elements_by_xpath("/html/body/main/div[1]/div/div[1]/section[1]/article/div[3]/div[1]")[0].text # house description div
        if self.municipalAssessmentExist(text):
            if self.compareValueToAssessment(text) < 1:
                self.writeIdToFile(self.driver.current_url)

    def municipalAssessmentExist(self,text):
        if "Municipal Assessment" in text:
            return True

    def compareValueToAssessment(self,text):
        # Assessment
        index = text.find("Municipal Assessment") + 20 
        assessment = ""
        for i in range(0,10):
            assessment = assessment + text[index +i] 
        assessment = assessment.lstrip()
        assessment = assessment.strip("$")
        assessment = ''.join([i for i in assessment if  i.isdigit()])

        # Asked Price
        index = text.find("Asking Price") + 13 
        price = ""
        for i in range(0,10):
            price = price + text[index +i] 
        price = price.lstrip()
        price = price.strip("$")
        price = ''.join([i for i in price if  i.isdigit()])

        return (int(price)/int(assessment))
    
    def writeIdToFile(self,url):
        f = open("list.txt", "a")
        f.write(url + "\n")
        f.close()
    

bot = Bot()
bot.login()
