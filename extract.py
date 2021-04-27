import os
import pandas as pd


product=pd.read_excel('product.xlsx')

def chget(val):
    product=pd.read_excel('product.xlsx')
    
    minidicte={}
    keysProduct=["Titre","Prix","Zone","Photos0","Photos1","Photos2",'description',"Catégorie","Sous-Categorie","Informations"]
    keysMydict=['title',"price","zone","p0","p1","p2",'desc',"cat","souscat","inf"]
    for e,i in enumerate(keysMydict):
        minidicte[i]=str(product[keysProduct[e]][val])
    return minidicte
def nbphoto(val):
    truphoto=[]
    liste=[chget(val)["p"+str(j)] for j in range(3)]
    for i in liste:
        if i!="nan":
            truphoto.append(i)
    return truphoto

        

    