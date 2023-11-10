import customtkinter
from classes_help_window import WindowForFastSearchOrgan, WindowForFastSearch
import tkinter
from tkinter import messagebox
from distribution_api import GetDataForWorkedWidgets

frame_default_color = "#F5DEB3"


class SimpleEntry(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_widget: str,
                 width_entry: int,
                 checkout_name: str = "off"):
        super().__init__(master=master, fg_color="#F5DEB3")

        self.checkout_name = checkout_name

        self.ent_lab = customtkinter.CTkLabel(self, text=name_widget)
        self.ent_lab.grid(row=0, column=0, sticky="nw")
        self.ent = customtkinter.CTkEntry(self, width=width_entry)
        self.ent.grid(row=1, column=0, sticky="sw")

    def get_value(self):
        if self.checkout_name == "on":
            result_checkout = self.validation_name()
            if result_checkout == True:
                return self.ent.get().title()
            else:
                messagebox.showerror(title="Ошибка", message="Неверно введено имя или отчество")
        else:
            return self.ent.get().title()

    def validation_name(self):
        pass
        # res = self.ent.get()
        # res_list = res.split(" ")
        # if res_list[1] not in list_all_name:
        #     return False
        # elif res_list[2] not in list_all_over_last_name:
        #     return False
        # else:
        #     return True

    def clean_en(self):
        self.ent.delete(first_index=0, last_index=50)


class SeriesNumberDocument(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)

        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_data(second_table="series_docx", index_element=3)
        self.object_for_get_data.close_data_base()

        self.ser_lab = customtkinter.CTkLabel(self, text="Cерия")
        self.ser_lab.grid(row=0, column=0, sticky="w")

        self.ser_lab_en = customtkinter.CTkComboBox(self, values=self.result_list[0], width=58)
        self.ser_lab_en.grid(row=1, column=0, sticky="w")
        self.ser_lab_en.set(self.result_list[1])

        self.num_doc = customtkinter.CTkLabel(self, text="Номер")
        self.num_doc.grid(row=0 ,column=1, padx=3, sticky="w")

        self.num_doc_en = customtkinter.CTkEntry(self, width=80)
        self.num_doc_en.grid(row=1, column=1, padx=3, sticky="w")

        self.time_reliz = customtkinter.CTkLabel(self, text="Дата выдачи")
        self.time_reliz.grid(row=0, column=2, padx=3, sticky="w")

        self.time_reliz_day_en = customtkinter.CTkEntry(self, width=90)
        self.time_reliz_day_en.grid(row=1, column=2, padx=3, sticky="w")

    def get_value(self):
        var_series_docx = self.ser_lab_en.get()
        var_number_docx = self.num_doc_en.get()

        res_str = self.time_reliz_day_en.get()
        result_data = res_str[:2] + "." + res_str[2:4] + "." + res_str[4::]

        return [var_series_docx, var_number_docx, result_data]

    def clean_en(self):
        self.num_doc_en.delete(first_index=0, last_index=15)
        self.time_reliz_day_en.delete(first_index=0, last_index=15)



class PersonalNumberDocument(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)

        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_data(second_table="letters", index_element=4)
        self.result_list_2 = self.object_for_get_data.get_data(second_table="id_citizen", index_element=5)
        self.object_for_get_data.close_data_base()

        self.main_label = customtkinter.CTkLabel(self, text="Личный номер")
        self.main_label.grid(row=0, column=0, sticky="w", columnspan=2)

        self.entry_for_7_numbers = customtkinter.CTkEntry(self, width=70)
        self.entry_for_7_numbers.grid(row=1, column=0)

        self.id_region = customtkinter.CTkComboBox(self, values=self.result_list[0], width=33)
        self.id_region.grid(row=1, column=1)
        self.id_region.set(self.result_list[1])

        self.zero_label = customtkinter.CTkLabel(self, text="0")
        self.zero_label.grid(row=1, column=2, padx=2)

        self.entry_for_2_numbers = customtkinter.CTkEntry(self, width=30)
        self.entry_for_2_numbers.grid(row=1, column=3)

        self.id_citizen = customtkinter.CTkComboBox(self, values=self.result_list_2[0], width=65)
        self.id_citizen.grid(row=1, column=4)
        self.id_citizen.set(self.result_list_2[1])

        self.check_digit = customtkinter.CTkEntry(self, width=30)
        self.check_digit.grid(row=1, column=5)

    def get_values(self):
        for_7_numbers = self.entry_for_7_numbers.get()
        letter = self.id_region.get()
        for_2_numbers = self.entry_for_2_numbers.get()
        pb = self.id_citizen.get()
        last_check_number = self.check_digit.get()
        return for_7_numbers + letter + "0" + for_2_numbers + pb + last_check_number

    def clean_en(self):
        self.entry_for_7_numbers.delete(first_index=0, last_index=15)
        self.entry_for_2_numbers.delete(first_index=0, last_index=5)
        self.check_digit.delete(first_index=0, last_index=5)


