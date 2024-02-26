import random
from datetime import datetime

'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Roman Pečimúth
email: roman.pecimuth@seznam.cz
discord: romanp._

'''
def vytvoreni_unikatniho_cisla():
    # Vytvoření náhodného čtyřmístného čísla
    while True:
        tajne_cislo = str(random.randint(1000, 9999))
        # Kontrola, zda nezačíná nulou a má 4 unikátní cifry
        if tajne_cislo[0] != "0" and len(set(tajne_cislo)) == 4:
            return tajne_cislo
        
def vypocet_trvani_casu(zacatek, konec):
    # Vypočítá trvání času mezi začátkem a koncem
    cas_trvani = konec - zacatek
    celkove_sekundy = int(cas_trvani.total_seconds())
    cas_minuty = celkove_sekundy // 60
    cas_sekundy = celkove_sekundy % 60
    return cas_minuty, cas_sekundy

def kontrola_vstupu(vstup):
    # Kontrola platnosti vstupu (čtyřmístné číslo s unikátními ciframi)
    if not vstup.isdigit() or len(set(vstup)) != 4 or len(vstup) != 4:
        return False
    return True

def vypocet_bulls_and_cows(hadane_cislo, vstupni_cislo):
    # Porovnání hadaného čísla s uživatelským vstupem
    if hadane_cislo == vstupni_cislo:
        return "uhodnuto"
    
    shodna_pozice_cisla = []
    neshodna_pozice_cisla = []
    
    if int(hadane_cislo) != int(vstupni_cislo):   
        # Porovnání číslic hadaného čísla a uživatelského vstupu
        for cislo1, cislo2 in (zip(hadane_cislo, vstupni_cislo)):
            if cislo1 == cislo2:
                shodna_pozice_cisla.append(cislo1)    
            elif cislo1 != cislo2 in hadane_cislo and vstupni_cislo:
                neshodna_pozice_cisla.append(cislo1)
        return shodna_pozice_cisla, neshodna_pozice_cisla
      
def hodnoceni_vysledku(pocet_hadani, obtiznost):
    konec_hry = {
        1: "Game over! The number got away from you!\n",
        2: "Too bad! Give it another shot!\n",
        3: "Game over! Tough luck, but don't give up!\n"
                }
    nahodne_cislo = random.randint(1, len(konec_hry))
    zprava = konec_hry[nahodne_cislo]
     
    if pocet_hadani >= obtiznost and obtiznost != 0:
         print(zprava)
         
    elif obtiznost == 4:
        return False
    else:
        return True
        
def vypis_casu_hodnoceni(zacatek_casomiry, konec_casomiry):
    cas_minuty, cas_sekundy = vypocet_trvani_casu(zacatek_casomiry, konec_casomiry)
    # casomira 
    if cas_minuty == 1 or cas_minuty == 0:
        minuty_text = "minute"
    else:
        minuty_text = "minutes"
    if cas_sekundy == 1:
        sekundy_text = "second"
    else:
        sekundy_text = "seconds"
        
    print(f"\n| Time spent in the game: {cas_minuty} {minuty_text}, {cas_sekundy} {sekundy_text} |")
       
def vypis_konecne_hodnoceni(pocet_hadani):
    if pocet_hadani <= 3:
        print("That's amazing")
    elif 3 < pocet_hadani <= 6:
        print("That's average")
    elif 6 < pocet_hadani <= 10:
        print("That's not bad")
    elif pocet_hadani > 15:
        print("That's not good")
        
    
    
    
def hra_bulls_and_cows(obtiznost):
    # Generování unikátního čísla pro hru
    hadane_cislo = vytvoreni_unikatniho_cisla()
    
    print(hadane_cislo)      
    oddelovac = "--" * 25
    pocet_hadani = 0
    
    zacatek_casomiry = datetime.now()
    print("Hi there!")

    print(oddelovac)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(oddelovac)
    print("Enter a number: ")
    print(oddelovac)
 
    hra = True
    while hra:
        if not hodnoceni_vysledku(pocet_hadani, obtiznost):
            break
        
        # Uživatelský vstup a zvýšení počtu pokusů
        
        vstupni_cislo = input(">>> ")    
        pocet_hadani += 1
        
        # Kontrola platnosti vstupu
        if not kontrola_vstupu(vstupni_cislo):
            print("Enter only 4-digit unique numbers.")
            print(oddelovac)
            continue
        
        vysledek = vypocet_bulls_and_cows(hadane_cislo, vstupni_cislo)
        
        if vysledek == "uhodnuto": # Uživatel uhodl číslo, výpis výsledku a statistik 
            print(f"Correct, you've guessed the right number in {pocet_hadani} guesses!")
            vypis_konecne_hodnoceni(pocet_hadani)
            
            konec_casomiry = datetime.now()
            
            vypis_casu_hodnoceni(zacatek_casomiry, konec_casomiry)
            print(oddelovac)
            
            hra = False
            # podmínky s počtem pokusů hádání, následný výpis úspěchu při hádání, podle počtu.        
        else:
            shodne, neshodne = vysledek
            # výpis podle počtů bull nebo bulls , cow nebo cows .     
            if len(shodne) == 1 and len(neshodne)  == 1:
                print(f"{len(shodne)} bull, {len(neshodne)} cow")
            elif len(shodne) == 1:
                print(f"{len(shodne)} bull, {len(neshodne)} cows")
            elif len(neshodne) == 1:
                print(f"{len(shodne)} bulls, {len(neshodne)} cow")
            else:
                print(f"{len(shodne)} bulls, {len(neshodne)} cows")
            
            print(oddelovac)

if __name__ == "__main__":
    #1 -> 15 pokusů , 2 -> 10 pokusů, 3 -> 5 pokusů, 4 -> dokud uživatel neuhodne číslo
    obtiznost = input("""Select Game Difficulty:
                        1 -easy 
                        2 -medium
                        3 -Hard
                        4 -No limit\n Enter a Number: """) 
    
    if not obtiznost.isalpha():
        obtiznost_cislo = int(obtiznost)
        
        if obtiznost_cislo == 1:
            hra_bulls_and_cows(15)
        elif obtiznost_cislo == 2:
            hra_bulls_and_cows(10)
        elif obtiznost_cislo == 3:
            hra_bulls_and_cows(5)
        elif obtiznost_cislo == 4:
            hra_bulls_and_cows(0)
    else:
        print("Invalid input. Please enter a valid number (1-4).")
    
    
    
    
        
       
    

    



 
 
        


        
        


        
        

