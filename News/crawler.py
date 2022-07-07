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
        file.write(pagedata("https://edition.cnn.com"+root.a.get("href")))
        file.close()
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