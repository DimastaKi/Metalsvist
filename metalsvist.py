#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import shutil

    # =============================================================
     # МОДУЛЬ 1: Гост2Дин

     # Модуль 2:
     # V TODO: прикрутить название для динов
     # X TODO: оптимизация: сзделать файл, в который будет записывать значение название дина, который
     # X парсится с сайта. При поиске, ищится вначале в файле, если нет - идет на сайт и парсит от туда.
     # V вынести словарь dic_din_in_metalvis  в отдельный модуль и подключить его

     # МОДУЛЬ 3:
     # TODO: сделать поиск по HV

     # МОДУЛЬ 4:
     # TODO: сделать расчет химанкера

     # МОДУЛЬ 5:
     # V сделать список с мш

     # МОДУЛЬ ADMIN:
     # через перезапись сделать возможность добавление пар в словарь dic_din_in_metalvis
     # сделать бэкап перед добавлением нового значение в словарь

     #
     # сделать табличную выдачу результатов.
     # ------------------------------------------
     # | DIN471 | 95PK1 | Стоп.кольцо внешн.471 |

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
     "6958" : "DIN 440, DIN 9021, ISO 7094, ISO 7093",
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
     "17475" : "DIN 963, DIN 965, ISO 2009, ISO 7046",
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

# рисует линию
def line():
    print ("{0:=^60}".format("> METALL-SVIST <"))

# принимает значение пути в ОС, где находится скрипт
parent = Path(__file__).resolve().parent

#BACKUP словарь соотношения DIN в артикула Солди
# dic_din_in_metalvis_id = {
#      "DIN440" : "7D200 Шайба д/дерева DIN 440",
#      "DIN471" : "95PK1 Стоп.кольцо внешн.471",
#      "DIN472" : "95PK2 Стоп.кольцо внутр.472",
#      "DIN439" : "6Z200 Гайка низкая DIN 439B",
#      "EN14399/6" : "7HV00 Шайба пов.твердости",
#      "DIN6916" : "7HV00 Шайба пов.твердости",
#      "DIN608" : "5V608 Болт потай.квадр.підг",
#      "DIN6798A" : "7V200 Шайба стопорная",
#      "DIN84" : "5M521 Гвинт циліндр.",
#      "DIN85" : "5M521 Гвинт циліндр.",
#      "DIN25201" : "7XNL0 Шайба Nord-Lock",
#      "DIN935" : "6KR20 Гайка корончатая",
#      "DIN9021" : "7N200 Шайба увеличенная",
#      "ISO7380" : "5I220 Винт метр",
#      "DIN6928" : "80620 Саморез /металл 6гр/гл",
#      "DIN1587" : "6KL20 Гайка колпачковая",
#      "DIN7981" : "80520 Саморез /металл полукруг",
#      "DIN94" : "95Z00 Шплинт",
#      "DIN914" : "9800H Штифт с кон.кон",
#      "DIN1481" : "9500P Штифт пружинный",
#      "DIN7603A" : "7U000 Шайба медная",
#      "DIN912" : "5I5O0 Винт вн.6гр",
#      "DIN315" : "6K200 Гайка барашковая",
#      "DIN71412" : "5MM20 Масленка",
#      "DIN7980" : "7P200 Шайба пружинная квад.с.",
#      "DIN6923" : "6L200 Гайка зубчатая",
#      "DIN582" : "5M820 Рымгайка",
#      "DIN580" : "5M820 Рымболты",
#      "DIN741" : "3S200 Зажим для каната",
#      "DIN7985" : "5M520 Винт полукруг",
#      "ISO10642" : "5I120 Винт метр.пот.вн.6гр",
#      "DIN7991" : "5I120 Винт метр.пот.вн.6гр",
#      "DIN965" : "5M120 Винт потай",
#      "ISO7046" : "5M120 Винт потай",
#      "DIN963" : "5M120 Винт потай",
#      "DIN1480" : "3N200 Захват",
#      "DIN985" : "6P200 Контргайка",
#      "DIN6334" : "6D200 Гайка удлинитель",
#      "DIN125" : "7O200 Шайба плоская",
#      "ISO4032" : "60201 Гайка гарант.кл.8",
#      "ISO10642" : "5I100 Винт метр.пот.вн.6гр",
#      "DIN7504P" : "9T120 Винт с/св.(TEX)потай",
#      "DIN967" : "50202 Винт пкр.бурт.",
#      "DIN7504K" : "9T620 Винт с/св.(TEX)6гр.гл.",
#      "DIN571" : "20620 Винт для дерева",
#      "DIN6796" : "7W000 Шайба пруж. тарельчатая",
#      "DIN603" : "5V220 Болт с квадр.подголовком",
#      "DIN934" : "60200 Гайка",
#      "DIN975" : "5Z200 Резьб.стержень метрич.",
#      "DIN933" : "56600 Болт",
#      "DIN931" : "56600 Болт",

