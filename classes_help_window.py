import customtkinter
from all_classes import TileWithResultSearch, CustomButton1, ButtonReferenceMod, TileForShowData, ButtonReferenceMod2
from distribution_api import SearchTownForDefaultInfo, RecordDefaultDataInTable, RecordWorkerInDataBase, \
    GetDataForWorkedWidgets
import time
from fuzzywuzzy import fuzz
from experience import AdditionalFunctional
from info_from_data_base import get_data


class ParentHelpWindow(customtkinter.CTkToplevel):
    """Родительский класс для вспомогательных окон"""
    def __init__(self,
                 name_win: str,
                 height_main_frame: int = 390
                ):
        super().__init__()
        self.title(name_win)
        self.width_win = 550
        self.height_win = 550
        self.geometry(f"{self.width_win}x{self.height_win}")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((1, 2), weight=1)

        #Создание фрейма вверху окна для поля ввода и кнопки поиска
        self.frame_for_tool_bar = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_tool_bar.grid(row=0, column=0, padx=2, pady=0, sticky="we")

        #Создание фрейма для вывода информации
        self.frame_main_job_field = customtkinter.CTkScrollableFrame(self, corner_radius=0)
        self.frame_main_job_field.grid(row=1, column=0, padx=2, pady=(2,2), sticky="wsen", rowspan=3)


class WindowForFastSearchOrgan(customtkinter.CTkToplevel):
    """Класс для быстрого поска органов"""
    def __init__(self,
                 name_win,
                 button_event=None):
        super().__init__()
        self.title(name_win)
        self.width_win = 700
        self.height_win = 450
        self.geometry(f"{self.width_win}x{self.height_win}")
        self.resizable(False, False)

        self.button_event = button_event

        self.columnconfigure(2, weight=1)

        from info_from_data_base import data_for_window_for_show_organs
        self.result_list = data_for_window_for_show_organs.copy()

        #Создание фрейма для кнопки выбрать сверху
        self.frame_for_tool_bar = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_tool_bar.grid(row=0, column=0, padx=0, pady=0, sticky="we", columnspan=2)

        #Создание Фрейма для кнопок разделов
        self.frame_for_navigation = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_navigation.grid(row=1, column=0, padx=0, pady=1, sticky="nws")

        #Создание фрейма для для основной рабочей области
        self.frame_for_main_job_field = customtkinter.CTkScrollableFrame(self, corner_radius=0, width=388,
                                                                         height=369, label_text=" ")
        self.frame_for_main_job_field.grid(row=1, column=0, padx=173, pady=1, sticky="we")

        self.label_for_main_job_field = customtkinter.CTkLabel(self.frame_for_main_job_field, font=("Arial Bold", 18),
                                                               text="Выберите раздел при помощи кнопок слева")
        self.label_for_main_job_field.grid(row=0, column=0, padx=60, pady=15)

        # Создание кнопки для панели инструментов
        self.button_ok = customtkinter.CTkButton(self.frame_for_tool_bar, text="Выбрать", width=80,
                                                 fg_color="green", command=self.button_select, state="disabled")
        self.button_ok.grid(row=0, column=0, padx=35, pady=10, sticky="w")

        self.button_add_organ = CustomButton1(self.frame_for_tool_bar,
                                              button_text="Вы также можете добавить учреждение",
                                              arg_row=0, arg_column=2, arg_padx=300)
        #Создание кнопок для навигации
        buttons = []
        for btn in self.result_list[0]:
            buttons.append(ButtonReferenceMod2(arg_frame=self.frame_for_navigation, text_button=btn, button_len=150,
                                              button_command=self.press_button_navigation))
        for count, button in enumerate(buttons):
            button.grid(row=count, column=0, padx=10, pady=10)

        self.add_func = AdditionalFunctional(main_frame=self.frame_for_main_job_field, object_btn=self.button_ok)

    def press_button_navigation(self, argument):
        for widget in self.frame_for_main_job_field.winfo_children():
            widget.destroy()
        self.frame_for_main_job_field.configure(label_text=argument)
        index_field = self.result_list[0].index(argument)
        self.add_func.show_result(argument_list=self.result_list[1][index_field])

    def button_select(self):
        get_value = self.add_func.return_value()
        self.button_event(get_value)
        self.destroy()


