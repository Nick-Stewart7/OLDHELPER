import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

"""@dataclass
    class Gun(repr=True):
    Icon: str
    Name: str
    Quote: str
    Quality: str
    Type: str
    DPS: float
    Mag: int
    Ammo: int
    Damage: int
    FRate: float
    Reload: float
    ProjSpeed: int
    Range: int
    Force: int
    Spread: int
    Notes: str"""

def scrapeWiki():
    url = "https://enterthegungeon.fandom.com/wiki/Guns"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    gunTable = soup.find('table')
    gunList = gunTable.find_all('tr')
    for i in range(len(gunList)):
        gunData = []
        for node in gunList[i].find_all('td'):
            if node.text != '':
                finalEntry = node.text.strip('\n')
                gunData.append(finalEntry)
            #make everything a gun class
            #how to store gun class for later access
            #does it have to be a class? just throw this in a database
            #make other python that uses the database so web app
            #does not have to do this init?
            #this scrape is an init
            #program will need to parse this data
        print(gunData)
        print("maybethis")
        
def main():
    scrapeWiki()
    #testtttergit
if __name__ == '__main__':
    main()