

# import  random




# mano komentaras
# """
# multi_line
# """
# vardas = "Jurgita"
# print(vardas)
# skaicius = 25
# print(skaicius)
# print("manos sugalvotas skaicius" + str(skaicius))

# true_or_false = false
# print(type(true_or_false))
# fruits = ['apple', 'orange', 'kivi', 'watermelon']
# lietuvos_pilieis = {
# 'id': 1,
# 'vardas': 'Antanas',
# 'Amzius': 34,
# 'Miestas': 'Klaipeda'
# }
# print(lietuvos_pilieis)


# # print(type(fruits))
#
#
# # lietuvos_pilietis = {
# #     'id': 1,
# #     'Vardas': 'Antantas',
# #     'Amzius': 34,
# #     'Miestas': 'Klaipeda'
# # }
# # # print(lietuvos_pilietis)
# # print("Pries:")
# # print("Vardas: ", lietuvos_pilietis["Vardas"])
# # print("Po: ")
# # lietuvos_pilietis['Vardas'] = "Giedrius"
# # print("Vardas: ", lietuvos_pilietis["Vardas"])
# # # print(type(fruits))
# # temperaturos = [20,25,22,18,12]
# # suma = sum(temperaturos)
# #
# # kiekis = len(temperaturos)
# # # print(kiekis)
# #
# # vidutine_temp = suma/kiekis
# # print("Vidutine temperatura yra: ", vidutine_temp)
#
# # 1. Sukurkite kintamąjį vardas ir priskirkite jam savo vardą. Tada parašykite programą,
# # kuri išspausdina sveikinimo žinutę su jūsų vardu;
# # Vardas = "Jurgita"
# # print(Vardas)
#
# # 2. Sukurkite kintamuosius skaicius1 ir skaicius2, ir priskirkite jiems du skaičius.
# # Parašykite programą, kuri juos sudeda ir išspausdina sumą.
# # Skaicius1 = 100
# # Skaicius2 = 99
# # print(Skaicius1 + Skaicius2)
#
# # 3. Parašykite programą, kuri prašo vartotojo įvesti skaičių ir nustato, ar tai yra lyginis ar nelyginis skaičius.
# #
# # 4. Sukurkite žodyną pavadinimu telefonu_knygute, kuriam raktai yra žmonių vardai, o reikšmės - jų telefono numeriai.
# # Parašykite programą, kuri leidžia vartotojui ieškoti telefono numerio pagal žmogaus vardą.
# # Telefono_knyga = {
# #     'Jurgis': '123456789',
# #     'Antanas': '234567890',
# #     'Aloyzas': '345678901',
# #     'Martynas': '456789012'   }
# # print("Jurgis: ", Telefono_knyga["Jurgis"])
#
# # 5. Sukurkite žodyną pavadinimu produktai, kuriame saugosite prekių pavadinimus ir jų kainas.
# # Parašykite programą, kuri suranda pigiausią produktą ir išspausdina jo pavadinimą ir kainą.
#
# # Produktai = {
# #     'Pienas': '1.99',
# #     'Duonas': '1',
# #     'Sviestas': '2',
# #     'Ledai': '0.55'
# # }
# # print(Produktai)
#
#
#
# # sarasas = [1,2,3,4,5]
# # for elementas in sarasas:
# #     print("elementas: ", elementas)
#
# # for i in range(2, 8):
# #     print(i)
#
# # for i in range(5, 0, -1):
# #     print(i)
#
# # skaiciai = [24, 11, 72, 34, 7, 84]
# #
# # didziausias_skaicius = skaiciai[0]
# #
# # for skaicius in skaiciai:
# #     if skaicius > didziausias_skaicius:
# #         didziausias_skaicius = skaicius
# # print("didziauias skaicius yra:", didziausias_skaicius)
#
#
# # skaicius = input("Koks tavo vardas: ")
# # print(skaicius)
#
# # skaicius = float(input("parasyk skaiciu:"))
# # print(skaicius)
#
#
# # skaicius = int(input("iveskit skaiciu:"))
# # suma = 0
# # for i in range(1, skaicius + 1):
# #     suma += i
# # print("skaiciu suma nuo 1 iki" , skaicius, "yra", suma)
#
# # 1. is saraso isfiltruot lyginius sk
#
# # sarasas = [2,5,11,25,9]
# # lyginiai_sk = []
# ## for skaicius in sarasas:
# #     if skaicius %2 == 0:
# #         lyginiai_sk.append(skaicius)
# # print("lyginiai_sk ", lyginiai_sk)
#
# # 2. atspausdinti piramide su zvaigzdutem
#
# # eiluciu_sk = int(input("iveskit sveika sk"))
# # for eilute in range(1, eiluciu_sk + 1):
# #     tarpas = eiluciu_sk - eilute
# #     zvaigzde = 2 * eilute - 1
# #     print(" " * tarpas + "*" * zvaigzde)
#
# # 3. rasti pirminius sk is intervalo (10,50) pirminiai sk
# # pradzia = 10
# # pabaiga = 50
# # # print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra:")
# # for skaicius in range(pradzia, pabaiga + 1):
# #     if skaicius > 1:
# #         for daliklis in range(2, skaicius):
# #             if (skaicius % daliklis) == 0:
# #                 break
# #         else:
# #             print(skaicius)
#
# # 4. Patikrinti zodius is saraso ir isvardinti tuos zodzius kurie prasideda A
# # zodiai_is_A = ["Saule", "Menulis", "Autobusas", "Kempine", "Apelsinas"]
# # Raide = "A"
# # for zodis in zodiai_is_A:
# #     if zodis[0]. upper() == Raide.upper():
# #         print(zodis)
#
# # 5. Sudaryt ir isvest daugybos lentele
# # print("daugybos_lentele nuo 1 iki 10")
# # for i in range(1,11):
# #     for j in range(1,11):
# #         rezultatas = i*j
# #         print(f"{i} x {j} = {rezultatas}")
# #     print()
#
# # 6. Patikrinti ar ivestas vartotojo skaicius yra teig ar neigiam arba nulis
# # skaicius = int(input("iveskite skaiciu_> "))
# # if skaicius > 0:
# #     print("ivestas skaicius teigiamas" )
# # elif skaicius < 0:
# #     print("ivestas skaicius neigiamas" )
# # else:
# #     print("ivestas skaicius = nulis")
#
# # 7. Isvesti fizz skaicius, kurie dalijasi is 3, buzz skaiciamd kurie dalinasi is 5, fizzbuzz, kurie dalijasi is 3 ir is 5
# # internavas nuo 1 iki 100
# for skaicius in range(1, 101):
#     if skaicius % 3 ==0 and skaicius % 5 ==0:
#         print("fizzbuzz")
#     elif skaicius % 3 ==0:
#         print("fizz")
#     elif skaicius % 5 ==0:
#         print("buzz")
#     else:print(skaicius)
#
#
# # 8. sukurti skaiciu spejimo zaidima, o vartotojas turi atspeti
# # pasleptas_skaicius = random.randint(1, 10)
# # bandymai = 0
# # max_bandymai = 10
# # while bandymai < max_bandymai:
# #     spejimas = int(input("Atspekite paslepta skaiciu nuo 1 iki 100: "))
# #     bandymai += 1
# #     if spejimas == pasleptas_skaicius:
# #         print(f"Sveikiname. Atspejote per {bandymai}bandymus")
# #         break
# #     elif spejimas < pasleptas_skaicius:
# #         print("bandykite didesni skaiciu")
# #     else:
# #         print("bandykite mazesni skaiciu")
# # if bandymai >= max_bandymai:
# #     print(f"jus pasiekete max bandymu skaiciu. paslesptas kaicius buvo {pasleptas_skaicius}")
#
# # sukurti zodynas, reia isvesti zodzius kurie ilgesni nei 6 simboliai
# # Zodziai = ["saule", "menulis", "dangus", "Vilnius", "Jurga","Gyvenimas", "kur"]
# # zodynas = {}
# # for zodis in Zodziai:
# #     zodynas[zodis] = len(zodis)
# # for zodis, ilgis in zodynas.items():
# #     if ilgis > 6:
# #         print(f"{zodis}: {ilgis} raides")
# #
# # 1. Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus;
# # Tekstas = Eglutė skarota eglutė žalia Meškutė gauruota ją lanko šile Jos liauną kamieną kalena geniai
# # zodynas = {}
# # zodziai = Tekstas.split()
# # for zodis in zodziai:
# #     zodynas[zodis] = zodynas.get(zodis, 0) + 1
# # for zodis, pasikartojimai in zodynas.items():
# #     if pasikartojimai >=3:
# #         print(f"pasikartojantis_zodis yra: {zodis}, pasikartojo {pasikartojimai} kartu")
#
#
# # 2 .Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą;
# # zodiai = ["Saule", "Autobusas", "Kempine", "Menulis", "Autobusas", "Autobusas", "Apelsinas"]
#
# # 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;
# # studentas = {
# #     "Jonas": 9
# #     "ona": 5
# #     "Petras": 10
# #     "Maryte": 8
# # }
#
# # 4. Sukurti žodyną su knygų informacija ir surikiuoti knygas pagal metus ir pavadinimus.
#
#
# # print("pradzia!")
# # vaisiai = ["obuolys", "slyva", "ananasas"]
# # for vaisius in vaisiai:
# #     print(vaisius)
# #     if vaisius == "slyva":
# #         break
# #     print("pabaiga!")
#
# # # print("pradzia!")
# # vaisiai = ["obuolys", "kriause", "slyva"]
# # for vaisius in vaisiai:
# #     print(vaisius)
# # #     if vaisius == "kriause":
# #         break
# # #     print("pabaiga!")
#
# # print("+------+------+")
# # print("|Vardas|Amzius|")
# # print("+Jonas +  34  +")
# # print("+------+------+")
#
# # x = 13
# # print(x + 1)
# # print(x)
# # x = 5 + 2
# # print(x)
# # first = 2
# # second = 3
# # third = first * second
# # second = third - first
# # print(second)
#
#
# # 1.Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą, kur n yra vartotojo įvestas skaičius.
# # Panaudokite "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte, ar įvestas skaičius yra sveikasis;
#
# # n = int(input("iveskit skaiciu:"))
# # if n <= 0:
# #     print("ivestas sk turi buti sveikasis")
# # else:
# #     suma = 0
# #     for skaicius in range(1, n + 1):
# #         suma += skaicius
# #     print(f"suma nuo 1 iki {n} yra {suma}")
##
# # 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10). Programa turi grąžinti mokinio vertinimą (
# #     pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai"). Naudokite "if" sąlygos sakinį;
#
# pazymys = int(input("Iveskite pazymi nuo 1 iki 10: "))
# ivertinimas = 'Puikiai'
# ivertinimas_1 = 'Gerai'
# ivertinimas_2 = 'Vidutiniskai'
# ivertinimas_3 = 'Silpnai'
# ivertinimas_4 = 'Neuztektinai'
# if pazymys <= 3:
#     print(f'Jusu rezultatas {ivertinimas_4}')
# elif pazymys <=5:
#     print(f'Jusu rezultatas {ivertinimas_3}')
# elif pazymys <=7:
#     print(f'Jusu rezultatas {ivertinimas_2}')
# elif pazymys <=9:
#     print(f'Jusu rezultatas {ivertinimas_1}')
# elif pazymys ==10:
#     print(f'Jusu rezultatas {ivertinimas}')
# elif pazymys >10:print(f' Pazymys negali buti didenis nei 10')
#
# ARBA galima taip MODESTO varianta
# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."
# print(f"Mokinio vertinimas: {vertinimas}")