class WindowForFastSearch(ParentHelpWindow):
    """Класс окна для быстрого выбора населенного пункта или банка\почты"""
    def __init__(self,
                 name_win: str,
                 button_text: str,
                 button_text2: str,
                 show_half_data: str = "on",
                 data=None,
                 button_event=None):
        super().__init__(name_win=name_win, height_main_frame=495)

        self.show_half_data = show_half_data
        self.data = data
        self.button_event = button_event

        # Создание лейбла подписи для текстового поля
        self.label_for_text_entry = customtkinter.CTkLabel(self.frame_for_tool_bar, font=("Arial Bold", 14),
                                                           text="Поиск")
        self.label_for_text_entry.grid(row=0, column=1, padx=15, sticky="sw")

        self.button_ok = customtkinter.CTkButton(self.frame_for_tool_bar, text=button_text,
                                                 width=60, fg_color="green", command=self.button_select)
        self.button_ok.grid(row=1, column=0, padx=15, pady=(5, 5), sticky="w")

        # Создание поля для ввода текста
        self.entry_for_search = customtkinter.CTkEntry(self.frame_for_tool_bar, width=320, corner_radius=8,
                                                       placeholder_text="Введите название")
        self.entry_for_search.grid(row=1, column=1, padx=10, pady=(5, 5), columnspan=3)

        # Создание кнопки для поиска
        self.button_for_search = customtkinter.CTkButton(self.frame_for_tool_bar, text=button_text2, width=60,
                                                         fg_color="green", command=self.button_search)
        self.button_for_search.grid(row=1, column=4, padx=10, pady=(5, 5))

        self.add_func = AdditionalFunctional(main_frame=self.frame_main_job_field, object_btn=self.button_ok)

    def show_data(self):
        self.add_func.show_result(argument_list=self.data, show_half_data=self.show_half_data)

    def button_search(self):
        self.value_for_search = self.entry_for_search.get()
        self.result_search = self.add_func.inline_search(data_for_search=self.data, value=self.value_for_search)
        self.add_func.show_result(argument_list=self.result_search)

    def button_select(self):
        self.button_event(value=self.add_func.return_value())
        self.destroy()


class WindowForSearchCase(ParentHelpWindow):
    """Класс окна для поиска обращений"""
    def __init__(self,
                 name_win: str,
                 name_text_field: str,
                 button_text: str,
                 height_main_frame: int = 468,
                 button_event=None):
        super().__init__(name_win=name_win, height_main_frame=height_main_frame)

        #Создание лейбла подписи для текстового поля
        self.label_for_text_entry = customtkinter.CTkLabel(self.frame_for_tool_bar, text=name_text_field)
        self.label_for_text_entry.grid(row=0, column=1, padx=20, sticky="sw")

        #Создание поля для ввода текста
        self.entry_for_search = customtkinter.CTkEntry(self.frame_for_tool_bar, width=320, corner_radius=8)
        self.entry_for_search.grid(row=1, column=1, padx=20, pady=(0, 5), columnspan=3)

        #Создание кнопки для поиска
        self.button_for_search = customtkinter.CTkButton(self.frame_for_tool_bar, text=button_text, width=60,
                                                         fg_color="green", command=button_event, corner_radius=8)
        self.button_for_search.grid(row=1, column=4, padx=2, pady=(0, 5))

    def event_button_search(self):
        get_from_entry = self.entry_for_search.get()


