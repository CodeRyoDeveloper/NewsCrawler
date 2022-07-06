import urllib.request as req    
import bs4  
def getdata(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8") 
    soup=bs4.BeautifulSoup(data,"html.parser")
    root=soup.find_all("div",class_="cd__content")
    i=0
    n=["1","2","3","4","5","6","7","8","9","10"]
    for root in root:
        file=open("textdata"+n[i]+".txt",mode="w",encoding='UTF-8')
        print(root.text)
        file.write(root.text+"\n")
        print("https://edition.cnn.com"+root.a.get("href"))
        file.write("https://edition.cnn.com"+root.a.get("href")+"\n")
        file.write(pagedata("https://edition.cnn.com"+root.a.get("href")))
        file.close()
        i=i+1
        if i>9 :
            break
def pagedata(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8") 
    soup=bs4.BeautifulSoup(data,"html.parser")
    if soup.find("section",id="body-text") != None:
        article=soup.find("section",id="body-text")
        print(article.text)
        return article.text
    else:
        return "None"
url="https://edition.cnn.com/business"
getdata(url)