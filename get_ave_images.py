import requests 
from bs4 import BeautifulSoup 

print("hello world")    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.avesdechile.cl/0jpgn/") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('a'):
    file="https://www.avesdechile.cl/0jpgn/"+item['href']
    solo_imagen=file.find('.jpg')
    if(solo_imagen>1):
        img_data = requests.get(file).content
        print("Descargando imagen:"+file)
        with open(item['href'], 'wb') as handler:
            handler.write(img_data)
            print("imagen grabadas")
    