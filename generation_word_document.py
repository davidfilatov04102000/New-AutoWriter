from docxtpl import DocxTemplate
import customtkinter
import time
import pprint
from generation_string_from_digit import IntToString
from modul_for_checkout_full_name import generator_another_case
import os, sys
import traceback


class WindowShowError:
    def __init__(self, res, real_path, generated_path):
        self.res = res
        self.real_path = real_path
        self.generated_path = generated_path
        error_window = customtkinter.CTk()
        error_window.title("error window")
        error_window.geometry("600x400")

        text_box = customtkinter.CTkTextbox(error_window, width=600, height=400)
        text_box.grid(row=0, column=0, sticky="wnes")
        text_box.insert("0.0", f"{self.real_path}\n\n{self.res}\n\n{self.generated_path}")

        error_window.mainloop()

class DateToday:
    def __init__(self):
        self.seconds = time.time()
        self.day = time.localtime(self.seconds)[2]
        self.month = time.localtime(self.seconds)[1]
        self.year_result = time.localtime(self.seconds)[0]

        self.month_list = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
                           "Июля", "Августа", "Cентября", "Октября", "Ноября", "Декабря"]

        self.day_result = f"{self.day}"
        self.month_result = f"{self.month}"

        if self.day < 10:
            self.day_result = f"0{self.day}"
        if self.month < 10:
            self.month_result = f"0{self.month}"

    def date_today(self):
        return f"{self.day_result}.{self.month_result}.{self.year_result}"

    def day_with_month(self):
        return f"{self.day_result} {self.month_list[self.month-1]}"

    def return_list_value(self):
        return [self.day_result, self.month, self.year_result]

    def return_list_value_2(self):
        for w in [self.day_result, self.month, self.year_result]:
            yield(w)


def handler_name_for_name_file(string):
    time_list = string.split(" ")
    return time_list


def separator_name_organs(name_organ):
    list_separators = ["РОВД", "РУВД", "ГОВД"]
    list_separators_2 = ["г."]
    count = 0
    for u in list_separators:
        if u in name_organ:
            count += 1
            if list_separators_2[0] in name_organ:
                index_separator = name_organ.index(list_separators_2[0])
                list_from_name_organ = [name_organ[:index_separator-1], name_organ[index_separator-1::]]
                return list_from_name_organ
            else:
                index_separator = name_organ.index(u)
                list_from_name_organ = [name_organ[:index_separator+4], name_organ[index_separator+5::]]
                return list_from_name_organ
    if count == 0:
        if list_separators_2[0] in name_organ:
            index_separator = name_organ.index(list_separators_2[0])
            list_from_name_organ = [name_organ[:index_separator - 1], name_organ[index_separator - 1::]]
            return list_from_name_organ


def cutting_str_path(path):
    path_list = []
    reversed_path_str = path[::-1]
    for y in reversed_path_str:
        path_list.append(y)

    # result_pass = None

    i, count = 0, 0
    while i < 2:
        if i == 2:
            break
        elif path_list[count] == "\\":
            i += 1
            path_list.pop(count)
        else:
            path_list.pop(count)

    path_str = "".join(path_list)
    result_pass = path_str[::-1]
    return result_pass


if getattr(sys, 'frozen', False):
    full_path_to_exe = sys._MEIPASS
    application_path = cutting_str_path(full_path_to_exe)
else:
    full_path_to_exe = os.path.dirname(os.path.abspath(__file__))
    application_path = cutting_str_path(full_path_to_exe)


def function_for_fast_add(*args):
    for i in args:
        yield i


