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


with webdriver.Firefox() as driver : 

    #TODO : throw exception IndexError when no input for the email address is supplied 
    try:
        setup_creds() 

    except IndexError:
        print("NO email or password provided") 
        if len(sys.argv > 3): 
            print("Too many arguments supplied " ) 

        
    print(f"username: {0}\npassword: {1} ",setup_creds() )  # establish credentials 

    driver.get("https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess") 
