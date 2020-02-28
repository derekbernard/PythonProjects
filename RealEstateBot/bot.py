from selenium import webdriver
from time import sleep

class Bot():
    def __init__(self):
        print("Bot starting")
        self.driver = webdriver.Chrome("C:/Users/Derek/Downloads/chromedriver.exe")

    def login(self):
        print("Starting")
        self.driver.get("https://duproprio.com/en/search/list")
        sleep(3)
        pageNumber = 1
       
        while True: 
            self.iterateTroughList()
            sleep(1)
            pageNumber= pageNumber + 1
            print(pageNumber)
            self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[3]/div/nav/div[2]/a").click()

            

        while True:
            print("searching for houses")
            sleep(1)
            try:
                self.driver.find_elements_by_class_name("search-results-listings-list__item-image-link")[0].click()
            except Exception:
                try:
                    self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div/div/div[1]").click()   
                except Exception:
                        exit(0)

    def iterateTroughList(self):
        listOfHouse =  self.driver.find_elements_by_class_name("search-results-listings-list__item-image-link")
        
        for i in range(len(listOfHouse)):
            listOfHouse =  self.driver.find_elements_by_class_name("search-results-listings-list__item-image-link")
            while True:
                try:
                    print("Trying to click house in list")
                    listOfHouse[i].click()
                    print("clicked")
                    sleep(3)
                    self.executeAnalysis()
                    #if not self.visited():
                    #    print("not visited")
                    #    self.executeAnalysis()
                    #else : 
                    #    print("already visited break")
                    break
                except:
                    print("couldnt clicked house listing")
                    sleep(3)
                    try:
                        self.driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div/div/div[1]").click()
                        print("popup closed, continuing")
                        sleep(2)
                    except:
                        print("unexcepted error, exiting")
                        print(i)
                        break

            print("done")
            self.driver.back()
            sleep(3)

    def visited(self):
        url = self.driver.current_url
        with open("list.txt") as fp:
            lines = fp.readlines()
            if url in lines:
                fp.close()
                return True
            else :
                fp.close()
                return False
         
    def executeAnalysis(self):
        print("analysis")
        text = self.driver.find_elements_by_xpath("/html/body/main/div[1]/div/div[1]/section[1]/article/div[3]/div[1]")[0].text
        if self.municipalAssessmentExist(text):
            if self.compareValueToAssessment(text) < 1:
                self.writeIdToFile(self.driver.current_url)

    def municipalAssessmentExist(self,text):
        if "Municipal Assessment" in text:
            return True

    def compareValueToAssessment(self,text):
        index = text.find("Municipal Assessment") + 20 
        assessment = ""
        for i in range(0,10):
            assessment = assessment + text[index +i] 
        assessment = assessment.lstrip()
        assessment = assessment.strip("$")
        assessment = ''.join([i for i in assessment if  i.isdigit()])

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
