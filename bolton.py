import sys 
from selenium import webdriver 

# first goal : sign into indeed.com 


#args = str[] 

#README: Function that initially uses the first two arguments to setup credentials for the bot 
 
Username = "bobbymcgee"
password = "@Ilikeworldofwarcraft" 

def BoltonBot(): 

        #credentials for the bot 


    with webdriver.Firefox() as driver : 

        #TODO : throw exception IndexError when no input for the email address is supplied 
        try:
            setup_creds() 

        except IndexError:
            raise SystemExit(f"Usage: {sys.argv[0] } <string_to_reverse> "  ) 


        driver.get("https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess") 

       #fill out the username and password boxes 


if __name__ == "__main__": 
    BoltonBot()
