import customtkinter
import all_classes
from all_classes import CustomButton1, ButtonReferenceMod
from distribution_api import DistributionDefaultInfo
import time


class ParentHelpWindow(customtkinter.CTk):
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

        #Создание фрейма вверху окна для поля ввода и кнопки поиска
        self.frame_for_tool_bar = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_tool_bar.grid(row=0, column=0, padx=0, pady=0, sticky="we")

        #Создание фрейма для вывода информации
        self.frame_main_job_field = customtkinter.CTkScrollableFrame(self, corner_radius=0, height=height_main_frame)
        self.frame_main_job_field.grid(row=1, column=0, padx=0, pady=2, sticky="we")


class WindowForFastSearch(ParentHelpWindow):
    """Класс окна для быстрого выбора населенного пункта или банка\почты"""
    def __init__(self,
                 name_win: str,
                 button_text: str,
                 button_event=None):
        super().__init__(name_win=name_win, height_main_frame=495)
        self.button_ok = customtkinter.CTkButton(self.frame_for_tool_bar, text=button_text,
                                                 width=80, fg_color="green", command=button_event)
        self.button_ok.grid(row=0, column=0, padx=25, pady=10, sticky="w")


# ert1 = WindowForFastSearch("Быстрый поиск", "выбрать")
# ert1.mainloop()


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
        self.label_for_text_entry.grid(row=0, column=0, padx=80, pady=(10, 35), sticky="nw")

        #Создание поля для ввода текста
        self.entry_for_search = customtkinter.CTkEntry(self.frame_for_tool_bar, width=350, corner_radius=8)
        self.entry_for_search.grid(row=0, column=0, padx=80, pady=(35, 10), sticky="s")

        #Создание кнопки для поиска
        self.button_for_search = customtkinter.CTkButton(self.frame_for_tool_bar, text=button_text, width=60,
                                                         fg_color="green", command=button_event, corner_radius=8)
        self.button_for_search.grid(row=0, column=0, padx=17, pady=(35, 10), sticky="se")

    def event_button_search(self):
        get_from_entry = self.entry_for_search.get()



# ert2 = WindowForSearchCase("Поиск обращений", "Введите фамилию абонента", "поиск")
# ert2.mainloop()


class WindowForSearchTown(WindowForSearchCase):
    """Класс для поиска населенного пункта для установки дефолтного города"""
    def __init__(self,
                 name_win: str,
                 name_text_field: str,
                 text_description: str,
                 button_text: str,
                 button_text2: str,
                 button_text3: str):
        super().__init__(name_win=name_win, name_text_field=name_text_field,
                         button_text=button_text, button_event=self.event_button_search, height_main_frame=390)
        #Создание фрейма для текстового описания
        self.frame_for_description = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_description.grid(row=2, column=0)

        self.label_description = customtkinter.CTkLabel(self.frame_for_description,
                                                     text=text_description, font=("Arial Bold", 12))
        self.label_description.grid(row=0, column=0, padx=5, pady=2, sticky="n")

        #Создание фрейма для дополнительных инструментов
        self.frame_for_additional_tool = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_additional_tool.grid(row=3, column=0, padx=0, pady=1, sticky="we")

        #Создание кнопок доп инструментов
        self.button_one = CustomButton1(self.frame_for_additional_tool, button_text=button_text2,
                                        arg_row=0, arg_column=0, button_event=self.call_window_fix_name_town)

        self.button_two = CustomButton1(self.frame_for_additional_tool, button_text=button_text3,
                                        arg_row=0, arg_column=1, button_event=self.call_window_add_new_town)

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
        start = time.time()
        self.get_from_entry = self.entry_for_search.get()
        self.obj_distributor = DistributionDefaultInfo(self.get_from_entry)
        self.list_results_search = self.obj_distributor.return_found_cities()

        iu = -1
        for sl in self.list_results_search:
            iu += 1
            self.full_text = sl[0] + ", " + sl[1] + ", " + sl[2]
            self.tile = all_classes.TileWithResultSearch(self.frame_main_job_field, self.full_text)
            self.tile.grid(row=iu, column=0, padx=10, pady=5, sticky="we", columnspan=2)
        finish = time.time() - start
        print(finish)



# ert3 = WindowForSearchTown("Поиск населенного пункта", "Название населенного пункта",
#                            "Внимание! Некоторые Н.П. могут иметь название на беларусском, будьте внимательны",
#                            "Поиск", button_text2="Вы можете корректировать название",
#                            button_text3="Вы можете добавить населенный пункт")
# ert3.mainloop()