# }

# МОДУЛЬ 1: преобразование госта в дин
def module_gost2din():

    print("\n" + "{0:>^16} Преобразование гостов в din {0:<^16}".format("").upper())
    gost = input("Введите номер ГОСТа >> ")

    

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
         print("\n=> Нет аналогов или ошибка в написании\n".upper())
    else:
        print("\nАналог(и) ГОСТ " + str(get_keys) + ": \n")

        # получение ключа из словаря и удаление пробела
        output_from_dic = (dic_for_standarts.get(get_keys).replace(", ", ","))

        # преобразование строки в список
        total_list_of_standarts = list(output_from_dic.split(","))

        # получение к-во стандартов по ключу
        zero_count_standarts = 0
        count_of_list_of_standart = (len(total_list_of_standarts) - 1)
        # print ("count_of_list_of_standart" + str(count_of_list_of_standart))

        one_standart_in_list = total_list_of_standarts[zero_count_standarts]
        temp_one_standart_in_list = one_standart_in_list.replace(" ", "")

        # и выводится в виде столбика найденные дины
        while count_of_list_of_standart >= zero_count_standarts:

            one_standart_in_list = total_list_of_standarts[zero_count_standarts]
            one_standart_in_list = one_standart_in_list.replace(" ", "")

            # открывает словарь/лист для поиска значения
            open_dict = (open(str(parent) + "/dict_metalvis_id.py", "r"))
            b = open_dict.readline()
            a = eval(b)

            # проверяет есть ли ошибка в названии и выводит сообщение
            try:
                b = a[one_standart_in_list]
                print (str(one_standart_in_list) + " - " + str(b))
                open_dict.close()
            except KeyError:
                print (str(one_standart_in_list) + " - Нет в ассортименте Metalvis")
                open_dict.close()

            zero_count_standarts += 1
        print ("")


# МОДУЛЬ 3: расчитывает HV крепеж по заданной толщине пакета
def module_hv():

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

def module_test():
    pass

def module_din_in_metalvis_id():
    print("\n" + "{0:>^7} Поиск артикула в базе Metalvis согластно din {0:<^7}".format("").upper())
    input_standart = input("Напишите номер Вaшего DINa: ")
    find_din = ("DIN" + str(input_standart))
    find_iso = ("ISO" + str(input_standart))

    # открывает словарь/лист для поиска значения
    open_dict = (open(str(parent) + "/dict_metalvis_id.py", "r"))
    b = open_dict.readline()
    a = eval(b)

    # проверяет есть ли ошибка в названии и выводит сообщение
    try:
        b = a[find_din]
        print ("\n" + str(find_din) + " - Группа товара: " + str(b) + "\n")
        open_dict.close()
    except KeyError:
        try:
            b = a[find_iso]
            print ("\n" + str(find_iso) + " - Группа товара: " + str(b) + "\n")
            open_dict.close()
        except KeyError:
            print ("\nВведеный DIN/ISO: " + str(input_standart) + ".\nНет в базе Metalvis или ошибка написания\n")
            open_dict.close()