class WhoGivePassport(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)

        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_data(second_table="table_default_list_organs", index_element=6)

        self.name_widget = customtkinter.CTkLabel(self, text="Орган, выдавший документ")
        self.name_widget.grid(row=0, column=0, sticky="w")

        self.organ_lab_en = customtkinter.CTkComboBox(self, values=self.result_list[0], width=270)
        self.organ_lab_en.grid(row=1, column=0)
        self.organ_lab_en.set(self.result_list[1])

        self.button_for_fast_search_organs = customtkinter.CTkButton(self, text="📗", width=35, fg_color="green",
                                                                     command=self.open_window_for_search_organ)
        self.button_for_fast_search_organs.grid(row=1, column=1)

    def open_window_for_search_organ(self):
        self.pop_up_window = WindowForFastSearchOrgan(name_win="Все органы выдающие документы")
        self.pop_up_window.mainloop()


class DateReleaseDocument(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_date: str):
        super().__init__(master=master, fg_color=frame_default_color)
        self.time_reliz = customtkinter.CTkLabel(self, text=name_date)
        self.time_reliz.grid(row=0, column=0, sticky="w")

        self.time_reliz_day_en = customtkinter.CTkEntry(self, width=90)
        self.time_reliz_day_en.grid(row=1, column=0)


class DateReleaseDocument2(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_date: str):
        super().__init__(master=master, fg_color=frame_default_color)
        twin_time_reliz = customtkinter.CTkLabel(self, text=name_date)
        twin_time_reliz.grid(row=0, column=0, sticky="w", columnspan=3)

        self.twin_time_reliz_day_en = customtkinter.CTkComboBox(self,
                                                                values=["01", "02", "03", "04"], width=70)
        self.twin_time_reliz_day_en.grid(row=1, column=0)

        self.twin_time_reliz_month_en = customtkinter.CTkComboBox(self,
                                                                  values=["01", "02", "03", "04"], width=70)
        self.twin_time_reliz_month_en.grid(row=1, column=1)

        self.twin_time_reliz_year_en = customtkinter.CTkComboBox(self,
                                                                 values=["1990", "1991", "1992"], width=70)
        self.twin_time_reliz_year_en.grid(row=1, column=2)