def generation_document_for_change_tariff(argument_list: list):
    list_variable_for_template = ["dogn", "name", "ser", "num", "ln", "organ", "datev", "adr_registr",
                                  "kon_num", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9",
                                  "init_worker", "id", "today", "month", "year"]
    gen = (a for a in argument_list[9])
    for_date_today = DateToday()
    gen_2 = for_date_today.return_list_value_2()
    data_list = list(function_for_fast_add(argument_list[2], argument_list[3].title(), argument_list[4][0],
                                           argument_list[4][1], argument_list[5], argument_list[6], argument_list[4][2],
                                           argument_list[7], argument_list[8], *gen, argument_list[10][1],
                                           argument_list[10][0], *gen_2))
    name_for_file = handler_name_for_name_file(argument_list[3])[0:2].title()
    data_dict = dict(zip(list_variable_for_template, data_list))

    finish_point = 0
    shet = 1
    global application_path
    global full_path_to_exe
    try:
        while finish_point != 1:
            if os.path.exists(
                f"{full_path_to_exe}\Документы\Все свои\Смена ТП на все свои {name_for_file} {shet}.docx") is True:
                shet += 1
            else:
                doc = DocxTemplate(f"{full_path_to_exe}\examples\privet.docx")

                context = data_dict
                doc.render(context)
                doc.save(f"{full_path_to_exe}\Документы\Все свои\Смена ТП на все свои {name_for_file} {shet}.docx")
                finish_point += 1
    except Exception as e:
        error_message = traceback.format_exc()
        error_window = WindowShowError(error_message, application_path, full_path_to_exe)


def generation_document_including_second_sim_card(argument_list: list):
    # global application_path
    # global full_path_to_exe
    # print(application_path)
    # print(full_path_to_exe)
    list_variable_for_template = ["dogn", "name", "ser", "num", "ln", "organ", "datev",
                                  "adr_registr", "kon_num", "n1", "n2", "n3", "n4", "n5",
                                  "n6", "n7", "n8", "n9", "twin_num", "init_worker", "today", "month", "year"]
    gen = (a for a in argument_list[9])
    for_date_today = DateToday()
    gen_2 = for_date_today.return_list_value_2()
    data_list = list(function_for_fast_add(argument_list[2], argument_list[3].title(), argument_list[4][0],
                                           argument_list[4][1], argument_list[5], argument_list[6], argument_list[4][2],
                                           argument_list[7], argument_list[8], *gen, argument_list[10], argument_list[11][1], *gen_2))
    name_for_file = handler_name_for_name_file(argument_list[3])[0:2].title()
    data_dict = dict(zip(list_variable_for_template, data_list))

    finish_point = 0
    shet = 1
    global application_path
    global full_path_to_exe
    try:
        while finish_point != 1:
            if os.path.exists(
                f"{full_path_to_exe}\Документы\Подключение Твин-Карты\Подключение Твин-Карты {name_for_file} {shet}.docx") is True:
                shet += 1
            else:
                doc = DocxTemplate(f"{full_path_to_exe}\examples\Twin-karta.docx")

                context = data_dict
                doc.render(context)
                doc.save(
                    f"{full_path_to_exe}\Документы\Подключение Твин-Карты\Подключение Твин-Карты {name_for_file} {shet}.docx")
                finish_point += 1
    except Exception as e:
        error_message = traceback.format_exc()
        error_window = WindowShowError(error_message, application_path, full_path_to_exe)


def generation_document_in_case_error_pay(argument_list: list):
    list_variable_for_template = ["name", "ser", "num", "organ", "datev_day", "datev_month", "datev_year", "ln", "num_for_zach",
                         "user_num", "sum_dig", "sum_prop", "num_zach", "filial_pay", "num_doc_pay", "date_pay",
                         "today", "month", "year", "last_name_inits", "user_map", "first_num_map", "last_num_map", "id",
                         "init_worker"]
    if argument_list[7] == "on":
        whom = generator_another_case(argument_list[2])
    else:
        whom = argument_list[8].title()
    date_in_list = argument_list[3][2].split(".")
    object_for_convert_int_to_str = IntToString(argument_list[9])
    amount_string = object_for_convert_int_to_str.return_value()
    for_date_today = DateToday()
    gen_2 = for_date_today.return_list_value_2()
    name_in_list = handler_name_for_name_file(argument_list[2])
    last_name_with_init_str = f"{name_in_list[0].title()} {name_in_list[1][0].title()}.{name_in_list[2][0].title()}."

    data_list = list(function_for_fast_add(argument_list[2].title(), argument_list[3][0], argument_list[3][1], argument_list[5],
                                           date_in_list[0], date_in_list[1], date_in_list[2], argument_list[4],
                                           argument_list[6], whom, argument_list[9], amount_string, argument_list[10],
                                           argument_list[11], argument_list[12], argument_list[14], *gen_2,
                                           last_name_with_init_str, argument_list[2].title(), argument_list[15][0],
                                           argument_list[15][1], argument_list[13][0], argument_list[13][1]))

    name_for_file = f"{name_in_list[0].title()} {name_in_list[1].title()}"
    data_dict = dict(zip(list_variable_for_template, data_list))

    finish_point = 0
    shet = 1
    global application_path
    global full_path_to_exe
    try:
        while finish_point != 1:
            if os.path.exists(
                f"{full_path_to_exe}\Документы\Ошибочная оплата\Ошибочная оплата {name_for_file} {shet}.docx") == (
            True):
                shet += 1
            else:
                err_doc = DocxTemplate(f"{full_path_to_exe}\examples\oshibka oplaty.docx")

                context = data_dict
                err_doc.render(context)
                err_doc.save(
                    f"{full_path_to_exe}\Документы\Ошибочная оплата\Ошибочная оплата {name_for_file} {shet}.docx")
                finish_point += 1
    except Exception as e:
        error_message = traceback.format_exc()
        error_window = WindowShowError(error_message, application_path, full_path_to_exe)


