import requests
from bs4 import BeautifulSoup 
'''

 url schema: 

    https://www.indeed.com/jobs?q=[[ JOB NAME ]]&l=[[ JOB LOCATION ]] 

 '''


def bolton(what,where): 
    #craft url using hexadecimal representations for spaces for the characters  
    query = ( "%20".join(what.split()) , "%20".join(where.split() )) 
    url = f"https://www.indeed.com/jobs?q={query[0]}&l={query[1]}" 
    #make get request to indeed website 
    response = requests.get(url) 
    #make sure the url request was sucessful 
    assert response.status_code < 200 , raise requests.HTTPError
    #parse the body message 
    page = BeautifulSoup(response.text ,'html.parser') 
    #list all tags with a class attribute of ( class = "jcs-JobTitle" ) 
    for listing in page.find_all("jcs-JobTitle"):
        print(f"\tFound Listing! : {listing}\n")




if __name__ == '__main__':
    bolton("Software Engineer", "Fort Wayne") 