#Модуль администратора
def module_admin():
    print ("{0:=^60}".format("> ADMIN PANEL <"))
    print("\n\
    id: Добавление новых пар значений в словарь поиска артикулов Metalvis\n\n\
    1: Вывести список SKU\n\
    2: Вывести список пар ГОСТ:DIN(ISO)\n\
    e: Выйти в главное меню\n")

    module_start = input("Выберите раздел: ")
    
    #Запуск раздела вывода списка SKU из файла dict_metalvis_id
    if module_start == "1":

    # открывает словарь/лист для поиска значения
        open_dict = (open(str(parent) + "/dict_metalvis_id.py", "r"))
        read_dict_file = open_dict.readline()
        dict_info = str(eval(read_dict_file))
        dict_info = dict_info.replace("', ","\n")
        dict_info = dict_info.replace("'","")
        dict_info = dict_info.replace("{","")
        dict_info = dict_info.replace("}","")
        dict_info = dict_info.replace("DIN","DIN ")
        dict_info = dict_info.replace("ISO","ISO ")
        
        print ("\nВывод всего списка пар DIN\ISO:SKU\n" + dict_info + "\n")
     
    # Запуск раздела вывода пары ГОСТ:DIN(ISO)
    if module_start == "2":
        get_gost = str(dic_for_standarts.items())
        get_gost = get_gost.replace("),","\n")
        get_gost = get_gost.replace("(","ГОСТ ")
        get_gost = get_gost.replace("'","")
        get_gost = get_gost.replace(")])","")
        get_gost = get_gost.replace("dict_itemsГОСТ ["," ")
        os.system('clear')
        print ("\nСписок всех пар ГОСТ:DIN\ISO\n" + get_gost + "\n")
        
    
# Запуск раздела добавление нового SKU
    if module_start == "id":
        print("Пример записи:'DIN931':'56600 Болт'")
        selected_standard = input("Что вы хотите добавить:\n\
         i: ISO\n\
         d: DIN? \n\
         Выбрать значение: ")
        if selected_standard == "i":
            selected_standard = "ISO"
        elif selected_standard == "d":
            selected_standard = "DIN"
        else:
            print ("Не корректное значение, попробуйте снова")
            module_admin()
        input_new_din = input("Напишите ТОЛЬКО номер DIN\\ISO: ")


        new_din = (str(selected_standard) + str(input_new_din))
        new_metalvis_id = input("Напишите артикул(12345 Название группы: ")
        print("\nБудет записано: '" + str(new_din) + "'" + " : " + "'" + str(new_metalvis_id) + "'\n")

        print ("Все верно? \n\
            Y - записать\n\
            N - вернутся  в начало\n")
        new_id = input ("Выберите действие: ")

        if new_id == "n":
            module_admin()
        elif new_id == "Y":

            # проверка на бэкапость словаря, если нет бэкапа словаря - создает его
            check_backup = (os.path.exists(str(parent) + "/backup_dict_metalvis_id.py"))
            check_backup
            if check_backup == False:
                print(shutil.copyfile(str(parent) + "/dict_metalvis_id.py", str(parent) + "/backup_dict_metalvis_id.py"))

            # выводит размеры бэкапов
            backup_file_size = os.path.getsize(str(parent) + "/backup_dict_metalvis_id.py")
            old_file_size = os.path.getsize(str(parent) + "/dict_metalvis_id.py")
            print("new file size:" + str(old_file_size) + "; backup size:" + str(backup_file_size))

            # создание бэкапа из словаря
            copy = shutil.copyfile(str(parent) + "/dict_metalvis_id.py", str(parent) + "/backup_dict_metalvis_id.py")
            print ("создание бэкапа словаря: " + str(copy))

            open_dict = open(str(parent) + "/dict_metalvis_id.py", "r")
            # создание шаблона для добавления нового значение
            add_item = ('"' + str(new_din) + '"' + ' : ' + '"' + str(new_metalvis_id) + '"' + ',')

            sets = str(open_dict.read())
            sets = sets.replace("}", "")

            new_item = (str(sets) + str(add_item) +"}")

            open_dict = open(str(parent) + "/dict_metalvis_id.py", "w")
            write_item = open_dict.write(str(new_item))

            open_dict = open(str(parent) + "/dict_metalvis_id.py", "r")
            sets = str(open_dict.read())

            print ("Записан новый ключ в словаре")

        else:
            print("Не известная команда")
            module_admin()
    else:
        start()

