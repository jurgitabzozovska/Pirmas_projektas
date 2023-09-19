 # 09-11 PAMOKA OBJEKTINIS PROGRAMAVIMAS
# ***********************1. UZDUOTIS
##     sukuriama klase
# class Zmogus:
#
##     sukuriamas konstruktorius
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
##      sukuriami metodai
#     def sveikinimas(self):
#         return f"Sveiki, as esu {self.vardas} ir man yra {self.amzius} metu"
#
#
##     sukuriamas objektas
# zmogus1 = Zmogus("Migle", 30)
# zmogus2 = Zmogus("Antanas", 45)
# print(zmogus1.sveikinimas())
# print(zmogus2.sveikinimas())


# ***********************2. UZDUOTIS
# class Automobilis:
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#         self.greitis = 0
#
#     def akseleratorius(self):
#         self.greitis += 10
#
#     def stabdis(self):
#         self.greitis -= 5
#
#     def info(self):
#         return f'{self.marke} {self.modelis}, greitis: {self.greitis} km/h'
#
# auto1=Automobilis('Mazda', '323')
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.stabdis()
# print(auto1.info())

# ***********************3. UZDUOTIS
# class Knyga:
#     def __init__(self, pavadinimas, autorius, leidimo_metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.leidimo_metai = leidimo_metai
#
#     def info(self):
#         return f'Knygos pavadinimas: {self.pavadinimas}, autorius: {self.autorius}, leidimo metai: {self.leidimo_metai}'
# knyga1 = Knyga('Saule', 'Jurgita', '2023')
# print(knyga1.info())

#
# ***********************4. UZDUOTIS
# class Preke:
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#     def info(self):
#         return f'{self.pavadinimas}: {self.kaina} eurų'
#
# class Krepselis:
#     def __init__(self):
#
#         self.prekes = []
#
#     def ideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def krepselio_info(self):
#         if not self.prekes:
#             print("tokios prekes nera")
#         else:
#             print("krepselio turinys: ")
#             for preke in self.prekes:
#                 print(preke.info())
#     def bendra_suma(self):
#         suma = sum(preke.kaina for preke in self.prekes)
#         return suma
#
# krepsys = Krepselis()
# preke1 = Preke('obuolis', 5.0)
# preke2 = Preke('bananas', 2.2)
# preke3 = Preke('vanduo', 1.3)
# preke4 = Preke('kava', 10.5)
#
#
# krepsys.ideti_preke(preke1)
# krepsys.ideti_preke(preke2)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke4)
#
#
# krepsys.krepselio_info()
#
# print(f'Bendra suma: {krepsys.bendra_suma()} eurų')


# 5. UZDUOTIS***PADARYTA
## Sukurkite klasę "Studentas", kuri turėtų šias savybes:
##     * vardas: studento vardas.
##     * pazymiai: sąrašas su studento pažymiais.
##
## Sukurkite klasę "Mokytojas", kuri turėtų šias savybes:
##     * vardas: mokytojo vardas.
##     * Mokytojo dėstoma tema: mokytojo dėstomas dalykas.
##
## Papildykite "Studentas" klasę metodu vidurkis(), kuris apskaičiuoja studento pažymių vidurkį.
## Papildykite "Mokytojas" klasę metodu ivertinimas(studentas, pazymys), kuris prideda studentui pažymį.
## Sukurkite objektus pagal "Studentas" ir "Mokytojas" klases, pridėkite pažymius ir vykdykite vidurkio apskaičiavimus bei pažymių pridėjimus.

# class Studentas:
#     def __init__(self, st_vardas):
#         self.st_vardas = st_vardas
#         self.pazymiai = []
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mokytojo_vardas, destomas_dakykas):
#         self.mokytojo_vardas = mokytojo_vardas
#         self.destomas_dalykas = destomas_dakykas
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1=Studentas('Petras')
# mokytojas1=Mokytojas('Jurgis', 'informatika')
#
# mokytojas1.ivertinimas(studentas1, 3)
#
# print(f'{studentas1.st_vardas}, vidurkis: {studentas1.vidurkis()}')

