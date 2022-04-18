from selenium import webdriver 
from selenium.webdriver.common.keys import Keys  

# first goal : sign into indeed.com 


driver  = webdriver.Firefox() 

driver.get('https://indeed.com') 
# make sure that the sign in button has the class name "gnav-header-o4sfaq emf9s7v0"  
sign_in_link = driver.find_element_by_link_text("Sign in") 



# find sign_in button 

# goto href in the button to get to the sign in page 

#redirect for the browser 


assert "no results found " not in driver.page_source 
driver.close()
