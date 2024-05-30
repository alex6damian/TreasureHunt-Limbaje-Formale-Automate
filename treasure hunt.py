import dfa_checker
import cs112_passer

c=cs112_passer.load_file("dfa3.cfg") # citirea fisierului

s=cs112_passer.get_section_list(c) # extragerea sectiunilor

stari=cs112_passer.get_section_content(s, "States") # extragerea starilor

transitions=cs112_passer.get_section_content(s,"Transitions") # # extragerea tranzitiilor

curent=cs112_passer.get_section_content(s,'S') # extragerea starii curente

curent=curent[0] # extragerea starii curente

final=cs112_passer.get_section_content(s, 'F') # extragerea starilor finale

string=input() # citirea stringului

sabie=0 # initializare sabie

mort=0 # initializare mort

key=0 # initializare cheie

items=[0,0] # initializare lista

for s in string: # parcurgerea stringului
    for t in transitions: # parcurgerea tranzitiilor
        if t[0] == curent and s==t[1]: # verificare daca tranzitia este posibila
            curent=t[2] # schimbarea starii curente
            if curent=='c3': # verificare daca am ajuns la c3
                items[1]=1 # setare sabie
            if curent=='c6': # verificare daca am ajuns la c6
                items[0]=1 # setare cheie
                final='c4' # setare stare finala
            break # iesire din for
    if curent == 'c5' and items[1] == 0: # verificare daca am ajuns la c5 si nu avem sabie
        break

if curent in final and items[0]==1: # verificare daca starea curenta este finala si avem cheie
    print("Acceptat") # afisare acceptat
else:
    print("Respins") # afisare respins