# # 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti, ar įvesti metai yra keliamieji
# # (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą;
# #
# Metai = int(input("iveskite metus"))
# if Metai % 4 == 0:
#     print("Kelemieji metai")
# else:
#     print("Nekeliami metai")

# # 4. Turite žodyną, kuriame yra vardai ir amžius. Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras,
# # kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;
#
# Studentai = {
#     "Petras": 32,
#     "Antanas": 15,
#     "Jurgis": 18
#     }
# Atrinkti_studentai = {}
# for Vardas, Amzius in Studentai.items():
#     if Amzius >= 18:
#         Atrinkti_studentai[Vardas] = Amzius
# print(Atrinkti_studentai)

# # 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas. Sukurkite sąrašą, kuriame prekės yra žodynai,
# # kuriuose yra prekės pavadinimas ir kaina. Taip pat paskaičiuokite bendrą visų prekių kainą;
# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")

# # 6. Turite sąrašą žmonių vardų. Sukurkite programą, kuri leidžia vartotojui įvesti vardą ir patikrina, ar jis yra sąraše.
# # Jei vardas yra sąraše, programa turi išvesti pranešimą "Vardas yra sąraše," kitu atveju - "Vardo nėra sąraše."


# vardas = input("Irasykite varda")
# Sarasas = ["Ona", "Jonas", "Petras", "Maryte"]
# Vardas_is_saraso = Sarasas
# for vardas in Sarasas:
#     if vardas == Vardas_is_saraso:
#         print("vardas yra sarase")