class WindowForSearchTown(WindowForSearchCase):
    """Класс для поиска населенного пункта для установки дефолтного города"""
    def __init__(self,
                 func_change_default_address: any,
                 name_win: str,
                 name_text_field: str,
                 text_description: str,
                 button_text: str,
                 button_text2: str,
                 button_text3: str):
        super().__init__(name_win=name_win, name_text_field=name_text_field,
                         button_text=button_text, button_event=self.event_button_search, height_main_frame=390)

        self.func_change_default_address = func_change_default_address
        #Создание кнопки выбора
        self.button_ok = customtkinter.CTkButton(self.frame_for_tool_bar, text="Выбрать", fg_color="green", width=60,
                                                 corner_radius=8, command=self.button_select)
        self.button_ok.grid(row=1, column=0, padx=10, pady=(0, 5))

        #Создание фрейма для текстового описания
        self.frame_for_description = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_description.grid(row=4, column=0)

        self.label_description = customtkinter.CTkLabel(self.frame_for_description,
                                                     text=text_description, font=("Arial Bold", 12))
        self.label_description.grid(row=0, column=0, padx=5, pady=2, sticky="n")

        #Создание фрейма для дополнительных инструментов
        self.frame_for_additional_tool = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_additional_tool.grid(row=5, column=0, padx=0, pady=1, sticky="we")

        #Создание кнопок доп инструментов
        self.button_one = CustomButton1(self.frame_for_additional_tool, button_text=button_text2,
                                        arg_row=0, arg_column=0, button_event=self.call_window_fix_name_town)

        self.button_two = CustomButton1(self.frame_for_additional_tool, button_text=button_text3,
                                        arg_row=0, arg_column=1, button_event=self.call_window_add_new_town)

        self.add_func = AdditionalFunctional(main_frame=self.frame_main_job_field, object_btn=self.button_ok)

    def call_window_fix_name_town(self):
        window_for_fix_name_town = WindowForTranslateNameTown(name_win="Корректировка названия",
                                                                     name_one_entry="Область", name_third_entry="Район",
                                                                     name_two_entry="Новое название",
                                                                     name_fourth_entry="Название сейчас",
                                                                     text_check_box="Добавить в список 'по умолчанию'",
                                                                     button_text="Сохранить")
        window_for_fix_name_town.mainloop()

    def call_window_add_new_town(self):
        window_add_new_town = WindowAddNewTown(name_win="Добавить новый населенный пункт",
                                               name_one_entry="Область",
                                               name_third_entry="Район",
                                               name_two_entry="Название населенного пункта",
                                               text_check_box="Добавить в список 'по умолчанию'",
                                               button_text="Сохранить"
                                               )
        window_add_new_town.mainloop()

    def event_button_search(self):
        self.get_from_entry = self.entry_for_search.get()
        self.obj_distributor = SearchTownForDefaultInfo(self.get_from_entry)
        self.list_results_search = self.obj_distributor.return_found_cities()

        self.label_found = customtkinter.CTkLabel(self.frame_main_job_field, text="Результаты поиска:",
                                                  font=("Arial Bold", 16))
        self.label_found.grid(row=0, column=0, padx=5, sticky="w")

        self.list_name_button = []
        self.list_identificators = []
        for sl in self.list_results_search:
            self.list_name_button.append(sl[0] + ", " + sl[1] + ", " + sl[2])
            self.list_identificators.append([sl[3], sl[4]])
        self.add_func.show_result_2(name_btn=self.list_name_button, info_id=self.list_identificators)

    #этот метод не трогать, он не повторяется
    def button_select(self):
        var_for_logging_last_press = self.add_func.return_value()
        self.default_address = var_for_logging_last_press[0].split(", ")
        self.default_id = var_for_logging_last_press[1].copy()
        self.obj_handler_default_data = RecordDefaultDataInTable(self.default_address, self.default_id)
        self.obj_handler_default_data.record_into_table()
        self.func_change_default_address()
        self.destroy()
        get_data()

#Сюда не лезть!!!
class CreateWorkerWindow(customtkinter.CTkToplevel):
    """Класс окна для регистрации нового сотрудника"""
    def __init__(self,
                 button_event: any,
                 name_win: str,
                 name_one_entry: str,
                 name_two_entry: str,
                 button_text: str
                 ):
        super().__init__()
        self.title(name_win)
        self.resizable(False, False)

        self.button_event = button_event

        self.label_for_first_entry = customtkinter.CTkLabel(self, text=name_one_entry)
        self.label_for_first_entry.grid(row=0, column=0, padx=20, pady=(10, 30), sticky="n")

        self.first_entry = customtkinter.CTkEntry(self, width=250)
        self.first_entry.grid(row=0, column=0, padx=20, pady=(30, 10), sticky="s")

        self.label_for_second_entry = customtkinter.CTkLabel(self, text=name_two_entry)
        self.label_for_second_entry.grid(row=1, column=0, padx=20, pady=(10, 30), sticky="n")

        self.second_entry = customtkinter.CTkEntry(self, width=250)
        self.second_entry.grid(row=1, column=0, padx=20, pady=(30, 10), sticky="s")

        self.button = customtkinter.CTkButton(self, text=button_text, command=self.event_button_save, fg_color="green")
        self.button.grid(row=3, column=0, padx=10, pady=(10, 10))

    def event_button_save(self):
        self.get_name_worker = self.first_entry.get()
        self.get_id_worker = self.second_entry.get()
        self.handler_for_data_worker = RecordWorkerInDataBase(name_worker=self.get_name_worker,
                                                              id_worker=self.get_id_worker)
        self.handler_for_data_worker.record_in_data_base()
        self.button_event()
        self.destroy()


