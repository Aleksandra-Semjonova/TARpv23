#print("Tere maailm!")
#nimi=input("Mis on sinu nimi?") 
#vanus=int(input("Kui vana sa oled?")) #float()->2.5
#print("Tere tulemast! "+nimi+". Sa oled"+str(vanus)+" aastat vana" #с помощью str будет воспринимать цифры за текст
#print("Tere tulemast!",nimi,". Sa oled",vanus,"aastat vana") #если запятая то дальше все пишем через нее
#print("Tere tulrmast! {0} Sa oled {1} aastat vana".format(nimi,vanus)) #меняется толлько то что в фигруных скобках
#print("Muutuja vanus=",vanus,"tüüp on",type(vanus))
#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True
#print("Muutuja vanus=",vanus,"tüüp on",type(vanus))
#print("Muutuja eesnimi=",eesnimi,"tüüp on",type(eesnimi))
#print("Muutuja pikkus=",pikkus,"tüüp on",type(pikkus))
#print("Muutuja kas_käib_koolis=",kas_käib_koolis,"tüüp on",type(kas_käib_koolis))
#3
from random import *
kokku=randint(10,100)
print("kokku: ",kokku)
mitu=int(input("Mitu kommi tahad võtta?"))
kokku=mitu
print("Nüüd laua peal on",kokku,"kommid")
4