import urllib.request as req
url="https://www.bloomberg.com/markets"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="story-list-story__info__headline")
for titles in titles:
    print(titles.a.string)
    print("https://www.bloomberg.com"+titles.a.get("href"))