#
#
# import  random
#
#
#
#
# # mano komentaras
# # """
# # multi_line
# # """
# # vardas = "Jurgita"
# # print(vardas)
# # skaicius = 25
# # print(skaicius)
# # print("manos sugalvotas skaicius" + str(skaicius))
#
# # true_or_false = false
# # print(type(true_or_false))
# # fruits = ['apple', 'orange', 'kivi', 'watermelon']
# # lietuvos_pilieis = {
# # 'id': 1,
# # 'vardas': 'Antanas',
# # 'Amzius': 34,
# # 'Miestas': 'Klaipeda'
# # }
# # print(lietuvos_pilieis)
#
#
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

***************PADARYTAS*******
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

# Namų darbai:
#
# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;

# 2. Sukurkite funkciją pirminiai_skaiciai(n), kuri priima sveikąjį skaičių n ir grąžina visus pirminius skaičius nuo 2 iki n;

# 3. Sukurkite funkciją zodziu_kiekis(tekstas), kuri priima tekstą ir grąžina žodžių skaičių tekste. Žodžius galite laikyti atskirtais tarpais;

# 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;

# 5. Sukurkite funkciją kvadrato_plotas(ilgis), kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.

# 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą.
# Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;

# 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.