import numpy



def KuvienVertaus(kuva1,kuva2,erotus):
    '''
    saa parametriksi kuvat 2-ulotteisessa listassa (numpy array)
    Funktio tarvitsee numpyn, mutta ei muita kirjastoja
    sekä kuinka suuri kirkkasu ero pitää olla (pienempi luku herkempi)
    
    palauttaa kirkkauseron ylittävien pikseleiden lukumäärän
    
    Listojen mittojen tulisi olla samoja
    '''
    


    lista1 = kuva1.tolist() #numpy array normaaliksi listaksi
    lista2 = kuva2.tolist() #numpy array normaaliksi listaksi

    #listat läpikäyntiä varten
    kuva1 = lista1 
    kuva2 = lista2

    laskuri = 0 

    #luodaan listat
    for i in range(len(kuva1)):
        for j in range(len(kuva1[1])):
            lista1[i][j] = kuva1[i][j]  #kirkkausalue talteen
            
    for i in range(len(kuva2)):
        for j in range(len(kuva2[1])):
            lista2[i][j] = kuva2[i][j] #kirkkausalue talteen


    #Vertaillan listoja
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            if lista1[i][j] != lista2[i][j]:
                if abs(lista1[i][j] - lista2[i][j]) > erotus: #kirkkaudessa pitää olla riittävän suuri ero
                    laskuri += 1

    return(laskuri)








if __name__ == "__main__": #tesiohjelma
    import cv2 #tätä kirjastoa ei tarvita funktion toimimista varten
    kuvannimi1 = "kuva1.png"

    kuvannimi2 = "kuva2.png"


    img1 = cv2.imread(kuvannimi1,0) #lukee kuvan 2-ulotteiseen taulukkoon


    img2 = cv2.imread(kuvannimi2,0) #lukee kuvan 2-ulotteiseen taulukkoon





    print(KuvienVertaus(img1,img2,30)) #kutsutaan funktiota
