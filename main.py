import customtkinter
from all_classes import ButtonReferenceMod, TileForWatchListWorkers
from classes_help_window import WindowForFastSearch, WindowForSearchCase, WindowForSearchTown, CreateWorkerWindow, \
    WindowForAddNewOrgan, WindowAddNewTown, WindowForTranslateNameTown, WindowAboutThis, WindowForFastSearchOrgan
from classes_window_modul import WindowForChangeTariff, WindowForAddSecondSimCard, WindowForRefundNumberLastOwner, \
    WindowForHandlerErrorPay, WindowForRefundNumberLastOwner, WindowForChangeOwner
from connection_with_data_base import ConnectWithDataBase
from tkinter.messagebox import askyesno
import time
from info_from_data_base import get_data


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

        from_table_default_info = self.take_data_about_my_address()
        self.label_my_town = customtkinter.CTkLabel(self.frame_for_job_with_town,
                                                    text=from_table_default_info[0],
                                                    text_color="#1C1C1C", font=("Arial Bold", 19))
        self.label_my_town.grid(row=0, column=1, padx=20, pady=(8, 15), sticky="nw")

        self.label_about_my_town = customtkinter.CTkLabel(self.frame_for_job_with_town,
                                                    text=from_table_default_info[1],
                                                    text_color="#1C1C1C", font=("Arial Bold", 11))
        self.label_about_my_town.grid(row=0, column=1, padx=10, pady=(15, 8), sticky="sw")

        #КНОПКИ

        # Создаем кнопки ссылки на модули
        btn1 = ButtonReferenceMod(self.frame_for_button_module, "Заявление Все свои", button_corner=8, button_len=200,
                                  button_command=self.open_modul_change_tariff)
        btn1.grid(row=1, column=0, padx=10, pady=15)
        btn2 = ButtonReferenceMod(self.frame_for_button_module, "Подключение Твин-Карты", button_corner=8, button_len=200,
                                  button_command=self.open_modul_for_include_second_sim_card)
        btn2.grid(row=2, column=0, padx=10, pady=15)
        btn3 = ButtonReferenceMod(self.frame_for_button_module, "Ошибочная оплата", button_corner=8, button_len=200,
                                  button_command=self.open_modul_for_handler_error_pay)
        btn3.grid(row=3, column=0, padx=10, pady=15)
        btn4 = ButtonReferenceMod(self.frame_for_button_module, "Смена владельца", button_corner=8, button_len=200,
                                  button_command=self.open_modul_for_change_owner)
        btn4.grid(row=4, column=0, padx=10, pady=15)
        btn5 = ButtonReferenceMod(self.frame_for_button_module, "Возврат номера", button_corner=8, button_len=200,
                                  button_command=self.open_modul_for_refund_number_last_Owner)
        btn5.grid(row=5, column=0, padx=10, pady=15)

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
                                                     text_button="Поиск по обращениям",
                                                     button_corner=8,
                                                     button_command=self.call_window_search_case)
        self.button_search_case.grid(row=0, column=0, padx=20, pady=10)
        self.button_how_this_use = ButtonReferenceMod(arg_frame=self.frame_for_additional_function,
                                                      text_button="Как этим пользоваться?",
                                                     button_corner=8,
                                                      button_command=self.call_window_about_this_program)
        self.button_how_this_use.grid(row=0, column=1, padx=20, pady=10)

        self.create_tile_with_info_worker()

        get_data()

        # from info_from_data_base import from_table_series_docx, from_table_letters, from_table_id_citizen, \
        #     from_table_default_list_organs, list_data_for_dates, data_for_widget_address_logging, from_table_workers, \
        #     from_table_banks, from_table_tariff_plan

    def call_window_change_default_town(self):
        window_change_town = WindowForSearchTown(func_change_default_address=self.change_default_address,
                                                 name_win="Поиск населенного пункта",
                                                 name_text_field="Название населенного пункта",
                                                 text_description="Внимание, некоторые Н.П. могут иметь название на "
                                                                  "беларуском языке, будьте внимательны",
                                                 button_text="Поиск", button_text2="Вы можете корректировать название",
                                                 button_text3="Вы можете добавить населенный пункт")

    def call_window_add_new_worker(self):
        window_add_new_worker = CreateWorkerWindow(self.create_tile_with_info_worker,
                                                   name_win="Регистрация работника",
                                                   name_one_entry="ФИО работника",
                                                   name_two_entry="id работника",
                                                   button_text="Сохранить")


    def call_window_search_case(self):
        window_search_case = WindowForSearchCase(name_win="Поиск обращений",
                                                 name_text_field="Фамилия абонента",
                                                 button_text="Поиск")


    def call_window_about_this_program(self):
        window_about_this_program = WindowAboutThis(name_win="О программе")


    def open_modul_change_tariff(self):
        obj_pop_up_window = WindowForChangeTariff()
        obj_pop_up_window.mainloop()

    def open_modul_for_include_second_sim_card(self):
        obj_pop_up_window = WindowForAddSecondSimCard()
        obj_pop_up_window.mainloop()

    def open_modul_for_handler_error_pay(self):
        obj_pop_up_window = WindowForHandlerErrorPay()
        obj_pop_up_window.mainloop()

    def open_modul_for_refund_number_last_Owner(self):
        obj_pop_up_window = WindowForRefundNumberLastOwner()
        obj_pop_up_window.mainloop()

    def open_modul_for_change_owner(self):
        obj_pop_up_window = WindowForChangeOwner()
        obj_pop_up_window.mainloop()

    def take_data_about_my_address(self):
        connect = ConnectWithDataBase()
        from_table_default_info = connect.get_table_from_db(name_table="table_default_info")
        connect.close_connect()
        text_my_town = from_table_default_info[0][2]
        text_about_my_town = from_table_default_info[0][1] + ", " + from_table_default_info[0][0]
        return [text_my_town, text_about_my_town]


    def change_default_address(self):
        connect = ConnectWithDataBase()
        self.from_table_deafault_info = connect.get_table_from_db(name_table="table_default_info")
        connect.close_connect()
        self.label_my_town.configure(text=self.from_table_deafault_info[0][2])
        self.text_about_my_town = self.from_table_deafault_info[0][1] + ", " + self.from_table_deafault_info[0][0]
        self.label_about_my_town.configure(text=self.text_about_my_town)

    def create_tile_with_info_worker(self):
        connect = ConnectWithDataBase()
        self.from_table_workers = connect.get_table_from_db(name_table="workers")
        i = 0
        for ip in self.from_table_workers:
            i += 1
            self.tile = TileForWatchListWorkers(master=self.frame_for_job_with_workers,
                                                button_event=self.delete_tile_with_info_worker,
                                                full_name=ip[2],
                                                id_worker=ip[0])
            self.tile.grid(row=i, column=0, padx=5, pady=4, sticky="w")

    def add_new_tile_with_info_worker(self):
        connect = ConnectWithDataBase()
        self.from_table_workers = connect.get_table_from_db(name_table="workers")[-1]
        connect.close_connect()
        print(self.from_table_workers)
        i = 0
        for ip in self.from_table_workers:
            i += 1
            self.tile = TileForWatchListWorkers(master=self.frame_for_job_with_workers,
                                                button_event=self.delete_tile_with_info_worker,
                                                full_name=ip[2],
                                                id_worker=ip[0])
            self.tile.grid(row=i, column=0, padx=5, pady=4, sticky="w")

    def delete_tile_with_info_worker(self, id_object, id_worker):
        pop_up_window = askyesno(title="Удаление сотрудника",
                                 message="Вы действительно хотите удалить этого сотрудника?")
        if pop_up_window is True:
            for widget in self.frame_for_job_with_workers.winfo_children():
                if id(widget) == id_object:
                    widget.destroy()
            connect = ConnectWithDataBase()
            connect.delete_string_from_table(name_table="workers", name_column="id_worker", result=id_worker)
        else:
            pass

aplication = App()
aplication.mainloop()