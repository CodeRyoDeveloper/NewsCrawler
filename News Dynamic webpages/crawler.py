import shutil   
import bs4
import os 
import time
from selenium import webdriver
def pagedata(url):
    driver.get(url)
    soup=bs4.BeautifulSoup(driver.page_source,"html.parser")
    if soup.find("section",id="body-text") != None:
        article=soup.find("section",id="body-text")
        print(article.text)
        return article.text
    else:
        return "None"
local=os.getcwd()
ch=local.replace("\\","/")
driver=webdriver.Chrome(ch+"/chromedriver.exe")
url="https://edition.cnn.com/business"
driver.get(url)
soup=bs4.BeautifulSoup(driver.page_source,"html.parser")
root=soup.find_all("div",class_="cd__content")
for root in root:
    Del=".!@#$%^&*()\/:*?<>|-+ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    characters="\/:*?<>|"
    date= ''.join( x for x in str(root.a.get("href")) if x not in Del)
    tit = ''.join( x for x in root.text if x not in characters)
    file=open(date[0:8]+" "+tit+".txt",mode="w",encoding='UTF-8')
    print(root.text)
    file.write(root.text+"\n")
    print("https://edition.cnn.com"+root.a.get("href"))
    file.write("https://edition.cnn.com"+root.a.get("href")+"\n")
    time.sleep(3)
    file.write(pagedata("https://edition.cnn.com"+root.a.get("href")))
    file.close()
    for num in os.listdir():
        j=1
        if str(date[0:8]) == num:
            Location1=ch+"/"+date[0:8]+" "+tit+".txt"
            Location2=ch+"/"+date[0:8]+"/"+date[0:8]+" "+tit+".txt"
            shutil.move(Location1,Location2)
            break
        else:
            j=0
    if j==0:
        os.mkdir(str(date[0:8]))
        Location1=ch+"/"+date[0:8]+" "+tit+".txt"
        Location2=ch+"/"+date[0:8]+"/"+date[0:8]+" "+tit+".txt"
        shutil.move(Location1,Location2)
driver.quit()
