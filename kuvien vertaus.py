import cv2
import numpy

kuvannimi1 = "kuva.png"

kuvannimi2 = "kuva2.png"

try:
    img1 = cv2.imread(kuvannimi1,0) #lukee kuvan 2-ulotteiseen taulukkoon
except: #jos kuvaa ei löydy
    print("Kuvaa1 ei löytynyt")
    exit()


try:
    img2 = cv2.imread(kuvannimi2,0) #lukee kuvan 2-ulotteiseen taulukkoon
except: #jos kuvaa ei löydy
    print("Kuvaa2 ei löytynyt")
    exit()




x = len(img1[1]) #kuvan leveys
y = len(img1) #kuvan korkeus



while(y > 200 and x > 200): #pienentää kuvan mittoja kunnes leveys tai korkeus on 200
    y -= 1
    x -= 1



img1 = cv2.resize(img1, (x,y), interpolation= cv2.INTER_LINEAR) #muuttaa kuvan koon
img2 = cv2.resize(img2, (x,y), interpolation= cv2.INTER_LINEAR) #muuttaa kuvan koon


a = img1.tolist() #numpy array normaaliksi listaksi
b = img2.tolist()#numpy array normaaliksi listaksi

lista1 = numpy.zeros((len(a),len(a[1])))#korkeus, leveys
lista2 = numpy.zeros((len(b),len(b[1])))#korkeus, leveys

lista1 = img1.tolist() #numpy array normaaliksi listaksi
lista2 = img1.tolist() #numpy array normaaliksi listaksi





luku = 255 // 10 #tummuusalueiden määrä

for i in range(len(a)):
    for j in range(len(a[1])):
        if a[i][j] // luku -1 >= 0: #tutkitaan pikselin tummuutta
            lista1[i][j] = a[i][j] // luku
    
for i in range(len(b)):
    for j in range(len(b[1])):
        if b[i][j] // luku -1 >= 0: #tutkitaan pikselin tummuutta
            lista2[i][j] = a[i][j] // luku
    
    
if lista1 == lista2:
    print("joo")