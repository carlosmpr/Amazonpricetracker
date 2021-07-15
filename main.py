import requests
from bs4 import BeautifulSoup
import lxml
HEADERS = {
    "Request Line": "GET / HTTP/1.1",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"en-US,en;q=0.9,es-DO;q=0.8,es;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

}
URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
response =requests.get(url=URL, headers=HEADERS)
data = response.text

webdata = BeautifulSoup(data,"lxml")
price = webdata.find(id="priceblock_ourprice")
print(webdata)