## UZDUOTIS
## Sukurkite klasę "Saskaita", kuri turėtų šias savybes ir metodus:
##     * 1.saskaitos_nr: sąskaitos numeris.
##   * 2.balansas: sąskaitos balansas (numatytasis pradžioje yra 0).
##     * inesti(suma): metodas, kuris prideda nurodytą sumą prie sąskaitos balanso.
##    * isimti(suma): metodas, kuris sumažina sąskaitos balansą nurodyta suma,
## jei yra pakankamai lėšų, arba išveda pranešimą apie nepakankamą balansą.
##    * informacija(): metodas, kuris grąžina informaciją apie sąskaitą (sąskaitos numeris ir balansas).
## Sukurkite bent du objektus pagal šią klasę ir atlikite operacijas, tokiu kaip lėšų įnešimas ir išėmimas, bei gaukite sąskaitos informaciją.

# class Saskaita:
#     def __init__(self, saskaitos_nr, balansas=0):
#         self.saskaitos_nr = saskaitos_nr
#         self.balansas = balansas
#         print(f'Sveiki atvyke i savo banko saskaita!')
#
#     def inesimo_suma(self,suma):
#         self.balansas += suma
#
#     def isemimo_suma(self,suma):
#             if self.balansas >=suma:
#                self.balansas -=suma
#                print(f'Jus isemete: {suma}')
#
#             else:
#                 print("Nepakankamas likutis")
#
#     def info(self):
#         return f'Saskaitos numeris: {self.saskaitos_nr}, saskaitos balansas: {self.balansas}'
#
# saskaita1= Saskaita('LT110', 2000)
# saskaita1.isemimo_suma(125)
# print(saskaita1.info())

## UZDUOTIS
## Sukurkite klasę "Kava", kuri turėtų savybes "pavadinimas", "kaina", ir "talpa".
## Parašykite metodą, kuris patikrintų, ar ši kava yra tinkama tam tikram puodeliui, pagal jo talpą.
#
# class Kava:
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#     def ar_tinkama_puodeliui(self, puodelio_talpa):
#         if self.talpa <= puodelio_talpa:
#             return f'{self.pavadinimas} kava tinka puodeliui su talpa {puodelio_talpa}ml'
#         else:
#             return  f'{self.pavadinimas} kava netelpa {puodelio_talpa}ml'
#
# kava1=Kava('Latte', 2.99, 250)
# puodelio_talpa=200
# print(kava1.ar_tinkama_puodeliui(puodelio_talpa))

## UZDUOTIS
## Klase knygynas, kuris turi knygas, sarasa, prideti ir\

# class Knygynas:
#     def __init__(self):
#         self.knygos = []
#     def prideti_knyga(self,knyga):
#         self.knygos.append (knyga)
#
#     def knygos_paieska(self,pavadinimas):
#         for knyga in self.knygos:
#             if knyga['pavadinimas'] == pavadinimas:
#                 return knyga
#         return None
#
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print('Knygynas tuscias')
#         else:
#             print('Knygyno knygu sarasas:')
#             for knyga in self.knygos:
#                 print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}")
# knygynas = Knygynas()
# knygynas.prideti_knyga({'pavadinimas': 'Ruduo', 'autorius': 'Donelaitis', 'metai': 69})
# ieskoma_knyga = knygynas.knygos_paieska('Ruduo')
# if ieskoma_knyga:
#     print(f'rasta knyga:{ieskoma_knyga["pavadinimas"]}')
# else:
#     print('knyga buvo nerasta')
# knygynas.knygu_sarasas()


## UZDUOTIS
## Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
## Parašykite metodus, kurie leidžia pridėti prekes prie prekių sąrašo, pašalinti prekes ir paskaičiuoti prekių bendrą sumą;
####SUKURIAMA KLASE
####SUKURIAMAS KONSTRUKTORIUS
####SUKURIAMI METODAI
####SUKURIAMAS OBJEKTAS

# class Prekybininkas:
#     def __init__(self, name):
#         self.name = name
#         self.prekes = []
#     def prideti_preke(self, preke, kiekis=1):
#         for _ in range(kiekis):
#             self.prekes.append(preke)
#     def pasalinti_preke(self, preke, kiekis=1):
#         if preke in self.prekes:
#            for _ in range(kiekis):
#                self.prekes.remove(preke)
#         else:
#             print("tokios prekes nera")
#
#     def prekiu_suma(self):
#         suma=sum(preke[1] for preke in self.prekes)
#         return suma
#
#
# pardavejas=Prekybininkas("Martynas")
# preke1=("kava", 1.0)
# preke2=("sultys", 2.5)
# preke3=("alus", 1.5)
#
# pardavejas.prideti_preke(preke1, 3)
# pardavejas.prideti_preke(preke2)
# pardavejas.prideti_preke(preke3,3)
# suma=pardavejas.prekiu_suma()
#
# print(suma)
#
# pardavejas.pasalinti_preke(preke1, 2)
# pardavejas.pasalinti_preke("preke4")
# suma=pardavejas.prekiu_suma()
#
# print("prekiu sarasas: ")
# for preke in pardavejas.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"bendra visu prekiu suma:{suma}")



