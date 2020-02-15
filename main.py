from selenium import webdriver
from time import sleep
from login import usr
from login import pw

class InstaBot:
     def __init__(self, usr, pw):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(usr)#Enters username
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(pw)#Enters password
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()#Clicks login
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()#clicks not now
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a").click()#Goes to profile
     def get_unfollowers(self):
        self.driver.find_element_by_xpath

     def unfollowers(self): 
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]").click()#Goes on following
        following = self.__get_names()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]").click()#Goes to followers
        followers = self.__get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

        
     def __get_names(self):
        sleep(2)
        #Scroll to the bottom
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        bottom_ht, ht = 0, 1
        while bottom_ht != ht:
                bottom_ht = ht
                sleep(1)
                ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #close button
        self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button/svg").click()
        return names


bot = InstaBot(usr, pw)
bot.unfollowers()      