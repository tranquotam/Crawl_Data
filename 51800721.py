import requests
import csv
from bs4 import BeautifulSoup


question_1 = True
question_2 = True
authors = {}
url = 'https://quotes.toscrape.com/page/__index__/'


def tacgiaLink(author_link):
    x = requests.get(author_link)
    soup = BeautifulSoup(x.text, "html.parser")
    name = soup.find("h3", {"class": "author-title"}).text.split('\n')[0]
    birthdate =  soup.find("span", {"class": "author-born-date"}).text

    return name, birthdate, author_link


def to_csv(dic):
    data = []
    for k,v in dic.items():
        data.append(v)
    
    with open('Quote.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Tacgia', 'Link', 'Namsinh', 'Quote'])
        writer.writeheader()
        writer.writerows(data)


for index in range(1,11):
    x = requests.get(url.replace('__index__', str(index)))

    soup = BeautifulSoup(x.text, "html.parser")
    mydivs = soup.find_all("div", {"class": "row"})

    with open('kq.txt', 'a' , encoding='utf-8') as f:
        f.write(str(mydivs[1]))


with open("kq.txt", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    result = soup.find_all("div", {"class": "quote"})
    if question_1: print(result)
    
    for quote in result:
        author = quote.findChild("small")
        
        if question_2: print(author)
        
        name, birthdate, author_link = tacgiaLink('https://quotes.toscrape.com' + quote.findChild("a")['href'])
        text = quote.find('span', class_='text').text

        if name in authors:
            authors[name]["Quote"].append(text)
        else:
            authors[name] = {
                'Tacgia': name,
                'Link':author_link,
                'Namsinh':birthdate,
                'Quote': [text]
            }

    to_csv(authors)       
    
    
