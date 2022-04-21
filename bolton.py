import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


# first goal : sign into indeed.com


# README: Function that initially uses the first two arguments to setup
# credentials for the bot

email = "bobbymcgee"
password = "@Ilikeworldofwarcraft"


'''
def BoltonBot():

    # TODO: add feature to allow the use of command line arguments to supply
    # credentials from a file . A use case of this would be using multiple
    # accounts

    with webdriver.Firefox() as driver:
        driver.get("https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess")

        # locate the email sign in
        email_input = driver.find_element(By.ID, "ifl-InputFormField-3")
        # change the value attribute in the tag

        try: 
            with open('creds.txt' , 'r' ) as credFile : 
                for i in credFile : 

                    print(i)
        email_input.value = email 
        assert email_input.value == email, 'email input must be changed ' 
        #try to submit the information 
        driver.find_element(By.TYPE, "Submit").click() 
'''



#first goal is to sign in 
class BoltonBot:





    def login(self, email, passwd): 





        with webdriver.Firefox() as driver:

            email_input = driver.find_element(By.ID, "ifl-InputFormField-3")
            email_input.value = email 

            driver.get("https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%4A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess") 

            assert email_input.value != email , 'Email was not changed '



if __name__ == "__main__":

    email = sys.argv[1] 
    password = email = sys.argv[2] 
    bot = BoltonBot() 
    bot.login(email,password) 



