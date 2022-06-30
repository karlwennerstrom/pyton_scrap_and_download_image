import requests 
import os
from bs4 import BeautifulSoup 

print("Obteniendo nombre para carpetas")
arreglo_carpetas=[]
arreglo_nombres=[]    
def getdata(url): 
    r = requests.get(url) 
    return r.text    
htmldata = getdata("https://www.avesdechile.cl/aves07.htm") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('a'):  
    carpeta=str(item.get('href'))
    if carpeta.find('.htm')>1:
         nombre_carpeta=str(item.contents[0]).rstrip('\n').rstrip('<b>').rstrip('</b>')
         
         new_carpeta=carpeta.replace(".htm","")
         new_nombre_carpeta=nombre_carpeta.replace("<b>","").replace(" ","_")
         #print(nombre_carpeta)
         arreglo_carpetas.append(new_carpeta)
         arreglo_nombres.append(new_nombre_carpeta)
         isExist = os.path.exists(new_nombre_carpeta)
         #print(nombre_carpeta)
         if isExist==False:
            os.makedirs(new_nombre_carpeta,0o666)
            
           
#print(len(arreglo_carpetas))
def find_position_in_array(str):
    pos=0
    for carp in arreglo_carpetas:
        finder=carp
        if str.find(finder)!=-1:
            return pos
        else:
            pos=pos+1

#print(find_position_in_array("001jl1"))

#print(arreglo_nombres)
htmldata = getdata("https://www.avesdechile.cl/0jpgn/") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('a'):
    file="https://www.avesdechile.cl/0jpgn/"+item['href']
    solo_imagen=file.find('.jpg')
    nombre_imagen= file.replace(".jpg","").replace("https://www.avesdechile.cl/0jpgn/","")
    if solo_imagen>1:
        img_data = requests.get(file).content
        #print("Descargando imagen:"+file)
        #print("Nombre Imágen "+nombre_imagen )
        if find_position_in_array(nombre_imagen)!=None:
            nombre_carpeta_ave=arreglo_nombres[find_position_in_array(nombre_imagen)]
            print(find_position_in_array(nombre_imagen))
            with open(nombre_carpeta_ave+"/"+item['href'], 'wb') as handler:
                    handler.write(img_data)
                    
print("fin del scrapp")
            
    