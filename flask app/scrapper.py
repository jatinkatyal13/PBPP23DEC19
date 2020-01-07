import requests
from bs4 import BeautifulSoup

def scrapSnapdeal(query):
  url = "https://www.snapdeal.com/search"
  params = {
    "keyword": query,
    "sort": "phtl"
  }
  r = requests.get(url, params = params)
  soup = BeautifulSoup(r.content)
  products = soup.findAll('div', attrs = {"class": "product-tuple-listing"})
  result = []

  for product in products:
    img_tag = product.find('img')
    if 'src' in img_tag.attrs:
        img = img_tag.attrs['src']
    else:
        img = img_tag.attrs['data-src']
    
    title = product.find('p', attrs = {"class": "product-title"}).text
    price = product.find('span', attrs = {"class": "product-price"}).text
    
    d = {
      "img": img,
      "title": title,
      "price": price
    }
    result.append(d)
  
  return result
