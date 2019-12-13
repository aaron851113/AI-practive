import requests
from bs4 import BeautifulSoup



number=1

def downloadNews(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    right = soup.find(class_='listRight')
    d=[]
    for new in right.find_all(class_='clear-fix'):
        title = new.find('h2').text.strip()
        u = new.find('a').get('href')
        d.append({'title':title, 'url':u})
        global number
        print(number,":",title) 
        number+=1

if __name__ == '__main__':
    url='http://www.chinatimes.com/newspapers/2601?page='
    for page in range(1,22) :
        http = url+str(page)
        print("page [",page,"]")     
        d=downloadNews(http)
    