# 09-06 NAMU daibai
#                    ****PADARYTAS****
# 1. Sukurkite sąrašą temperatūros su temperatūromis. Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta"
# (jei temperatūra virš 20) arba "šalta" (jei temperatūra 20 ar mažiau) temperatura

# temperaturos = [25,20,5,30,-5]
# silta = []
# salta = []
# for temp in temperaturos:
#     if temp >=20:
#         silta.append(temp)
# print('silta:', silta)
# #    else:
# salta.append(temp)
# print('salta:', salta)

#               *****PADARYTAS****
# 2. Turite žodyną su studentų vardais ir jų pažymiais. Parašykite "for" ciklą,
# kuris išveda kiekvieno studento vardą ir jo pažymį.
#
# Studentai = {
#     'Jurgis': (5,6,7),
#     'Antanas': (5,7,2),
#     'Aloyzas': (10,10,9),
#     'Martynas': (2,2,2)
# }
# print(Studentai)

# ***************PADARYTAS*******
## 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius.
# Naudojant "while" ciklą, pridėkite kiekvieną įvestą skaičių prie sąrašo.
# Ciklą nutraukite, kai vartotojas įveda 0.

# ivesti_sk = []
# while True:
#
#     skaicius = int(input('Prasome ivesti skaiciu:'))
#     if skaicius == 0:
#         break
#
#         ivesti_sk.append(skaicius)
#         print('ivesti_skaicius:')
#         for skaicius in ivesti_sk:
#
#             print(ivesti_sk)