## UZDUOTIS
## Sukurkite klasę "Darbuotojas" (Employee), kuri turi atributus "vardas" (name), "pareigos" (position), ir "atlyginimas" (salary).
## Parašykite metodus, kurie leidžia keisti darbuotojo pareigas ir atlyginimą;
####SUKURIAMA KLASE
####SUKURIAMAS KONSTRUKTORIUS
####SUKURIAMI METODAI
####SUKURIAMAS OBJEKTAS


# class Darbuotojas:
#     def __init__(self, vardas, pareigos, alga):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.alga = alga
#     def pakeisti_alga(self, nauja_alga):
#         self.alga = nauja_alga
#     def pakeisti_pareigas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
#
#
# #
# darbuotojas1=Darbuotojas("Jonas", "vairuotojas", 500)
# darbuotojas1.pakeisti_alga(1500)
# darbuotojas1.pakeisti_pareigas("vadybininkas")
#
# print(f"{darbuotojas1.vardas}, pareigos: {darbuotojas1.pareigos}, gaunama alga:{darbuotojas1.alga}")





## UZDUOTIS
## Sukurkite klasę "Skaičiuotuvas", kuri turi metodus "sudėti" (add), "atimti" (subtract), "dauginti" (multiply) ir "dalinti" (divide).
## Šie metodai priima du skaičius ir atlieka atitinkamą matematinę operaciją.
####SUKURIAMA KLASE
####SUKURIAMAS KONSTRUKTORIUS
####SUKURIAMI METODAI
####SUKURIAMAS OBJEKTAS

# class Skaiciuotuvas:
#     def add(self, a, b):
#        return a+b
#     def subtract(self, a, b):
#         return a-b
#     def multiply(self, a, b):
#         return a*b
#     def divide(self, a,b):
#         if b == 0:
#             return "dalyba is 0 negalima"
#         else:
#             return a/b
#
# a=3
# b=5
#
# a1=Skaiciuotuvas()
# suma=a1.add(a,b)
# skirtumas=a1.subtract(a,b)
# dalyba=a1.multiply(a,b)
# daugyba=a1.divide(a,b)
#
# print(f"{suma}, {skirtumas}, {dalyba}, {daugyba}")

# Sukurkite klasę "Klase", kuri turės savybę "pavadinimas" ir sąrašą "pamokos" (pamokų pavadinimai ir laikas).
# Sukurkite klasę "Mokykla", kuri turės sąrašą klasių. Parašykite metodą, kuris išveda mokyklos tvarkaraštį su visomis pamokomis.

# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.pamokos = []
#
#     def sukurti_pamoka(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#
#     def tvarkarastis(self):
#         tvarkarastis = f"Klase: {self.pavadinimas} \n"
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis += f"- {pavadinimas}, laikas: {laikas} \n"
#         return tvarkarastis
#
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#
#     def sukurti_klase(self, klase):
#         self.klases.append(klase)
#
#     def Tvarkarastis_galutinis(self):
#         galutinis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis += klase.tvarkarastis()
#         return galutinis
#
#
#
# klase1 = Klase("Ziopliu 9A")
# klase1.sukurti_pamoka("Nosiakrap6tis", "8:00-8:45")
# klase1.sukurti_pamoka("Kalbagrauzis", "9:00-9:45")
#
# klase2 = Klase("Smalsučiai gudručiai 1B")
# klase2.sukurti_pamoka("Priešpiečiai", "10:00-10:45")
# klase2.sukurti_pamoka("Kalbagrauzis", "11:00-11:45")
#
# mokykla =Mokykla("Tinginių pantys")
#
# mokykla.sukurti_klase(klase1)
# mokykla.sukurti_klase(klase2)
#
# tvarkarastis = mokykla.Tvarkarastis_galutinis()
#
# print(mokykla.Tvarkarastis_galutinis())