class CreateWorkerWindow(customtkinter.CTk):
    """Класс окна для регистрации нового сотрудника"""
    def __init__(self,
                 name_win: str,
                 name_one_entry: str,
                 name_two_entry: str,
                 button_text: str,
                 button_event=None
                 ):
        super().__init__()
        self.title(name_win)
        self.resizable(False, False)

        self.label_for_first_entry = customtkinter.CTkLabel(self, text=name_one_entry)
        self.label_for_first_entry.grid(row=0, column=0, padx=20, pady=(10, 30), sticky="n")

        self.first_entry = customtkinter.CTkEntry(self, width=250)
        self.first_entry.grid(row=0, column=0, padx=20, pady=(30, 10), sticky="s")

        self.label_for_second_entry = customtkinter.CTkLabel(self, text=name_two_entry)
        self.label_for_second_entry.grid(row=1, column=0, padx=20, pady=(10, 30), sticky="n")

        self.second_entry = customtkinter.CTkEntry(self, width=250)
        self.second_entry.grid(row=1, column=0, padx=20, pady=(30, 10), sticky="s")

        self.button = customtkinter.CTkButton(self, text=button_text, command=button_event, fg_color="green")
        self.button.grid(row=3, column=0, padx=10, pady=(10, 10))


# ert4 = CreateWorkerWindow("Регистрация работника", "ФИО Работника", "id Работника", "готово")
# ert4.mainloop()

class WindowForAddNewOrgan(customtkinter.CTk):
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


# ert5 = WindowForAddNewOrgan("Добавить новое учреждение", "Область",
#                             "Полное название органа", "Добавить в дефолтный список", "Готово")
# ert5.mainloop()


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


# ert6 = WindowAddNewTown("Новый населенный пункт", "Область", "Город", "Район", "Добавить в дефолтный список", "Готово")
# ert6.mainloop()


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


# ert7 = WindowForTranslateNameTown(name_win="Корректировка названия", name_one_entry="область",
#                                   name_third_entry="Район", name_two_entry="Новое название",
#                                   name_fourth_entry="Уже существующее название",
#                                   text_check_box="Добавить в дефолтный список",
#                                   button_text="Готово")
# ert7.mainloop()


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


# ert8 = WindowAboutThis(name_win="Как этим пользоваться?")
# ert8.mainloop()


class WindowForFastSearchOrgan(customtkinter.CTk):
    """Класс для быстрого поска органов"""
    def __init__(self, name_win):
        super().__init__()
        self.title(name_win)
        self.width_win = 700
        self.height_win = 450
        self.geometry(f"{self.width_win}x{self.height_win}")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)


        #Создание фрейма для кнопки выбрать сверху
        self.frame_for_tool_bar = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_tool_bar.grid(row=0, column=0, padx=0, pady=0, sticky="wne")

        #Создание Фрейма для кнопок разделов
        self.frame_for_navigation = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_for_navigation.grid(row=1, column=0, padx=0, pady=1, sticky="nws")

        #Создание фрейма для для основной рабочей области
        self.frame_for_main_job_field = customtkinter.CTkFrame(self, corner_radius=0, width=700, height=396)
        self.frame_for_main_job_field.grid(row=1, column=0, padx=223, pady=1)

        # Создание кнопки для панели инструментов
        self.button_ok = customtkinter.CTkButton(self.frame_for_tool_bar, text="Выбрать", width=80,
                                                 fg_color="green")
        self.button_ok.grid(row=0, column=0, padx=35, pady=10, sticky="w")

        self.button_add_organ = CustomButton1(self.frame_for_tool_bar,
                                              button_text="Вы также можете добавить учреждение",
                                              arg_row=0, arg_column=2, arg_padx=300)

        #Создание кнопок для навигации
        self.refer_on_field1 = ButtonReferenceMod(self.frame_for_navigation, text_button="Все", string=0,
                                                  grid_pad_y=10)
        self.refer_on_field1 = ButtonReferenceMod(self.frame_for_navigation, text_button="Минск", string=1,
                                                  grid_pad_y=10)
        self.refer_on_field2 = ButtonReferenceMod(self.frame_for_navigation, text_button="Брестская обл", string=2,
                                                  grid_pad_y=10)
        self.refer_on_field3 = ButtonReferenceMod(self.frame_for_navigation, text_button="Витебская обл", string=3,
                                                  grid_pad_y=10)
        self.refer_on_field4 = ButtonReferenceMod(self.frame_for_navigation, text_button="Гомельская обл", string=4,
                                                  grid_pad_y=10)
        self.refer_on_field5 = ButtonReferenceMod(self.frame_for_navigation, text_button="Гродненская обл", string=5,
                                                  grid_pad_y=10)
        self.refer_on_field6 = ButtonReferenceMod(self.frame_for_navigation, text_button="Минская обл", string=6,
                                                  grid_pad_y=10)
        self.refer_on_field7 = ButtonReferenceMod(self.frame_for_navigation, text_button="Могилевская обл", string=7,
                                                  grid_pad_y=10)



# ert9 = WindowForFastSearchOrgan(name_win="Все органы")
# ert9.mainloop()