# ***************PADARYTAS*******
# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos.
# Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne.
# Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".

# drinkas = input('irasykite gerimo pavadinima:')
# gerimai ={
#     'kava': 1,
#     'fanta': 1,
#     'vynas': 10,
#     'pienas': 2,
#     'sultys': 3,
#     'alus': 2
# }
# # if drinkas in gerimai:
#     kaina = gerimai[drinkas]
#     print(kaina)
# # else:
#     print('tokio gerimo neturime')


#                  ***PADARYTA***
# 5. Patikrinkite, ar skaičiai sąraše yra lyginiai arba nelyginiai.
# Sukurkite du tuščius sąrašus: vienas lyginiams ir kitą nelyginiams skaičiams,
# išrūšiuokite lyginius ir nelyginius skaičius iš skaičiai sąrašo.
#
# skaiciai = [2, 5, 11, 14, 20, 35]
# lyginiai = []
# nelyginiai = []
## for sk in skaiciai:
#     if sk % 2 == 0:
#         lyginiai.append(sk)
#     else:
#         nelyginiai.append(sk)
# print('lyginiai skaiciai:', lyginiai)
# print('nelyginiai skaiciai:', nelyginiai)



# 09-07
# POP

# vardai = ["Jonas", "Petras", "Marius", "Laura"]
# pirmas_vardas = vardai.pop(2)
# print(pirmas_vardas)

# Inser  (nurodome kur deti)
# vardai = ["Jonas", "Petras", "Marius", "Laura"]
# vardai.insert(1,"Giedrius")
# print(vardai)

# SORT
# vardai = ["Jonas", "Petras", "Marius", "Laura"]
# vardai.sort(reverse=True)
# print(vardai)

# Remove
# vardai = ["Jonas", "Petras", "Marius", "Laura"]
# vardai.remove("Laura")
# print(vardai)

# Su tokiais skliaustais () sarase reiksmiu pakeist negalima

#
# vaisiai = ['obuolys', 'kriause', 'bananas', 'braske']

# # vaisiai2 = {
# # "obuolus, "
# # ""kriause", "
# # ""bananas", "
# # ""braske"
# # }
#
# vaisiai3 = vaisiai2[0]
#            print (vaisiai3)

