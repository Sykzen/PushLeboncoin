import os
try:
    import pandas as pd
except:
    try:
        os.system('pip install pandas')
        import pandas
    except:
        os.system('python -m pip install pandas')

try:
    os.system('eftkrt')==0
except:
    print('work')
product=pd.read_excel('product.xlsx')

def chget(val):
    product=pd.read_excel('product.xlsx')
    
    minidicte={}
    keysProduct=["Titre","Prix","Zone","Photos0","Photos1","Photos2",'description']
    keysMydict=['title',"price","zone","p0","p1","p2",'desc']
    for e,i in enumerate(keysMydict):
        minidicte[i]=str(product[keysProduct[e]][val])
    return minidicte
def nbphoto(val):
    truphoto=[]
    liste=[chget(val)["p"+str(j)] for j in range(3)]
    for i in liste:
        if i!="":
            truphoto.append(i)
    return truphoto
            
    