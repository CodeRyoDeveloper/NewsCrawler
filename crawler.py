from re import M
import urllib.request as req
def getdata(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4 
    soup=bs4.BeautifulSoup(data,"html.parser")
    root=soup.find_all("div",class_="cd__content")
    for root in root:
        print(root.text)
        file.write(root.text)
        file.write("\n")
        print("https://edition.cnn.com"+root.a.get("href"))
        file.write("https://edition.cnn.com"+root.a.get("href"))
        file.write("\n")
        pagedata("https://edition.cnn.com"+root.a.get("href"))       
def pagedata(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4 
    soup=bs4.BeautifulSoup(data,"html.parser")
    if soup.find("section",id="body-text") != None:
        article=soup.find("section",id="body-text")
        print(article.text)
        file.write(article.text)
        file.write("\n\n\n\n\n\n\n\n")
file=open("data.txt",mode="w",encoding='UTF-8')
pageURL="https://edition.cnn.com/business"
getdata(pageURL)
file.close()

