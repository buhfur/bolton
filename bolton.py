import sys 
from selenium import webdriver 

# first goal : sign into indeed.com 


#args = str[] 

#README: Function that initially uses the first two arguments to setup credentials for the bot 
def setup_creds():  # I don't know how stupid this is to do 
    global EMAIL 
    global PASS  
    EMAIL = sys.argv[1]
    PASS  = sys.argv[2] 
    return (EMAIL, PASS) 


with driver as webdriver.Firefox() : 

    setup_creds()  # establish credentials 

    driver.get("https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess") 
