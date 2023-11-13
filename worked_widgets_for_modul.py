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
        self.pop_up_window = WindowForFastSearchOrgan(name_win="Все органы выдающие документы",
                                                      button_event=self.configure_value)
        self.pop_up_window.mainloop()

    def configure_value(self, value):
        self.organ_lab_en.set(value)

    def get_value(self):
        return self.organ_lab_en.get()


class DateReleaseDocument(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_date: str):
        super().__init__(master=master, fg_color=frame_default_color)
        self.time_reliz = customtkinter.CTkLabel(self, text=name_date)
        self.time_reliz.grid(row=0, column=0, sticky="w")

        self.time_reliz_day_en = customtkinter.CTkEntry(self, width=90)
        self.time_reliz_day_en.grid(row=1, column=0)

    def get_values(self):
        res_str = self.time_reliz_day_en.get()
        res1 = res_str[:2]
        res2 = res_str[2:4]
        res3 = res_str[4::]
        return res1 + "." + res2 + "." + res3

    def clean_en(self):
        self.time_reliz_day_en.delete(first_index=0, last_index=15)


class DateReleaseDocument2(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_date: str):
        super().__init__(master=master, fg_color=frame_default_color)
        twin_time_reliz = customtkinter.CTkLabel(self, text=name_date)
        twin_time_reliz.grid(row=0, column=0, sticky="w", columnspan=3)

        object_for_get_data = GetDataForWorkedWidgets()
        result_list = object_for_get_data.return_data_for_dates()

        self.twin_time_reliz_day_en = customtkinter.CTkComboBox(self,
                                                                values=result_list[0], width=70)
        self.twin_time_reliz_day_en.grid(row=1, column=0)

        self.twin_time_reliz_month_en = customtkinter.CTkComboBox(self,
                                                                  values=result_list[1], width=70)
        self.twin_time_reliz_month_en.grid(row=1, column=1)

        self.twin_time_reliz_year_en = customtkinter.CTkComboBox(self,
                                                                 values=result_list[2], width=70)
        self.twin_time_reliz_year_en.grid(row=1, column=2)

    def get_values(self):
        res1 = self.twin_time_reliz_day_en.get()
        res2 = self.twin_time_reliz_month_en.get()
        res3 = self.twin_time_reliz_year_en.get()
        return res1 + "." + res2 + "." + res3