def generation_document_for_change_owner(argument_list: list):
    list_variable_for_template = ["dog_n", "today", "month", "year", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9",
                                    "name_own", "ser", "num_docx", "ln", "organ", "datev", "full_adress_reg_own",
                                    "name_receiver", "if_change_tp", "num_sim", "tp", "kod", "num", "first_name",
                                    "last_name", "over_last_name", "date_birthday", "place_birthday", "ser_receiver",
                                    "num_docx_receiver", "organ_receiver1", "field_organ_receiver", "organ_receiver",
                                    "datev_receiver", "ln_receiver", "field_reg", "district_reg", "town_reg",
                                    "street_reg",
                                    "home", "kv", "id", "worker", "full_worker"]
    for_date_today = DateToday()
    gen_collection_date = for_date_today.return_list_value_2()
    gen_number = (f for f in argument_list[3][3::])
    if argument_list[12][1] != 0:
        if_the_change_tariff = argument_list[12][0]
    else:
        if_the_change_tariff = ""
    list_from_name = handler_name_for_name_file(argument_list[9].title())
    separated_name_organs = separator_name_organs(argument_list[15])
    if argument_list[-2] == "on":
        address_logging_new_owner = argument_list[8]
    else:
        address_logging_new_owner = argument_list[-3]
    separated_address_logging = address_logging_new_owner.split(", ")
    if len(separated_address_logging) < 6:
        separated_address_logging.append(" ")
    gen_collection_address = (g for g in separated_address_logging)
    gen_collection_data_about_worker = (s for s in argument_list[-1])
    data_list = list(function_for_fast_add(argument_list[2], *gen_collection_date, *gen_number, argument_list[4].title(),
                                           argument_list[5][0], argument_list[5][1], argument_list[6], argument_list[7],
                                           argument_list[5][2], argument_list[8], argument_list[9].title(), if_the_change_tariff,
                                           argument_list[10], argument_list[12][0], argument_list[3][3:5],
                                           argument_list[3][5::], list_from_name[0], list_from_name[1], list_from_name[2],
                                           argument_list[11], argument_list[13], argument_list[-6][0], argument_list[-6][1],
                                           separated_name_organs[0], separated_name_organs[1], argument_list[15],
                                           argument_list[-6][2], argument_list[-4], *gen_collection_address,
                                           *gen_collection_data_about_worker))
    name_for_file = f"{argument_list[4][0].title()} {argument_list[4][1].title()}"
    data_dict = dict(zip(list_variable_for_template, data_list))

    finish_point = 0
    shet_1 = 1
    shet_2 = 1
    shet_3 = 1
    global application_path
    global full_path_to_exe
    try:
        while finish_point != 1:
            if os.path.exists(
                f"{full_path_to_exe}\Документы\Смена владельца\Акт приема передачи {name_for_file} {shet_1}.docx") is True:
                shet_1 += 1
            if os.path.exists(
                f"{full_path_to_exe}\Документы\Смена владельца\Договор {name_for_file} {shet_2}.docx") is True:
                shet_2 += 1
            if os.path.exists(f"{full_path_to_exe}\Документы\Смена владельца\Отказ {name_for_file} {shet_3}.docx") is True:
                shet_3 += 1
            else:
                ch_ow_doc1 = DocxTemplate(f"{full_path_to_exe}\examples\smena_vladeltsa.docx")

                context1 = data_dict
                ch_ow_doc1.render(context1)
                ch_ow_doc1.save(
                    f"{full_path_to_exe}\Документы\Смена владельца\Акт приема передачи {name_for_file} {shet_1}.docx")

                ch_ow_doc2 = DocxTemplate(f"{full_path_to_exe}\examples\dogovor.docx")

                context2 = data_dict
                ch_ow_doc2.render(context2)
                ch_ow_doc2.save(f"{full_path_to_exe}\Документы\Смена владельца\Договор {name_for_file} {shet_2}.docx")

                ch_ow_doc3 = DocxTemplate(f"{full_path_to_exe}\examples\otkaz_ot_reklamy.docx")

                context3 = data_dict
                ch_ow_doc3.render(context3)
                ch_ow_doc3.save(f"{full_path_to_exe}\Документы\Смена владельца\Отказ {name_for_file} {shet_3}.docx")
                finish_point += 1
    except Exception as e:
        error_message = traceback.format_exc()
        error_window = WindowShowError(error_message, application_path, full_path_to_exe)