class AddressLogging(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.local_reg = customtkinter.CTkLabel(self, text="Адрес регистрации")
        self.local_reg.grid(row=0, column=0, sticky="w", columnspan=2)

        self.local_reg_en1 = customtkinter.CTkComboBox(self, values=["Брестская обл", "Гомельская обл", "Гродненская обл", "Минская обл",
                      "Могилевская обл", "Витебская обл"], width=150)
        self.local_reg_en1.grid(row=1, column=0, sticky="w")

        self.local_reg_en2 = customtkinter.CTkComboBox(self, values=['Cтолинский р-н', 'Барановичский Р-н', 'Берёзовский Р-н', 'Брестский Р-н', 'Ганцевичский Р-н',
                'Дрогичинский Р-н', 'Жабинковский Р-н', 'Ивановский Р-н', 'Ивацевичский Р-н', 'Каменецкий Р-н',
                'Кобринский Р-н', 'Лунинецкий Р-н', 'Ляховичский Р-н', 'Малоритский Р-н', 'Пинский Р-н',
                'Пружанский Р-н'],
                                                       width=150, )
        self.local_reg_en2.grid(row=1, column=1, columnspan=2, padx=0, sticky="w")

        self.local_reg_en3 = customtkinter.CTkComboBox(self, values=["г.Давид-Городок", "г.Столин", "Н.п.Туры", "Н.п.Хорск", "аг.Ольшаны", "аг.Рубель", "Н.п.Ремель",
                 "Н.п.Хотомель", "Н.п.Хоромск", "Н.п.Турское", "Н.п.Теребличи", "Н.п.Старина", "Н.п.Семигостичи",
                 "Н.п.Ольпень", "Н.п.Ольманы", "Н.п.Ольгомель", "Н.п.Оздамичи", "Н.п.Мочуль", "Н.п.Малые орлы",
                 "Н.п.Лядец", "Н.п.Лутки", "Н.п.Лисовичи", "Н.п.Высокое", "Н.п.Велемичи", "Н.п.Большие орлы",
                 "Н.п.Бережное"], width=145)
        self.local_reg_en3.grid(row=2, column=0, sticky="w")

        self.button_for_fast_search_town = customtkinter.CTkButton(self, text="📗", width=35, fg_color="green",
                                                                   command=self.open_window_for_fast_search)
        self.button_for_fast_search_town.grid(row=2, column=1, padx=18, sticky="w")

        self.local_reg_en4_lab = customtkinter.CTkComboBox(self, values=["Ул.", "Пер."], width=60)
        self.local_reg_en4_lab.grid(row=2, column=1, padx=75, sticky="w")

        self.local_reg_en4 = customtkinter.CTkEntry(self, width=155, placeholder_text="Название улицы")
        self.local_reg_en4.grid(row=3, column=0)

        self.local_reg_en5_lab = customtkinter.CTkLabel(self, text="Д.")
        self.local_reg_en5_lab.grid(row=3, column=1, padx=0, sticky="w")

        self.local_reg_en5 = customtkinter.CTkEntry(self, width=40)
        self.local_reg_en5.grid(row=3, column=1, padx=15, sticky="w")

        self.local_reg_last_en6_lab = customtkinter.CTkLabel(self, text="Кв.")
        self.local_reg_last_en6_lab.grid(row=3, column=1, sticky="w", padx=57)

        self.local_reg_last_en6 = customtkinter.CTkEntry(self, width=60)
        self.local_reg_last_en6.grid(row=3, column=1, sticky="w", padx=75)

    def open_window_for_fast_search(self):
        pop_up_window = WindowForFastSearch(name_win="Выбор города", button_text="Выбрать",
                                            button_text2="Поиск")
        pop_up_window.mainloop()


class WorkedNumberTelephone(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_widget: str):
        super().__init__(master=master, fg_color=frame_default_color)
        self.connect_use_lab = customtkinter.CTkLabel(self, text=name_widget)
        self.connect_use_lab.grid(row=0, column=0, sticky="w", columnspan=3)

        self.connect_use_lab1 = customtkinter.CTkLabel(self, text="+375")
        self.connect_use_lab1.grid(row=1, column=0)

        self.connect_use_cod_lab = customtkinter.CTkComboBox(self, values=["29", "33", "44"],
                                                             width=60)
        self.connect_use_cod_lab.grid(row=1, column=1)

        self.connect_use = customtkinter.CTkEntry(self, width=120)
        self.connect_use.grid(row=1, column=2)


class NumberForExecuteOperation(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.of_use_num_lab = customtkinter.CTkLabel(self,
                                                text="Номер для проведения операции в формате: "
                                                     "ХХХ ХХ ХХ")
        self.of_use_num_lab.grid(row=0, column=0, sticky="w", columnspan=3)

        self.of_use_num = customtkinter.CTkEntry(self, width=120)
        self.of_use_num.grid(row=1, column=0)

        self.chk_var = tkinter.IntVar()
        self.chk = customtkinter.CTkCheckBox(self,
                                             text="Портированный номер \n(здесь формат ввода "
                                                  "ХХ ХХХ ХХ ХХ)", font=("Arial Bold", 10),
                                             variable=self.chk_var, onvalue=1, offvalue=0)
        self.chk.grid(row=1, column=1)


class IdWorker(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.id_worker_lab = customtkinter.CTkLabel(self, text="ID")
        self.id_worker_lab.grid(row=0, column=0, sticky="w")

        self.id_worker = customtkinter.CTkComboBox(self, values=["17660280", "9423193"], width=120)
        self.id_worker.grid(row=1, column=0)


class FieldForNumberSimCard(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.twin_sim_num_lab = customtkinter.CTkLabel(self, text="Номер sim-Карты")
        self.twin_sim_num_lab.grid(row=0, column=0, columnspan=2, sticky="w")

        self.twin_sim_lab_default = customtkinter.CTkLabel(self, text="8937502")
        self.twin_sim_lab_default.grid(row=1, column=0)

        self.twin_sim_num = customtkinter.CTkEntry(self, width=120)
        self.twin_sim_num.grid(row=1, column=1, padx=3)


class CheckBoxWithText(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_widget: str,
                 value_on_off: str = "off"):
        super().__init__(master=master, fg_color=frame_default_color)
        self.chk_fio_var = tkinter.StringVar(value=value_on_off)
        self.err_check_fio_lab = customtkinter.CTkCheckBox(self, text=name_widget, font=("Arial Bold", 11),
                                                           variable=self.chk_fio_var,
                                                           onvalue="on", offvalue="off")
        self.err_check_fio_lab.grid(row=0, column=0)


class PlacePay(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_widget: str):
        super().__init__(master=master, fg_color=frame_default_color)
        self.err_filial_pay_lab = customtkinter.CTkLabel(self, text=name_widget)
        self.err_filial_pay_lab.grid(row=0, column=0, sticky="w")

        self.err_filial_pay = customtkinter.CTkComboBox(self, values=["беларусбанк", "белпочта",
                                                                      "приорбанк"], width=200)
        self.err_filial_pay.grid(row=1, column=0)

        self.button_for_fast_search_town = customtkinter.CTkButton(self, text="📗", width=35, fg_color="green",
                                                                   command=self.open_window_for_fast_search_banks)
        self.button_for_fast_search_town.grid(row=1, column=1, padx=3)

    def open_window_for_fast_search_banks(self):
        self.pop_up_window = WindowForFastSearch(name_win="Список всех банков РБ", button_text="Выбрать",
                                                 button_text2="Поиск")
        self.pop_up_window.mainloop()


class DoubleEntryForNumBankCard(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.err_first_sym_map_lab = customtkinter.CTkLabel(self, text="Первые 4 цифры БК", font=("Arial Bold", 12))
        self.err_first_sym_map_lab.grid(row=0, column=0, sticky="w", columnspan=2)

        self.err_first_sym_map = customtkinter.CTkEntry(self, width=60)
        self.err_first_sym_map.grid(row=1, column=0, sticky="w")

        self.err_second_sym_map_lab = customtkinter.CTkLabel(self, text="Последние 4 цифры БК", font=("Arial Bold", 12))
        self.err_second_sym_map_lab.grid(row=0, column=3, padx=15, sticky="w")

        self.err_second_sym_map = customtkinter.CTkEntry(self, width=60)
        self.err_second_sym_map.grid(row=1, column=3, padx=15, sticky="w")


class Tariffs(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        ch_ow_tariff_plan = customtkinter.CTkLabel(self, text="Трифный план")
        ch_ow_tariff_plan.grid(row=0, column=0, sticky="w")

        self.ch_ow_tariff_plan_en = customtkinter.CTkComboBox(self, values=["супер", "Супер голос",
                                                                            "Супер 10"], width=130)
        self.ch_ow_tariff_plan_en.grid(row=1, column=0)


class TariffsWithCheckBox(Tariffs):
    def __init__(self,
                 master: any):
        super().__init__(master=master)
        self.chk_for_change_tp = tkinter.IntVar()
        self.chk_vidget_for_change_tp = customtkinter.CTkCheckBox(self, text="Cмена Тарифного плана",
                                                                  font=("Arial Bold", 11),
                                                                  variable=self.chk_for_change_tp, onvalue=1,
                                                                  offvalue=0)
        self.chk_vidget_for_change_tp.grid(row=1, column=2, padx=5)


class PlaceBirthday(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.ch_ow_place_birthday = customtkinter.CTkLabel(self, text="Место рождения")
        self.ch_ow_place_birthday.grid(row=0, column=0, sticky="w")

        self.ch_ow_place_birthday_en1 = customtkinter.CTkComboBox(self, values=["Брестская обл", "Витебская обл"], width=150)
        self.ch_ow_place_birthday_en1.grid(row=1, column=0)

        self.ch_ow_place_birthday_en2 = customtkinter.CTkComboBox(self, values=["Давид-Городок", "Велемичи"],
                                                                  width=150)
        self.ch_ow_place_birthday_en2.grid(row=1, column=1, padx=10)

        self.button_for_fast_search_town = customtkinter.CTkButton(self, text="📗", width=35, fg_color="green",
                                                                   command=self.open_window_for_select_town)
        self.button_for_fast_search_town.grid(row=1, column=2, padx=3)

    def open_window_for_select_town(self):
        pop_up_window = WindowForFastSearch(name_win="Выбор города", button_text="Выбрать", button_text2="Поиск")
        pop_up_window.mainloop()


class InfoBar(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, width=700, height=55,
                         fg_color="#F5F5DC",border_color="#808080",
                         border_width=1, corner_radius=10)

        self.fin_lab = customtkinter.CTkLabel(self, text="Заполните форму, нажмите 'Готово'",
                                              font=("Arial Bold", 20),
                                              text_color="black")
        self.fin_lab.grid(row=0, column=0, padx=180, pady=5, sticky="w")


    def change_void_text(self, text_mess):
        def local_change_text():
            self.fin_lab.configure(text="Заполните форму, нажмите 'Готово'", text_color="black")
        self.fin_lab.configure(text=text_mess, text_color="green")
        self.fin_lab.after(8000, local_change_text)


def gener_mess(name_dir):
    return f"Документ готов в папке: {name_dir}"

def message_about_finish(frame, name_frame, x, y, name_dir, font_size=19):
    fin_lab = customtkinter.CTkLabel(frame.tab(name_frame), text=f"Документ готов в папке: {name_dir}",
                                     font=("Arial Bold", font_size),
                                     text_color="red")
    fin_lab.place(relx=x, rely=y)
    fin_lab.after(6000, fin_lab.destroy)
