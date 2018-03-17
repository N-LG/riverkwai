#!/usr/bin/python3.4
#
# 1-demarrer l'execution de ce script
# 2-lancer le jeu
# 3-choisir le job barde et choisissez votre instrument
# 4-appuyer sur la touche F2 chaque fois que vous voulez jouer la musique

base = 0.5  #base de temp du déroulé de la musique, diminuer pour accelerer le tempo


import time
import ctypes
user32 = ctypes.WinDLL('user32.dll')

def lire(chaine,tempo):
    for i in chaine:
        user32.keybd_event(ord(i),0,0,0)
        time.sleep(base * tempo)
        user32.keybd_event(ord(i),0,2,0)
  
    return

def lireM(chaine,tempo):
    for i in chaine:
        user32.keybd_event(0x11,0x9d,0 , 0)  #ctrl
        user32.keybd_event(ord(i),0,0,0)
        time.sleep(base * tempo)
        user32.keybd_event(ord(i),0,2,0)
        user32.keybd_event(0x11,0x9d,2 , 0)
    return

def lireP(chaine,tempo):
    for i in chaine:
        user32.keybd_event(0x10,0xAA,0,0)    #shift
        user32.keybd_event(ord(i),0,0,0)
        time.sleep(base * tempo) 
        user32.keybd_event(ord(i),0,2,0)
        user32.keybd_event(0x10,0xAA,2,0)
         
    return

def pause(tempo):
    time.sleep(base * tempo)  
    return 

while True:
    print ("j'attend que la touche F2 soit pressé")
    val = 0
    while (val & 128)==0:
        val=user32.GetKeyState(0x71) #code de touche F2

    lire("IY",0.5)
    pause(1.5)
    lire("YUI",0.5)
    lireP("Y",0.5)
    pause(0.5)
    lireP("Y",0.5)
    pause(0.5)
    lireP("R",2)
    lire("IY",0.5)
    pause(1.5)
    lire("YUYI",0.5)
    pause(0.5)
    lire("I",0.5)
    pause(0.5)
    lire("U",2)
    lire("UT",0.5)
    pause (1.5)
    lire("TYUIY",0.5)
    pause(1.5)
    lire("YUYTI",0.5)
    pause(0.5)
    lire("YUT",0.5)
    pause(0.5)
    lireP("Z",0.5)
    lire("I",4)


    print ("la musique a été joué!")

    


    
    