# Sunumeruoja
# for indeksas, vaisius in enumerate(vaisiai, start=1):
#     print(f'{indeksas}. {vaisius}')


# with open("failo_pav.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# with open("failo_pav.txt", "r", encoding="utf-8") as file:
#     for eilute in file:
#         print(eilute.strip())

# vaisiai = []

# with open('vaisiai.txt', 'r', encoding='utf-8') as file:
#     file:write('obuolys, \nkriause, \nbananas, \nbraske')
#     vaisiai = file.readlines()
#     print(vaisiai)

# 09-08 - FUNKCIJOS
# 1.
# def pasisveikinimas(vardas):
#     sveikinimas = f"sveiki, {vardas}"
#     return sveikinimas
#
# vardas = input("iveskite varda")
# sveikinimas = pasisveikinimas(vardas)
# print(sveikinimas)

# 2.
# def ar_lyginis(skaicius):
#     if skaicius %2 == 0:
#         return True
#     else:
#         return False
## skaicius = 8
# if ar_lyginis(skaicius):
#     print(f'{skaicius} yra lyginis')
# else:
#     print(f'{skaicius} yra nelyginis')

# 3.
# def suma(a, b):
#     rezultatas = a +b
#     return rezultatas
# x = 5
# y = 3
# sumos_rezultatas = suma(x, y)
# print(f'{x} + {y} = {sumos_rezultatas}')

# 4.
# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# sarasas = [10, 15, 20, 25, 30]
# rezultatas = vidurkis(sarasas)
# print(f'saraso vidurkis: {rezultatas}')

#
# 5.ar_teigiamas(skaicius)
# def ar_teigiamas(skaicius):
#         if skaicius > 0:
#                 return True
#         else:
#                 return False
#
# skaicius = -1
# if ar_teigiamas(skaicius):
#         print(f"{skaicius} yra teikiagas")
# else:
#         print(f"{skaicius} yra neigiamas")

# 6.did skaicius sarase

# def didziausias_sk(skaicius):
#     didziausias = skaicius[0]
#     for sk in skaicius:
#         if sk > didziausias:
#             didziausias = sk
#     return didziausias
#
# sarasas = [10, 658, 12, -2]
# didziausias = didziausias_sk(sarasas)
# print(f'didziausias yra {didziausias}')

# 7. f-ja sujungia du sarasus
# def sujungti_sarasai (sarasas_1, sarasas_2):
#     sujungtas_sarasas = sarasas_1 + sarasas_2
#     return sujungtas_sarasas
# s_1 = [1, 2, 3]
# s_2 = [4, 5, 6]
# rezultatas = sujungti_sarasai(s_1, s_2)
# print(rezultatas)

# 8. rasti didesni sk nei yra sarase
# def didesnis (listas, skaicius):
#     did = [sk_1 for sk_1 in listas if sk_1 > skaicius]
#     return did
#
# listas = [1, 2, 15, 10, 1005]
# n = 8
# didesni_sk = didesnis(listas, n)
# print(f'sarase skaiciai didesni uz {n} yra {didesni_sk}')

# 09-08 Namų darbai:
#---------------PADARYTAS______________
# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;

# def vidurkis(pazymiai):
#     suma = sum(pazymiai)
#     avg = suma/len(pazymiai)
#     return avg
# st_pazymiai = [2,10,5,6,8,4,9]
# rezultatas = vidurkis(st_pazymiai)
# print(f'pazymiu_vidurkis: {rezultatas}')

#---------------PADARYTAS______________
# 2. Sukurkite funkciją pirminiai_skaiciai(n), kuri priima sveikąjį skaičių n ir grąžina visus pirminius skaičius nuo 2 iki n;

