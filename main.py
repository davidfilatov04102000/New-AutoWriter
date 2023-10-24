import customtkinter
from all_classes import ButtonReferenceMod
from classes_help_window import WindowForFastSearch, WindowForSearchCase, WindowForSearchTown, CreateWorkerWindow, \
    WindowForAddNewOrgan, WindowAddNewTown, WindowForTranslateNameTown, WindowAboutThis, WindowForFastSearchOrgan


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color="#F5F5DC")
        """Базовые свойства голого окна"""

        self.title("Compose")
        self.width_main_win = 800
        self.height_main_win = 450
        self.geometry(f"{self.width_main_win}x{self.height_main_win}")
        self.resizable(False, False)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((1, 2, 3), weight=1)

        """ФРЕЙМЫ"""

        #Созадаем фрейм под кнопки модулей
        self.frame_for_button_module = customtkinter.CTkFrame(self, fg_color="#F5DEB3", corner_radius=0)
        self.frame_for_button_module.grid(row=0, column=0, pady=(0, 0), sticky="nsew", rowspan=4)
        # self.grid_rowconfigure(4, weight=1)

        """Создание фрейма для основной рабочей области"""

        self.main_job_frame = customtkinter.CTkFrame(self, corner_radius=8, fg_color="#F5DEB3")
        self.main_job_frame.grid(row=0, column=1, padx=10, pady=(5, 10), sticky="wnes", rowspan=4, columnspan=3)

        # Создание фрейма для обозревания или установки населенного пункта
        self.frame_for_job_with_town = customtkinter.CTkFrame(self.main_job_frame, fg_color="#F7BE81",
                                                              corner_radius=8)
        self.frame_for_job_with_town.grid(row=0, column=1, padx=10, pady=10, sticky="wne")

        # Создание фрейма для работы со списком сотрудников
        self.frame_for_job_with_workers = customtkinter.CTkScrollableFrame(self.main_job_frame, fg_color="#F5D0A9",
                                                                           corner_radius=8, border_color="#F7BE81",
                                                                           border_width=2, height=40,
                                                                           label_text="Список работников")
        self.frame_for_job_with_workers.grid(row=1, column=1, padx=10, pady=0, sticky="wne")

        #Создание фрейма для функций: поиск обращений и как этим пользоваться
        self.frame_for_additional_function = customtkinter.CTkFrame(self.main_job_frame, fg_color="#F7BE81",
                                                                    corner_radius=8, height=50)
        self.frame_for_additional_function.grid(row=3, column=1, padx=10, pady=14, sticky="wne")

        """ЛЕЙБЛЫ"""

        """Создаем лейбл на фрейме для кнопок модулей"""
        self.h1_label = customtkinter.CTkLabel(self.frame_for_button_module, text="Все Модули", text_color="#585858",
                                               font=("Arial black", 20))
        self.h1_label.grid(row=0, column=0, padx=15, pady=10)

        #Создаем Лейбл для фрейма для работы с конфигурацией населенного пункта
        self.label_where_we = customtkinter.CTkLabel(self.frame_for_job_with_town, text="Где мы?:",
                                                     text_color="#585858", font=("Arial black", 16))
        self.label_where_we.grid(row=0, column=0, padx=30, pady=18)

        #Создание Лейбла который будет подсвечивать название нашего НП
        self.label_my_town = customtkinter.CTkLabel(self.frame_for_job_with_town,
                                                    text="Калинковичи",
                                                    text_color="#1C1C1C", font=("Arial Bold", 18))
        self.label_my_town.grid(row=0, column=1, padx=20, pady=(8, 15), sticky="nw")

        self.label_about_my_town = customtkinter.CTkLabel(self.frame_for_job_with_town,
                                                    text="Гомельская обл, Калинковичский Р-н",
                                                    text_color="#1C1C1C", font=("Arial Bold", 10))
        self.label_about_my_town.grid(row=0, column=1, padx=10, pady=(15, 8), sticky="sw")

        #КНОПКИ

        # Создаем кнопки ссылки на модули
        btn1 = ButtonReferenceMod(self.frame_for_button_module, "Заявление Все свои", 1)
        btn2 = ButtonReferenceMod(self.frame_for_button_module, "Подключение Твин-Карты", 2)
        btn3 = ButtonReferenceMod(self.frame_for_button_module, "Ошибочная оплата", 3)
        btn4 = ButtonReferenceMod(self.frame_for_button_module, "Смена владельца", 4)
        btn5 = ButtonReferenceMod(self.frame_for_button_module, "Возврат номера", 5)

        #Создание кнопки для изменения конфигурации населенного пункта
        self.button_change_town = customtkinter.CTkButton(self.frame_for_job_with_town, text="Изменить",
                                                          font=("Arial Bold", 13), width=70,
                                                          command=self.call_window_change_default_town)
        self.button_change_town.grid(row=0, column=2, padx=(25, 95), pady=15, sticky="w")

        #Создание кнопки добавления сотрудника на фрейм для работы со списком сотрудников
        self.button_add_worker = customtkinter.CTkButton(self.frame_for_job_with_workers, text="➕",
                                                         font=("Arial bold", 12), width=25, fg_color="green",
                                                         command=self.call_window_add_new_worker)
        self.button_add_worker.grid(row=0, column=0, padx=2, pady=2, sticky="nw")

        #Cоздание кнопок на фрейм с доп функциями
        self.button_search_case = ButtonReferenceMod(arg_frame=self.frame_for_additional_function,
                                                     text_button="Поиск по обращениям", string=0, button_column=0,
                                                     grid_pad_x=25, grid_pad_y=8, button_corner=8,
                                                     button_command=self.call_window_search_case)
        self.button_how_this_use = ButtonReferenceMod(arg_frame=self.frame_for_additional_function,
                                                      text_button="Как этим пользоваться?", string=0, button_column=1,
                                                      grid_pad_x=25, grid_pad_y=8, button_corner=8,
                                                      button_command=self.call_window_about_this_program)


    def call_window_change_default_town(self):
        window_change_town = WindowForSearchTown(name_win="Поиск населенного пункта",
                                                 name_text_field="Название населенного пункта",
                                                 text_description="Внимание, некоторые Н.П. могут иметь название на "
                                                                  "беларуском языке, будьте внимательны",
                                                 button_text="Поиск", button_text2="Вы можете корректировать название",
                                                 button_text3="Вы можете добавить населенный пункт")
        window_change_town.mainloop()

    def call_window_add_new_worker(self):
        window_add_new_worker = CreateWorkerWindow(name_win="Регистрация работника",
                                                   name_one_entry="ФИО работника",
                                                   name_two_entry="id работника",
                                                   button_text="Сохранить")
        window_add_new_worker.mainloop()

    def call_window_search_case(self):
        window_search_case = WindowForSearchCase(name_win="Поиск обращений",
                                                 name_text_field="Фамилия абонента",
                                                 button_text="Поиск")
        window_search_case.mainloop()

    def call_window_about_this_program(self):
        window_about_this_program = WindowAboutThis(name_win="О программе")
        window_about_this_program.mainloop()







aplication = App()
aplication.mainloop()