class WindowForAddNewOrgan(customtkinter.CTkToplevel):
    """Класс окна для добавления нового органа выдающего документы"""
    def __init__(self,
                 name_win: str,
                 name_one_entry: str,
                 name_two_entry: str,
                 text_check_box: str,
                 button_text: str,
                 button_event=None):
        super().__init__()
        self.title(name_win)
        self.resizable(False, False)

        self.pad_x = 20
        self.pad_y_for_lab = [(10, 35), "nw"]
        self.pad_y_for_en = [(30, 10), "s"]

        self.label_one_entry = customtkinter.CTkLabel(self, text=name_one_entry)
        self.label_one_entry.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y_for_lab[0],
                                  sticky=self.pad_y_for_lab[1])

        self.one_entry = customtkinter.CTkComboBox(self, width=250)
        self.one_entry.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y_for_en[0], sticky=self.pad_y_for_en[1])

        self.label_third_entry = customtkinter.CTkLabel(self, text=name_two_entry)
        self.label_third_entry.grid(row=3, column=0, padx=self.pad_x, pady=self.pad_y_for_lab[0],
                                    sticky=self.pad_y_for_lab[1])

        self.third_entry = customtkinter.CTkEntry(self, width=250)
        self.third_entry.grid(row=3, column=0, padx=self.pad_x, pady=self.pad_y_for_en[0], sticky=self.pad_y_for_en[1])

        self.check_var = customtkinter.IntVar(value=0)
        self.check_button = customtkinter.CTkCheckBox(self, text=text_check_box, variable=self.check_var,
                                                      onvalue=1, offvalue=0, fg_color="green", hover_color="green")
        self.check_button.grid(row=4, column=0)

        self.button_ok = customtkinter.CTkButton(self, text=button_text, command=button_event, fg_color="green")
        self.button_ok.grid(row=5, column=0, padx=self.pad_x, pady=20)



class WindowAddNewTown(WindowForAddNewOrgan):
    """Класс окна для внесения в базу данных города, которого там нет"""
    def __init__(self,
                 name_win: str,
                 name_one_entry: str,
                 name_two_entry: str,
                 name_third_entry: str,
                 text_check_box: str,
                 button_text: str,
                 button_event=None):
        super().__init__(name_win=name_win,
                         name_one_entry=name_one_entry,
                         name_two_entry=name_two_entry,
                         text_check_box=text_check_box,
                         button_text=button_text,
                         button_event=button_event
                         )
        self.title(name_win)
        self.resizable(False, False)

        self.label_two_entry = customtkinter.CTkLabel(self, text=name_third_entry)
        self.label_two_entry.grid(row=1, column=0, padx=self.pad_x, pady=self.pad_y_for_lab[0],
                                  sticky=self.pad_y_for_lab[1])

        self.two_entry = customtkinter.CTkComboBox(self, width=250)
        self.two_entry.grid(row=1, column=0, padx=self.pad_x, pady=self.pad_y_for_en[0], sticky=self.pad_y_for_en[1])


class WindowForTranslateNameTown(WindowAddNewTown):
    """Класс окна для корректировки названия населенного пункта в базе данных"""
    def __init__(self,
                 name_win: str,
                 name_one_entry: str,
                 name_two_entry: str,
                 name_third_entry: str,
                 name_fourth_entry: str,
                 text_check_box: str,
                 button_text: str,
                 button_event=None
                 ):
        super().__init__(name_win=name_win,
                         name_one_entry=name_one_entry,
                         name_two_entry=name_two_entry,
                         name_third_entry=name_third_entry,
                         text_check_box=text_check_box,
                         button_text=button_text,
                         button_event=button_event)

        self.label_fourth_entry = customtkinter.CTkLabel(self, text=name_fourth_entry)
        self.label_fourth_entry.grid(row=2, column=0, padx=self.pad_x, pady=self.pad_y_for_lab[0],
                                     sticky=self.pad_y_for_lab[1])

        self.fourth_entry = customtkinter.CTkEntry(self, width=250)
        self.fourth_entry.grid(row=2, column=0, padx=self.pad_x, pady=self.pad_y_for_en[0],
                               sticky=self.pad_y_for_en[1])


class WindowAboutThis(customtkinter.CTk):
    def __init__(self, name_win):
        super().__init__()
        self.title(name_win)
        self.width_win = 550
        self.height_win = 550
        self.geometry(f"{self.width_win}x{self.height_win}")
        self.resizable(False, False)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.scroll_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0)
        self.scroll_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nesw", rowspan=3, columnspan=3)






