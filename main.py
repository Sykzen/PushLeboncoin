import os
import time
from extract import *
import random
import webbrowser
import pyautogui
import pyperclip

def sleepy():#sleep for 1second and few millisecond
    return time.sleep(1+random.uniform(0,1))


webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("leboncoin.fr")


nbproduit=len(product)
print("je vais déposer "+str(nbproduit)+" produit")

Announcenumber=0
            
                    
pyautogui.hotkey("alt", "esc")
sleepy()
sleepy()
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('\n')
        
        
def deposephoto(val,i):
 
        
    addphoto= pyautogui.locateOnScreen('img/addphoto.png')
    formx, formy = pyautogui.center(addphoto)
    pyautogui.click(formx, formy)
    pyperclip.copy(nbphoto(val)[i])
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    
    pyautogui.typewrite('\n')
trace=Announcenumber
def deposite():
    #cliquer sur déposer
    global Announcenumber
    annonce=chget(Announcenumber)
    sleepy()
    escal1= pyautogui.locateOnScreen('img/escal1.png')
    formx, formy = pyautogui.center(escal1)
    pyautogui.click(formx, formy)
    pyautogui.press('tab')
    pyperclip.copy(annonce['title'])
    pyautogui.press('del')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    
    sleepy()
    # Click on Choisissez une autre catégorie
    choisir= pyautogui.locateOnScreen('img/choisir.png')
    formx, formy = pyautogui.center(choisir)
    pyautogui.click(formx, formy)
    
    sleepy()
    # Click on Categorie
    categorie= pyautogui.locateOnScreen("img/Categorie/"+annonce['cat']+".png")
    formx, formy = pyautogui.center(categorie)
    pyautogui.click(formx, formy)
    
    sleepy()
    # Click on Sous Categorie
    try:
        souscategorie= pyautogui.locateOnScreen('img/SousCategorie/'+annonce['souscat']+'.png')
        formx, formy = pyautogui.center(souscategorie)
        pyautogui.click(formx, formy)
    except:
        souscategorie2= pyautogui.locateOnScreen('img/SousCategorie/'+annonce['souscat']+'2.png')
        formx, formy = pyautogui.center(souscategorie2)
        pyautogui.click(formx, formy)
    
    sleepy()
    # Click on Continuer
    continuer= pyautogui.locateOnScreen('img/continuer.png')
    formx, formy = pyautogui.center(continuer)
    pyautogui.click(formx, formy)
    sleepy()
    # type Title
    pyautogui.press('tab')
    pyperclip.copy(annonce['title'])
    pyautogui.hotkey("ctrl", "v")
    # type Description
    pyautogui.press('tab')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('del')
    pyperclip.copy(annonce['desc'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    # type Price
    pyautogui.press('tab')
    pyperclip.copy(annonce['price'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy()
    # Post Image
    if Announcenumber==trace:
        for i in range(3):
            try:
                quite= pyautogui.locateOnScreen('img/quit.png')
                formx, formy = pyautogui.center(quite)
                pyautogui.click(formx, formy)
            except:
                pass
    for i in range(len(nbphoto(Announcenumber))):
        deposephoto(Announcenumber,i)
        sleepy()
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy()
    # type Zone
    pyautogui.press('tab')
    pyperclip.copy(annonce['zone'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    sleepy()
    pyautogui.typewrite('\n')
    sleepy()
    # type Continue
    for i in range(5):
        pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy()
    
   
    
    deposefinal= pyautogui.locateOnScreen('img/deposefinal.png')
    formx, formy = pyautogui.center(deposefinal)
    pyautogui.click(formx, formy)
    
    
    Announcenumber=Announcenumber+1
    
if __name__=="__main__":
 
    while (nbproduit-trace)!=0:
        print(" je vais déposer le produit N°: "+str(Announcenumber+1))
        deposite()
        nbproduit=nbproduit-1
        sleepy()
        newdepose= pyautogui.locateOnScreen('img/newdepose.png')
        formx, formy = pyautogui.center(newdepose)
        pyautogui.click(formx, formy)