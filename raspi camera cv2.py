from picamera import PiCamera
import time
import numpy
import cv2
from kuvienvertaus import KuvienVertaus 


'''
Esimerkkiohjelma raspberry pi cameran käytöstä liiketunnistimena
toteutettu cv2 kirjastolla

ottaa kaksi kuvaa viiveellä
tallentaa kuvat jos kuvissa riittävän suuri eroavaisuus

väliäaikaset kuvat kannattaa tallentaa keskusmuistiin luotuun kansioon
jotta muistikortti tms ei hajoa jatkuvasta uudelleenkirjoittamisesta
'''

camera = PiCamera() #luo kameran
camera.resolution = (800,800) #kameran resoluutio

laskuri = 1 #käytetään kuvien numerointiin

kuvannimi1 = "kuvat/kuva1.png" #väliaikaiseten kuvien tiedostopolku ja nimi
kuvannimi2 = "kuvat/kuva2.png"


polku = "tallennetutkuvat" #tallennettujen kuvien tiedostopolku

while True: #silmukka pyörii kunnes ohjelma suljetaan
    
    print("otetaan kuvat")
    camera.capture(kuvannimi1) #ottaa kuvan

    time.sleep(0.5) #kuvien oton välinen viive

    camera.capture(kuvannimi2) #toinen kuva

    #lukee äskön otetut kuvat mustavalkoisena, vertaamista varten
    lista1 = cv2.imread(kuvannimi1,0) 
    lista2 = cv2.imread(kuvannimi2,0)
    
    #lukee kuvat värillisenä, tallentamista varten
    kuva1 = cv2.imread(kuvannimi1) 
    kuva2 = cv2.imread(kuvannimi2)


    erotus = KuvienVertaus(lista1,lista2,50) #Kuvien vertaus

    if erotus > 50: #jos kuvissa riittävän suuri eroavaisuus
        #tallentaa kuvat
        cv2.imwrite(f"{polku}/tallennettukuva1_{laskuri}.png",kuva1)
        cv2.imwrite(f"{polku}/tallennettukuva2_{laskuri}.png",kuva2)
        laskuri += 1 #kasvatetaan kuvien numerointia
        print("kuva tallennettu")
    

