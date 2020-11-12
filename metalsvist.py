#import requests
#from bs4 import BeautifulSoup
    # =============================================================
     # МОДУЛЬ 1: Гост2Дин
     # TODO: Добавить проверку на корректность ввода гостов.
          # TODO: обрезать буквы и "-год"

     # Модуль 2:
     # TODO: прикрутить название для динов

     # МОДУЛЬ 3:
     # TODO: сделать поиск по HV

     # МОДУЛЬ 4:
     # TODO: сделать поиск по дину по сайту

     # МОДУЛЬ 5:
     # TODO: сделать расчет химанкера

    # =============================================================

# МОДУЛЬ 1: преобразование госта в дин
def gost2din():
    gost = input("Введите только номер ГОСТа: ")
    
    #проверка на валидность ввода
    gost = (gost.replace(" ", ""))
    gost = (gost.strip())
    gost = (gost.lower())
    gost = (gost.replace("гост", ""))

    


    intut_gost = gost

    # Словарь соотношений ГОСТа в DIN + ISO
    dic_for_standarts = {
         "397" : "DIN 94, ISO 1234",
         "1144" : "DIN 96, DIN 7981, ISO 7049",
         "1145" : "DIN 7982, DIN 97, ISO 7050",
         "1146" : "DIN 95, DIN 7983, ISO 7051",
         "1476" : "DIN 553, ISO 7434",
         "1477" : "DIN 438, DIN 551, ISO 7436, ISO 4766",
         "1478" : "DIN 417, ISO 7435",
         "1481" : "DIN 561",
         "1482" : "DIN 479",
         "1485" : "DIN 479",
         "1486" : "DIN 480",
         "1488" : "DIN 478",
         "1491" : "DIN 84, ISO 1207",
         "3032" : "DIN 315",
         "3033" : "DIN 444",
         "3057" : "DIN 2093",
         "3070" : "DIN 3060",
         "3128" : "DIN 7, DIN 6325, ISO 2338",
         "3129" : "DIN 1, ISO 2339",
         "4751" : "DIN 580, ISO 3266",
         "5915" : "DIN 555, DIN 934, ISO 4034, ISO 4032, ISO 8673",
         "5916" : "DIN 439, DIN 936, ISO 4035, ISO 4036, ISO 8675",
         "5918" : "DIN 935, ISO 7035, ISO 7036, ISO 7037",
         "5919" : "DIN 937, ISO 7038",
         "5927" : "DIN 555, DIN 934, ISO 4032, ISO 4034, ISO 8673",
         "5932" : "DIN 935, DIN 937, ISO 7035, ISO 7036, ISO 7037, ISO 7038",
         "6393" : "DIN 1816",
         "6402" : "DIN 127",
         "6958" : "DIN 440, DIN 9021, ISO 7094, ISO 7093-1, ISO 7093-2",
         "7798" : "DIN 931, DIN 933, ISO 4014",
         "7801" : "DIN 607",
         "7802" : "DIN 603, ISO 8677",
         '7805' : "DIN 931, DIN 933, ISO 4014",
         "8878" : "DIN 914, ISO 4027",
         "9464" : "DIN 7978, ISO 8736",
         "9649" : "DIN 125, ISO 7089, ISO 7090",
         "10299" : "DIN 660, ISO 1051",
         "10300" : "DIN 661, ISO 1051",
         "10301" : "DIN 662, ISO 1051",
         "10302" : "DIN 674, ISO 1051",
         "10337" : "DIN 7964",
         "10338" : "DIN 7964",
         "10450" : "DIN 433, ISO 7092",
         "10462" : "DIN 6797, DIN 6798",
         "10463" : "DIN 6798",
         "10464" : "DIN 6797, DIN 6798",
         "10619" : "DIN 7982, ISO 7050",
         "10620" : "DIN 7983, ISO 7051",
         "10621" : "DIN 7516 A, DIN 7981, ISO 7049",
         "10657" : "DIN 546",
         "10906" : "DIN 434, DIN 435",
         "11074" : "DIN 913, ISO 4026",
         "11075" : "DIN 915, ISO 4028",
         "11371" : "DIN 125, ISO 7089, ISO 7090",
         "11473" : "DIN 571",
         "11644" : "DIN 967",
         "11648" : "DIN 6799",
         "11738" : "DIN 912, DIN 7984, ISO 4762, ISO 21269",
         "11860" : "DIN 1587",
         "11871" : "DIN 546, DIN 1804",
         "11872" : "DIN 5406",
         "13152" : "DIN 186",
         "13438" : "DIN 6319",
         "13439" : "DIN 6796",
         "13463" : "DIN 93, DIN 463",
         "13464" : "DIN 93, DIN 463",
         "13942" : "DIN 471",
         "13943" : "DIN 472",
         "14229" : "DIN 1481, ISO 8752",
         "14724" : "DIN 444",
         "14725" : "DIN 444",
         "15522" : "DIN 431",
         "15523" : "DIN 6330",
         "17473" : "DIN 85, DIN 7985, ISO 1580, ISO 7045",
         "17474" : "DIN 964, DIN 966, ISO 2010, ISO 7047",
         "17475" : "DIN 963, DIN 965, ISO 2009, ISO 7046-1, ISO 7046-2",
         "17673" : "DIN 605",
         "18746" : "DIN 427, ISO 2342",
         "22033" : "DIN 938",
         "22034" : "DIN 939",
         "22035" : "DIN 939",
         "22038" : "DIN 835",
         "22353" : "DIN 6914, ISO 7412",
         "22354" : "DIN 6915, ISO 7414",
         "22355" : "DIN 6916, ISO 7416",
         "23360" : "DIN 6885",
         "24071" : "DIN 6888, ISO 3912",
         "28964" : "DIN 916, ISO 4029",
    }

    # проверка гостов в динах
    output_from_dic = (dic_for_standarts.get(intut_gost))

    # Если проверка вывела None - выводит ошибку, иначе - значение словаря, т.к. есть аналог в дине
    if output_from_dic == None:
         print("Не корректно введенный номер ГОСТа или нет аналогов в современных стандартах")
    else:
        # проверка на соотношение гост == дин
        output_from_dic = (dic_for_standarts.get(intut_gost).replace(", ", ","))

        # преобразование строки в список
        total_list_of_standarts = list(output_from_dic.split(","))
        
        # проверка к-во динов и печать каждого отдельного дина с новой строки
        zero_count_standarts = 0
        count_of_list_of_standart = (len(total_list_of_standarts) - 1)
        
        print("= Аналог(и) в современном стандарте: ")
     
        # выполняется перебор найденных стандартов при сравнении гостов и динов и выводится в виде столбика найденные дины
        while count_of_list_of_standart >= zero_count_standarts:
             print("== " + str(total_list_of_standarts[zero_count_standarts]))
             zero_count_standarts += 1

