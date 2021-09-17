import requests
import json
from bs4 import BeautifulSoup

def scrapeWiki():
    url = "https://enterthegungeon.fandom.com/wiki/Guns"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    gunTable = soup.find('table')
    gunList = gunTable.find_all('tr')
    jsonList = []
    cleanedList = []
    for i in range(len(gunList)):
        gunData = []
        #TODO not entirely accurate yet make sure blasphmeny lines up correctly
        for node in gunList[i].find_all('td'):
            finalEntry = node.text.strip('\n')
            finalEntry = finalEntry.strip()
            if finalEntry != "/" and finalEntry != '':
                gunData.append(finalEntry)
        if gunData != []:
            cleanedList.append(gunData)
    pknum = 1
    for gun in cleanedList:
        gunDict = {}
        gunDict['model'] = "Gun.Gun"
        gunDict['pk'] = pknum
        pknum += 1
        attrDict = {}
        attrDict['gunName'] = gun[0]
        attrDict['quote'] = gun[1]
        attrDict['type'] = gun[2]
        attrDict['DPS'] = gun[3]
        attrDict['mag'] = gun[4]
        attrDict['ammo'] = gun[5]
        attrDict['rate'] = gun[6]
        attrDict['reload'] = gun[7]
        attrDict['shotspd'] = gun[8]
        attrDict['range'] = gun[9]
        attrDict['force'] = gun[10]
        attrDict['spread'] = gun[11]
        gunDict['fields'] = attrDict
        jsonList.append(gunDict)

    jsonFile = open("guns.json", "w")
    jsonString = json.dumps(jsonList)
    jsonFile.write(jsonString)
    jsonFile.close()
        
def main():
    scrapeWiki()
if __name__ == '__main__':
    main()