# Module 5 - справочник по мелкому шагу для метрики
def module_fine_pitch_fasteners():
    dic_fine_pitch_fasteners = {
    "4" : "0.7",
    "5" : "0.8",
    "6" : "1",
    "8" : "1.25, 1",
    "10" : "1.5, 1, 1.25",
    "12" : "1.75, 1.5, 1.25",
    "14" : "2, 1.5",
    "16" : "2, 1.5",
    "18" : "2.5, 1.5, 2",
    "20" : "2.5, 2, 1.5",
    "22" : "2.5, 1.5, 2",
    "24" : "3, 2",
    "27" : "3, 2, 1.5",
    "30" : "3.5, 2",
    "33" : "3.5, 2",
    "36" : "4, 3",
    "39" : "4, 3",
    "42" : "4.5, 3",
    "48" : "5, 3",
    }
    
    # Вывод всего списка ключей словаря и его очистка от мусора
    show_all_keys = str(dic_fine_pitch_fasteners.keys())
    replace_trash = show_all_keys.replace("'", "")
    replace_trash = replace_trash.replace("dict_keys([", "Доступные диаметры: \n")
    replace_trash = replace_trash.replace("])", "")
    print (replace_trash)

    # запрос на ввод ключа-диаметра и перевод полученного словаря в список, удаление лишних пробелов
    diametr_of_fasteners = input("\nВведите диаметр: ")
    get_thread_pitch = dic_fine_pitch_fasteners.get(diametr_of_fasteners)
    

    # если введеного диаметра нет в списке ключей - беда, иначе - вывод списка ШР с комментариями
    if get_thread_pitch == None:
        print (str(diametr_of_fasteners) + " - неправильный или не стандартный размер")
    else:
        get_thread_pitch = get_thread_pitch.replace(" ","")
        convert_to_list_of_thread_pitch = list(get_thread_pitch.split(","))
        print ("")
        count_of_thread_pitch = list(get_thread_pitch.split(","))
        len_of_thread_pitch = (len(count_of_thread_pitch))-1
        if len_of_thread_pitch == 0:
            print(str(convert_to_list_of_thread_pitch[0]) + " - стандартная резьба\n")
        elif len_of_thread_pitch == 1:
            print (str(convert_to_list_of_thread_pitch[0]) + " - стандартная резьба")
            print (str(convert_to_list_of_thread_pitch[1]) + " - мелкая резьба №1\n")
        elif len_of_thread_pitch == 2:
            print (str(convert_to_list_of_thread_pitch[0]) + " - стандартная резьба")
            print (str(convert_to_list_of_thread_pitch[1]) + " - мелкая резьба №1")
            print (str(convert_to_list_of_thread_pitch[2]) + " - мелкая резьба №2\n")
        else:
            print("Что-то пошло не так...")

# МЕНЮ запуска скриптов + главное меню
def start():
    module_test()

    line()
    print ("\nДоступные разделы справочника:\n\
    1: Преобразование ГОСТа в DIN\n\
    2: (Не активный)Просчет размеров для HV крепежа\n\
    3: (Не активный)Расчет веса метизов\n\
    4: (Не активный)Расчет количества химанкера\n\
    5: Поиск артикула Metalvis по известному DIN/ISO\n\
    6: Справочник по мелкому шагу для метрики\n\n\
    е: Выйти из программы\n\
    admin: Администрирование базы")

    module_start = input("Выберите раздел: ")

    if module_start == "1":
        os.system('clear')
        line()
        module_gost2din()

    elif module_start == "5":
        os.system('clear')
        line()
        module_din_in_metalvis_id()

    elif module_start == "6":
        os.system('clear')
        line()
        module_fine_pitch_fasteners()

    elif module_start == "admin":
        os.system('clear')
        line()
        module_admin()

    elif module_start == "e":
        os.system('clear')
        sys.exit()

    else:
        print("Сначала нужно выбрать активный раздел")
        start()

    start()


start()
