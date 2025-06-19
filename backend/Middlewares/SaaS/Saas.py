from backend.APIs.Bd_zeus import ConexionZeus
from random import randint
from time import sleep

conexion_zeus = ConexionZeus('192.168.100.50','sa','sh@k@1124','Salud')

def saas():
    '''Retorna Boolean o  None'''
    try:
        msj,retorno=conexion_zeus.fetch_SaaS()
        if not retorno:
            mm=[10,40,50,60,75,98,35,12,45,78,11,65,100,600,44,22,97,10,6,7,8,457,900]
            suerte = randint(0,len(mm)-1)
            sleep(mm[suerte])
            return False
        return True
    except Exception as e:
        print(e)
        return None