# def pirminiai_sk(n):
#      if n == 1:
#          return False
##      elif n > 1:
#         for sk in range(2, n):
#             if (n%sk) == 0:
#                 return False
##         else:
#             return True
# n = 12
# if pirminiai_sk(n):
#     print(f'{n} yra pirminis')
# else:
#     print(f'{n} yra nepirminis')
#
#---------------PADARYTAS______________
# 3. Sukurkite funkciją zodziu_kiekis(tekstas), kuri priima tekstą ir grąžina žodžių skaičių tekste. Žodžius galite laikyti atskirtais tarpais;
#
# Tekstas = 'Siandien yra sekmadienis ir as turiu daryti namu darbus'
# # def zodziu_kiekis(sakinys):
# #     kiekis = len(sakinys.split())
# #     return kiekis
# # print('Zodziu sakinyje yra:', zodziu_kiekis(Tekstas))
#
# #---------------PADARYTAS______________
# # 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;
#
# def didz_elementas(sarasas):
#     max = sarasas[0]
#     for skaicius in sarasas:
#         if skaicius > max:
#             max = skaicius
#     print('Didziausias rastas skaicius sarase yra:', max)
# sk_sarasas = [9, 7, 4, 2, 3, 6, 8, 10, 21, 5]
# print(sk_sarasas)
# didz_elementas(sk_sarasas)
#
# #---------------PADARYTAS______________
# # 5. Sukurkite funkciją kvadrato_plotas(ilgis), kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.
# # 1 VARIANTAS
# # kvadrato_krastine = 10
# # kvadrato_plotas = kvadrato_krastine*kvadrato_krastine
# # print('kvadrato plotas yra:', kvadrato_plotas)
#
# # 2 VARIANTAS
# # def kvadrato_plotas(S):
# #     return S * S
# # S = 10
# # plotas = kvadrato_plotas(S)
# # print('Kvadrato plotas yra:', (plotas))
#
# #---------------PADARYTAS______________
# # 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą.
# # Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;
#
# # def suma_saraso(x):
# #     viso = 0
# #     for sarasas in x:
# #         viso = viso + sarasas
# #     return viso
# # sarasas_sk = [1,2,3,4,5,1,4,5]
# # print('Skaiciu saraso suma yra:', suma_saraso(sarasas_sk))
#
# #---------------PADARYTAS______________
# # 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.
# #
# # def mano_sarasas(sarasas):
# #    sandauga = 1
# #    for skaicius in sarasas:
# #         sandauga *= skaicius
# #    return sandauga
# # sk_sarasas = [2, 4, 6, 8, 10]
# # print('Saraso skaiciu sandauga lygi:',mano_sarasas (sk_sarasas))

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
class Treneris:
    def __init__(self):
        self.strategija = "ataka"
    def keisti_strategija(self,nauja_strategija):
        self.strategija = nauja_strategija

    def strategijos_info(self):
        return f'naudojama strategija {self.strategija}'
class Zaidejas:
    def __init__(self, pavarde, pozicija):
        self.pavarde = pavarde
        self.taiklumas = 30
        self.pozicija = pozicija

    def upgrade(self):
        self.taiklumas += 5
        if self.taiklumas > 100:
            self.taiklumas = 100

    def zaidejo_info(self):
        return f'{self.pavarde}, zaidejo pozicija {self.pozicija}, ir jo taiklumas {self.taiklumas}%'
class Komanda:
    def __init__(self, pavadinimas):
        self.komanda =[]
        self.pavadinimas = pavadinimas
        self.treneris = Treneris()
    def prideti_zaideja(self,zaidejas):
        self.komanda.append(zaidejas)

    def isimti_zaideja(self, zaidejas):
        if zaidejas in self.komanda:
            self.komanda.remove(zaidejas)
    def komandos_informacija(self):
        print(f'{self.pavadinimas}, komandos zaidejai: ')
        for zaidejas in self.komanda:
            print(zaidejas.zaidejo_info())
    def strategijos_info(self):
        print (self.treneris.strategijos_info())

    def pasirinkti_treneri(self, treneris):
        self.komanda.append(treneris)

    def pakeisti_treneri(self, treneris):
        if treneris in self.komanda:
            self.komanda.remove(treneris)

komanda=Komanda("Puseles")
zaidejas1=Zaidejas("Greitas", "puolejas")
zaidejas2=Zaidejas("didelis", "saugas")
zaidejas3=Zaidejas("vidutinis", "atsarginis")

komanda.prideti_zaideja(zaidejas1)
komanda.prideti_zaideja(zaidejas2)
komanda.prideti_zaideja(zaidejas3)

zaidejas1.upgrade()
zaidejas1.upgrade()
zaidejas3.upgrade()

komanda.komandos_informacija()
komanda.strategijos_info()