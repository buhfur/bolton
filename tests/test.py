import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

class IndeedOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() 

    #attempt to sign into indeed 
    def test_indeed_search(self):
        driver = self.driver 