# МОДУЛЬ 2: отображдение имени через парсинг с сайта
def name_from_site():
    print("\n" + "\t" + "названии товара".upper())
    #   парсинг информации из сайта по поиску
    search_id = "din912"
    url = 'http://metalvis.ua/search/?q=' + search_id + '&prf' # url страницы
    r = requests.get(url)

    # Запись полученного парсинга
    with open('search.html', 'w') as output_file:
        output_file.write(r.text)

    # Создание супа для фильтрации по названии товара и его маркировка
    with open("search.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

    # фильт и запись полученного фильтра
    with open ('parser.xml', 'w') as output_file:
        soup_find = str(soup.find_all(attrs={"class" : "h catalogue_descr"}))
        soup_from_perser = BeautifulSoup(soup_find, 'lxml')
        output_file.write(soup_find)

    # второй, боллее приближенный фильтр
    with open ('parser.xml', 'r') as output_filter_file:
        soup_final_find = str(soup_from_perser.find(attrs={"class" : "h2"}))

        # создание фальла полученного после последнего фильтра
        with open ('final_filter.xml', 'w') as final_filter:
            final_filter.write(soup_final_find)
            print("write final_filter is ok")
        print(soup_final_find)
        



# запуск скрипта
def start():

     print("\n" + "\t" + "Преобразование гостов в din".upper())
     
     # МОДУЛЬ 1: гост2дин
     gost2din()
     
     # МОДУЛЬ 2: поиска названия товара через металвис
     #name_from_site()

     # включить для циклического выполнения
     #start()


start()
