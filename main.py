import os
import time
from extract import *
import random
import webbrowser
try:
    import pyautogui
    import pyperclip
except:
    try:
        os.system('pip install pyautogui')
        os.system('pip install pyperclip')
        import pyautogui
        import pyperclip
    except:
        os.system('python -m pip install pyautogui')
        os.system('python -m pip install pyperclip')
        import pyautogui
        import pyperclip
            
def sleepy():
    return time.sleep(1+random.uniform(0,1))


webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("leboncoin.fr")


sleepy()
sleepy()
nbproduit=len(product)
print("je vais déposer "+str(nbproduit)+" produit")

Announcenumber=0

depose= pyautogui.locateOnScreen('img/depose.png')
formx, formy = pyautogui.center(depose)
pyautogui.click(formx, formy)
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
    
    choisir= pyautogui.locateOnScreen('img/choisir.png')
    formx, formy = pyautogui.center(choisir)
    pyautogui.click(formx, formy)
    
    sleepy()
    
    serviceplus= pyautogui.locateOnScreen('img/serviceplus.png')
    formx, formy = pyautogui.center(serviceplus)
    pyautogui.click(formx, formy)
    
    sleepy()
    try:
        prestationservice= pyautogui.locateOnScreen('img/prestationservice.png')
        formx, formy = pyautogui.center(prestationservice)
        pyautogui.click(formx, formy)
    except:
        prestationservice2= pyautogui.locateOnScreen('img/prestationservice2.png')
        formx, formy = pyautogui.center(prestationservice2)
        pyautogui.click(formx, formy)
    
    sleepy()
    
    continuer= pyautogui.locateOnScreen('img/continuer.png')
    formx, formy = pyautogui.center(continuer)
    pyautogui.click(formx, formy)
    sleepy()
    
    pyautogui.press('tab')
    pyperclip.copy(annonce['title'])
    pyautogui.hotkey("ctrl", "v")
    
    pyautogui.press('tab')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('del')
    pyperclip.copy(annonce['desc'])
    pyautogui.hotkey("ctrl", "v")
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    
    pyautogui.press('tab')
    pyperclip.copy(annonce['price'])
    pyautogui.hotkey("ctrl", "v")
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    
    
    sleepy()
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
    pyautogui.press('tab')
    
    pyperclip.copy(annonce['zone'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyautogui.typewrite('\n')
    sleepy()
    for i in range(5):
        pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy()
    
   
    
    deposefinal= pyautogui.locateOnScreen('img/deposefinal.png')
    formx, formy = pyautogui.center(deposefinal)
    pyautogui.click(formx, formy)
    
    
    Announcenumber=Announcenumber+1
    
if __name__=="__main__":
 
    while nbproduit!=0:
        print(" je vais déposer le produit N°: "+str(Announcenumber+1))
        deposite()
        nbproduit=nbproduit-1
        sleepy()
        newdepose= pyautogui.locateOnScreen('img/newdepose.png')
        formx, formy = pyautogui.center(newdepose)
        pyautogui.click(formx, formy)