# Sukurkite klasę "Žaislas", kuri turėtų savybes, tokias kaip "pavadinimas" ir "amžiaus rekomendacija".
# Tada sukurkite klasę "Vaikas", kuri turėtų vardą ir amžių.
# Tada sukurkite klasę "VaikasSuZaislu", kuri turėtų šio vaiko objektą ir žaislo objektą.
# Patikrinkite, ar vaiko amžius atitinka žaislo amžiaus rekomendaciją.

# class Zaislas:
#     def __init__(self,pavadinimas, amziaus_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amziaus_rekomendacija = amziaus_rekomendacija
#
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius =amzius
#
# class VaikasSuZaislu:
#     def __init__(self,vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#     def amziaus_tikrinimas(self):
#         if self.vaikas.amzius >=self.zaislas.amziaus_rekomendacija:
#             return f'{self.vaikas.vardas} gali zaisti su zaislu "{self.zaislas.pavadinimas}" '
#         else:
#             return f'{self.vaikas.vardas} negali zaisti su zaislu "{self.zaislas.pavadinimas}", nes turi paaugti '
#
#
# zaislas1=Zaislas('Lego Betmen', 7)
# zaislas2=Zaislas('burbulai', 15)
# zaislas3=Zaislas('knyga', 8)
#
# vaikas1=Vaikas('Austeja',9)
# vaikas2=Vaikas('Eidvile', 0.5)
# vaikas3=Vaikas('Giedrius', 5)
#
# vaikas_su_zaislu1=VaikasSuZaislu(vaikas1, zaislas2)
#
# rezultatas = vaikas_su_zaislu1.amziaus_tikrinimas()
# print(rezultatas)

# Sukurkite programą, kuri leidžia vartotojui valdyti krepšinio komandą.
# Galite kurti klases, pvz., "Komanda", "Žaidėjas", "Treneris".
# Kiekvienas žaidėjas turėtų turėti savo statistiką(taiklumas,pozicija), o treneris - instrukcijas ir strategiją(komandos sudeti).
# Programa turi leisti vartotojui pridėti naujus žaidėjus, juos treniruoti ir valdyti komandos sudeti.
# class Treneris:
#     def __init__(self):
#         self.strategija = "ataka"
#     def keisti_strategija(self,nauja_strategija):
#         self.strategija = nauja_strategija
#
#     def strategijos_info(self):
#         return f'naudojama strategija {self.strategija}'
# class Zaidejas:
#     def __init__(self, pavarde, pozicija):
#         self.pavarde = pavarde
#         self.taiklumas = 30
#         self.pozicija = pozicija
#
#     def upgrade(self):
#         self.taiklumas += 5
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#
#     def zaidejo_info(self):
#         return f'{self.pavarde}, zaidejo pozicija {self.pozicija}, ir jo taiklumas {self.taiklumas}%'
# class Komanda:
#     def __init__(self, pavadinimas):
#         self.komanda =[]
#         self.pavadinimas = pavadinimas
#         self.treneris = Treneris()
#     def prideti_zaideja(self,zaidejas):
#         self.komanda.append(zaidejas)
#
#     def isimti_zaideja(self, zaidejas):
#         if zaidejas in self.komanda:
#             self.komanda.remove(zaidejas)
#     def komandos_informacija(self):
#         print(f'{self.pavadinimas}, komandos zaidejai: ')
#         for zaidejas in self.komanda:
#             print(zaidejas.zaidejo_info())
#     def strategijos_info(self):
#         print (self.treneris.strategijos_info())
#
#     def pasirinkti_treneri(self, treneris):
#         self.komanda.append(treneris)
#
#     def pakeisti_treneri(self, treneris):
#         if treneris in self.komanda:
#             self.komanda.remove(treneris)
#
# komanda=Komanda("Puseles")
# zaidejas1=Zaidejas("Greitas", "puolejas")
# zaidejas2=Zaidejas("didelis", "saugas")
# zaidejas3=Zaidejas("vidutinis", "atsarginis")
#
# komanda.prideti_zaideja(zaidejas1)
# komanda.prideti_zaideja(zaidejas2)
# komanda.prideti_zaideja(zaidejas3)
#
# zaidejas1.upgrade()
# zaidejas1.upgrade()
# zaidejas3.upgrade()
#
# komanda.komandos_informacija()
# komanda.strategijos_info()