class AddressLogging(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)

        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_data_for_widget_place_logging()
        self.object_for_get_data.close_data_base()

        self.default_value = self.result_list[0]
        self.default_id = self.result_list[1]
        self.list_field = self.result_list[2]
        self.list_district_in_field = self.result_list[3]
        self.full_list_district = self.result_list[4]
        self.full_list_town = self.result_list[5]


        self.local_reg = customtkinter.CTkLabel(self, text="Адрес регистрации")
        self.local_reg.grid(row=0, column=0, sticky="w", columnspan=2)

        self.local_reg_en1 = customtkinter.CTkComboBox(self, values=self.list_field, width=150,
                                                       command=self.combobox_callback)
        self.local_reg_en1.grid(row=1, column=0, sticky="w")
        self.local_reg_en1.set(self.default_value[0])

        self.local_reg_en2 = customtkinter.CTkComboBox(self, values=self.list_district_in_field[self.default_id[0]],
                                                       width=150, command=self.combobox_callback_2)
        self.local_reg_en2.grid(row=1, column=1, columnspan=2, padx=0, sticky="w")
        self.local_reg_en2.set(self.default_value[1])

        self.local_reg_en3 = customtkinter.CTkComboBox(self, values=self.full_list_town[self.default_id[1]], width=145)
        self.local_reg_en3.grid(row=2, column=0, sticky="w")
        self.local_reg_en3.set(self.default_value[2])
        self.list_town_for_combobox = self.full_list_town[self.default_id[1]].copy()

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

    def combobox_callback(self, value):
        for_district = self.list_field.index(value)
        new_dist_list = self.list_district_in_field[for_district]
        for_town = self.full_list_district.index(new_dist_list[0])
        self.local_reg_en2.configure(values=new_dist_list)
        self.local_reg_en2.set(new_dist_list[0])
        self.local_reg_en3.configure(values=self.full_list_town[for_town])
        self.local_reg_en3.set(self.full_list_town[for_town][0])
        self.list_town_for_combobox = self.full_list_town[for_town].copy()


    def combobox_callback_2(self, value):
        for_town = self.full_list_district.index(value)
        self.local_reg_en3.configure(values=self.full_list_town[for_town])
        self.local_reg_en3.set(self.full_list_town[for_town][0])
        self.list_town_for_combobox = self.full_list_town[for_town].copy()

    def set_value(self, value):
        self.local_reg_en3.set(value)

    def open_window_for_fast_search(self):
        pop_up_window = WindowForFastSearch(name_win="Выбор города", button_text="Выбрать",
                                            button_text2="Поиск", data=self.list_town_for_combobox,
                                            button_event=self.set_value)
        pop_up_window.after(200, pop_up_window.show_data)

    def get_values(self):
        res1, res2, res3 = self.local_reg_en1.get(), self.local_reg_en2.get(), self.local_reg_en3.get()
        res4, res5, res6, res7 = self.local_reg_en4_lab.get(), self.local_reg_en4.get(), self.local_reg_en5.get(), \
                                 self.local_reg_last_en6.get()
        if res7 == "":
            return res1 + ", " + res2 + ", " + res3 + ", " + res4 + " " + res5 + ", д. " + res6
        else:
            return res1 + ", " + res2 + ", " + res3 + ", " + res4 + " " + res5 + ", д. " + res6 + ", кв. " + res7

    def clean_en(self):
        self.local_reg_en4.delete(first_index=0, last_index=50)
        self.local_reg_en5.delete(first_index=0, last_index=5)
        self.local_reg_last_en6.delete(first_index=0, last_index=5)


class WorkedNumberTelephone(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_widget: str):
        super().__init__(master=master, fg_color=frame_default_color)
        self.connect_use_lab = customtkinter.CTkLabel(self, text=name_widget)
        self.connect_use_lab.grid(row=0, column=0, sticky="w", columnspan=3)

        self.connect_use_lab1 = customtkinter.CTkLabel(self, text="+375")
        self.connect_use_lab1.grid(row=1, column=0)

        self.connect_use_cod_lab = customtkinter.CTkComboBox(self, values=["29", "33", "44", "25"],
                                                             width=60)
        self.connect_use_cod_lab.grid(row=1, column=1)

        self.connect_use = customtkinter.CTkEntry(self, width=120)
        self.connect_use.grid(row=1, column=2)

    def get_values(self):
        res_cod, res_num = self.connect_use_cod_lab.get(), self.connect_use.get()
        return "375" + res_cod + res_num

    def clean_en(self):
        self.connect_use.delete(first_index=0, last_index=10)


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

    def get_values(self):
        chk = self.chk_var.get()
        res_num = self.of_use_num.get()
        if len(res_num) == 7:
            if res_num[0] in ["1", "4"]:
                self.of_use_num.delete(first_index=0, last_index=10)
                return False
            elif chk == 1:
                self.of_use_num.delete(first_index=0, last_index=10)
                return False
            else:
                if chk == 0:
                    kod_for_num_for_oper = ""
                    list_first_dig1 = ["2", "5", "7", "8"]
                    list_first_dig2 = ["3", "6", "9"]
                    if res_num[0] in list_first_dig1:
                        kod_for_num_for_oper = "29"
                    elif res_num[0] in list_first_dig2:
                        kod_for_num_for_oper = "33"
                    num_use_for_operation_finally = kod_for_num_for_oper + res_num
                    return num_use_for_operation_finally
        elif len(res_num) > 7:
            if chk == 0:
                self.of_use_num.delete(first_index=0, last_index=10)
                return False
            elif chk == 1:
                return res_num

    def clean_en(self):
        self.of_use_num.delete(first_index=0, last_index=15)

    def clean_chk(self):
        self.chk.deselect()

