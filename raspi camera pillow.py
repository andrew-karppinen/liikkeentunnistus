from picamera import PiCamera
import time
import numpy
from kuvienvertaus import KuvienVertaus 
from PIL import Image

'''
Esimerkkiohjelma raspberry pi cameran käytöstä liiketunnistimena
toteutettu pillow kirjastolla

ottaa kaksi kuvaa viiveellä
tallentaa kuvat jos kuvissa riittävän suuri eroavaisuus

väliäaikaset kuvat kannattaa tallentaa keskusmuistiin luotuun kansioon
jotta muistikortti tms ei hajoa jatkuvasta uudelleenkirjoittamisesta
'''

camera = PiCamera() #luo kameran
camera.resolution = (500,500) #kameran resoluutio

laskuri = 1 #käytetään kuvien numerointiin

kuvannimi1 = "kuvat/kuva1.png" #väliaikaiseten kuvien tiedostopolku ja nimi
kuvannimi2 = "kuvat/kuva2.png"


polku = "tallennetutkuvat" #tallennettujen kuvien tiedostopolku

while True: #silmukka pyörii kunnes ohjelma suljetaan
    
    print("otetaan kuvat")
    camera.capture(kuvannimi1) #ottaa kuvan

    time.sleep(0.5) #kuvien oton välinen viive

    camera.capture(kuvannimi2) #toinen kuva

    #lukee äskön otetut kuvat mustavalkoisena vertaamista varten
    lista1 = numpy.array(Image.open(kuvannimi1).convert('L')) #lukee kuvan 2d taulukkoon mustavalkoisena
    lista2 = numpy.array(Image.open(kuvannimi2).convert('L')) #lukee kuvan 2d taulukkoon mustavalkoisena
    
    #luetaan kuvat värillisenä tallentamista varten
    kuva1 =  Image.open(kuvannimi1)
    kuva2 = Image.open(kuvannimi2)

    erotus = KuvienVertaus(lista1,lista2,65) #Kuvien vertaus
    


    if erotus > 60: #jos kuvissa riittävän suuri eroavaisuus
        #tallentaa värilliset kuvat
        kuva1.save(f"{polku}/tallennettukuva1_{laskuri}.png")
        kuva2.save(f"{polku}/tallennettukuva2_{laskuri}.png")
        laskuri += 1 #kasvatetaan kuvien numerointia
        print("kuva tallennettu")
    