def generation_document_for_refund_number_last_owner(argument_list: list):
    list_variable_for_template = ["dog_n", "num_sim", "tp", "kod", "num", "first_name", "last_name", "over_last_name", "name_receiver",
                     "date_birthday", "place_birthday", "ser_receiver", "num_docx_receiver", "organ_receiver1",
                     "field_organ_receiver", "organ_receiver", "datev_receiver", "ln_receiver", "field_reg", "district_reg", "town_reg",
                     "street_reg", "home", "kv", "id", "worker", "full_worker", "today", "month", "year", "sum"]
    list_from_name = handler_name_for_name_file(argument_list[2])
    gen_collection_name = (a for a in list_from_name)
    separated_name_organ = separator_name_organs(argument_list[5])
    separated_address_logging = argument_list[8].split(", ")
    if len(separated_address_logging) < 6:
        separated_address_logging.append(" ")
    gen_collection_address = (g for g in separated_address_logging)
    for_date_today = DateToday()
    gen_collection_date = for_date_today.return_list_value_2()
    gen_collection_data_about_worker = (t for t in argument_list[-1])
    data_list = list(function_for_fast_add(argument_list[9], argument_list[9], argument_list[10], argument_list[-3][0:2],
                                           argument_list[-3][2::], *gen_collection_name, argument_list[2], argument_list[7],
                                           argument_list[6], argument_list[3][0], argument_list[3][1],
                                           separated_name_organ[0], separated_name_organ[1], argument_list[5],
                                           argument_list[3][2], argument_list[4], *gen_collection_address,
                                           argument_list[-1][0], *gen_collection_data_about_worker, *gen_collection_date,
                                           argument_list[-2]))
    name_for_file = f"{list_from_name[0].title()} {list_from_name[1].title()}"
    data_dict = dict(zip(list_variable_for_template, data_list))

    finish_point = 0
    shet_1 = 1
    shet_2 = 1
    global application_path
    global full_path_to_exe
    try:
        while finish_point != 1:
            if os.path.exists(
                f"{full_path_to_exe}\Документы\Возврат номера\Предоставление номера {name_for_file} {shet_1}.docx") == (
                True):
                shet_1 += 1
            elif os.path.exists(
                f"{full_path_to_exe}\Документы\Возврат номера\Отказ {name_for_file} {shet_2}.docx") == (
                True):
                shet_2 += 1
            else:
                doc = DocxTemplate(f"{full_path_to_exe}\examples\dogovor_for_receiver.docx")

                context = data_dict
                doc.render(context)
                doc.save(
                    f"{full_path_to_exe}\Документы\Возврат номера\Предоставление номера {name_for_file} {shet_1}.docx")

                doc_2 = DocxTemplate(f"{full_path_to_exe}\examples\otkaz_ot_reklamy.docx")

                context_2 = data_dict
                doc_2.render(context_2)
                doc_2.save(f"{full_path_to_exe}\Документы\Возврат номера\Отказ {name_for_file} {shet_2}.docx")
                finish_point += 1
    except Exception as e:
        error_message = traceback.format_exc()
        error_window = WindowShowError(error_message, application_path, full_path_to_exe)