class IdWorker(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)

        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_data_about_workers()

        self.object_for_get_data.close_data_base()

        self.list_id_worker = self.result_list[0].copy()
        self.list_data_worker = self.result_list[1].copy()

        self.dict_for_data_worker = dict(zip(self.list_id_worker, self.list_data_worker))

        self.id_worker_lab = customtkinter.CTkLabel(self, text="ID")
        self.id_worker_lab.grid(row=0, column=0, sticky="w")

        self.id_worker = customtkinter.CTkComboBox(self, values=self.list_id_worker, width=120)
        self.id_worker.grid(row=1, column=0)

    def get_values(self):
        res_id = self.id_worker.get()
        different_info = self.dict_for_data_worker[res_id]
        return [res_id, different_info[0], different_info[1]]


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

    def get_values(self):
        res_sim = self.twin_sim_num.get()
        return "8937502" + res_sim

    def clean_en(self):
        self.twin_sim_num.delete(first_index=0, last_index=30)


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

    def get_values(self):
        return self.chk_fio_var.get()

    def clean_en(self):
        self.err_check_fio_lab.deselect()


class PlacePay(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_widget: str):
        super().__init__(master=master, fg_color=frame_default_color)
        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_any_list(table="banks")
        self.object_for_get_data.close_data_base()

        self.err_filial_pay_lab = customtkinter.CTkLabel(self, text=name_widget)
        self.err_filial_pay_lab.grid(row=0, column=0, sticky="w")

        self.err_filial_pay = customtkinter.CTkComboBox(self, values=self.result_list, width=200)
        self.err_filial_pay.grid(row=1, column=0)

        self.button_for_fast_search_town = customtkinter.CTkButton(self, text="📗", width=35, fg_color="green",
                                                                   command=self.open_window_for_fast_search_banks)
        self.button_for_fast_search_town.grid(row=1, column=1, padx=3)

    def set_value(self, value):
        self.err_filial_pay.set(value)

    def open_window_for_fast_search_banks(self):
        self.pop_up_window = WindowForFastSearch(name_win="Список всех банков РБ", button_text="Выбрать",
                                                 button_text2="Поиск", data=self.result_list, show_half_data="off",
                                                 button_event=self.set_value)
        self.pop_up_window.after(200, self.pop_up_window.show_data)

    def get_values(self):
        return self.err_filial_pay.get()


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

    def get_values(self):
        res_list = []
        res_list.append(self.err_first_sym_map.get())
        res_list.append(self.err_second_sym_map.get())
        return res_list

    def clean_en(self):
        self.err_first_sym_map.delete(first_index=0, last_index=10)
        self.err_second_sym_map.delete(first_index=0, last_index=10)


class Tariffs(customtkinter.CTkFrame):
    def __init__(self,
                 master: any):
        super().__init__(master=master, fg_color=frame_default_color)
        self.object_for_get_data = GetDataForWorkedWidgets()
        self.result_list = self.object_for_get_data.get_any_list(table="tariff_plan")
        self.object_for_get_data.close_data_base()

        ch_ow_tariff_plan = customtkinter.CTkLabel(self, text="Трифный план")
        ch_ow_tariff_plan.grid(row=0, column=0, sticky="w")

        self.ch_ow_tariff_plan_en = customtkinter.CTkComboBox(self, values=self.result_list, width=130)
        self.ch_ow_tariff_plan_en.grid(row=1, column=0)

    def get_values(self):
        res1 = self.ch_ow_tariff_plan_en.get()
        return res1


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

    def get_values(self):
        res_list = []
        res1 = self.ch_ow_tariff_plan_en.get()
        res2 = self.chk_for_change_tp.get()
        res_list.append(res1), res_list.append(res2)
        return res_list

    def clean_en(self):
        self.chk_vidget_for_change_tp.deselect()


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
