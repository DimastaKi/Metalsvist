import os
import sys
import requests
from bs4 import BeautifulSoup


    # =============================================================
     # МОДУЛЬ 1: Гост2Дин

     # Модуль 2:
     # TODO: прикрутить название для динов
     # TODO: оптимизация: сзделать файл, в который будет записывать значение название дина, который
     # парсится с сайта. При поиске, ищится вначале в файле, если нет - идет на сайт и парсит от туда.

     # МОДУЛЬ 3:
     # TODO: сделать поиск по HV

     # МОДУЛЬ 4:
     # TODO: сделать поиск по дину по сайту

     # МОДУЛЬ 5:
     # TODO: сделать расчет химанкера

# рисует линию
def line():
    print ("{0:=^60}".format(" METALSVIST "))

list_of_din = ""

# МОДУЛЬ 1: преобразование госта в дин
def gost2din():

    print("\n" + "{0:>^16} Преобразование гостов в din {0:<^16}".format("").upper())
    gost = input("Введите номер ГОСТа >> ")

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

    # получение ключа-госта из введенного пользователем
    temp_keys = ""
    get_keys = ""

    for keys in dic_for_standarts:
        temp_keys = keys
        search_gost = gost.find(temp_keys)
        if search_gost >= 0:
            get_keys = temp_keys

    # поиск ключа в словаре гостов
    output_from_dic = (dic_for_standarts.get(get_keys))

    # Если ключа нет - выводит None, иначе - значение словаря
    if output_from_dic == None:
         print("Нет аналогов")
    else:
        print("= Аналог(и) " + str(get_keys) + ": ")

        # получение ключа из словаря и удаление пробела
        output_from_dic = (dic_for_standarts.get(get_keys).replace(", ", ","))

        # преобразование строки в список
        total_list_of_standarts = list(output_from_dic.split(","))

        # получение к-во стандартов по ключу
        zero_count_standarts = 0
        count_of_list_of_standart = (len(total_list_of_standarts) - 1)
       
        # МОДУЛЬ 2: отображдение имени через парсинг с сайта


        def name_from_metalvis():
            count = 0
            output = 1

            #   парсинг информации из сайта по поиску
            search_id = total_list_of_standarts[count]
            
            url = 'http://metalvis.ua/search/?q=' + search_id + '&prf' # url страницы
            r = requests.get(url)

            with open('parser.xml', 'w') as output_file:
                output_file.write(r.text)
            with open("parser.xml", "r") as f:
                contents = f.read()
                soup = BeautifulSoup(contents, 'lxml')
                soup_find = str(soup.find_all(attrs={"class" : "h catalogue_descr"}))
                soup_from_perser = BeautifulSoup(contents, 'lxml')
                soup_final_search_name = str(soup_from_perser.find("a" , {"class": "propTitle"}))

                while output == 1:

                    
                    start_search_name = int(soup_final_search_name.find('style="height:auto">') + 20)
                    finist_search_name = int(soup_final_search_name.find('</a>'))
                    name_from_site = soup_final_search_name[start_search_name:finist_search_name:]
                    
                    # print()
                    start_search_din = int(soup_find.find("<b>")+44)
                    din_from_site = str(soup_find[start_search_din:400].strip())
                    print(din_from_site)

                    print()

                    if din_from_site in total_list_of_standarts:
                        print("Названии изделия: ".upper() + str(name_from_site) + "\n")
                    else:
                        din_from_site = None
                        if count_of_list_of_standart >= count:
                            count += 1
                            print("выхлоп с ноне")
                        else:
                            output == 0

                    print("выхлоп с вил")
                    output += 1
                else:
                    print("hz nnone")


        # и выводится в виде столбика найденные дины
        while count_of_list_of_standart >= zero_count_standarts:
             print("== " + str(total_list_of_standarts[zero_count_standarts]))
             zero_count_standarts += 1


        print("")
        name_from_metalvis()
        test_poligone()
        start()




def test_poligone():
    pass


# МОДУЛЬ 3: расчитывает HV крепеж по заданной толщине пакета
def hv():

    diameter = "12"
    hv_long = 0
    client_long = 15

    dic_hv_diameter_M12 = {
    "30" : "6,10",
    "35" : "11,15",
    "40" : "16,20",


    }

    #создание листа из словаря
    diametr_to_list = list(dic_hv_diameter_M12.get(diameter).split(","))


    # создание размеров: начальный, конечный, рекомендуемая длинна болта
    start_l = (diametr_to_list[0])
    start_l = int(start_l) - 1
    finish_l = (diametr_to_list[1])
    finish_l = int(finish_l)


    total_long = 0

    while start_l < finish_l:

        start_l += 1
        total_long = start_l
        print (total_long)

# МЕНЮ запуска скриптов + главное меню
def start():
    line()
    print ("Выбери раздел:  | Gost2DIN: 1  | HV: 2   |\n\
 \t\t| Home: 0      | Exit: e |")
    module_start = input("Выберите значение: ")


    if module_start == "1":
        line()
        gost2din()

    elif module_start == "2":
        line()
        hv()

    elif module_start == "e":
        os.system('clear')
        sys.exit()

    elif module_start == "0":
        line()
        start()

    else:
        print("Мимо... попробуй снова...")
        start()

    start()


start()
