import customtkinter
from worked_widgets_for_modul import SimpleEntry, SeriesNumberDocument, PersonalNumberDocument, WhoGivePassport, \
    DateReleaseDocument, DateReleaseDocument2, AddressLogging, WorkedNumberTelephone, NumberForExecuteOperation, \
    IdWorker, FieldForNumberSimCard, CheckBoxWithText, PlacePay, DoubleEntryForNumBankCard, TariffsWithCheckBox, \
    PlaceBirthday, InfoBar
from all_classes import TileWithNameModule


class ParentClassForWindowModul(customtkinter.CTk):
    def __init__(self,
                 name_window: str,
                 win_width: int = 850,
                 win_height: int = 570,
                 ):
        super().__init__(fg_color="#F5F5DC")
        self.name_window = name_window
        self.title(self.name_window)
        self.win_width = win_width
        self.win_height = win_height
        self.geometry(f"{self.win_width}x{self.win_height}")
        self.resizable(False, False)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.main_frame = customtkinter.CTkFrame(self, fg_color="#F5DEB3", corner_radius=15)
        self.main_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nesw", rowspan=3, columnspan=3)

        self.main_frame.columnconfigure((0, 1, 2), weight=1)

        self.frame_for_name_module = TileWithNameModule(self.main_frame,
                                                                    name_for_tile=self.name_window)
        self.frame_for_name_module.grid(row=0, column=0, sticky="wne", columnspan=4)


class WindowForChangeTariff(ParentClassForWindowModul):
    def __init__(self):
        super().__init__(name_window="Смена ТП на все свои", win_height=780)

        for_sticky_1 = "w"
        for_padx_1 = 50
        for_padx_2 = 0

        self.simple_entry = SimpleEntry(master=self.main_frame, name_widget="Номер договора",
                                                    width_entry=180)
        self.simple_entry.grid(row=1, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.ser_num_doc = SeriesNumberDocument(master=self.main_frame)
        self.ser_num_doc.grid(row=2, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.personal_number = PersonalNumberDocument(self.main_frame)
        self.personal_number.grid(row=3, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.who_give_this_docx = WhoGivePassport(self.main_frame)
        self.who_give_this_docx.grid(row=4, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.date_release_docx = DateReleaseDocument(self.main_frame, name_date="Дата Выдачи")
        self.date_release_docx.grid(row=5, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.date_2 = DateReleaseDocument2(self.main_frame, name_date="Дата последнего платежа")
        self.date_2.grid(row=6, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.address_logging = AddressLogging(self.main_frame)
        self.address_logging.grid(row=1, column=1, sticky=for_sticky_1, rowspan=2)

        self.worked_number = WorkedNumberTelephone(self.main_frame, name_widget="Контактный номер")
        self.worked_number.grid(row=7, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.number_for_operation = NumberForExecuteOperation(self.main_frame)
        self.number_for_operation.grid(row=8, column=0, padx=for_padx_1, sticky=for_sticky_1)

        self.entry_id_worker = IdWorker(self.main_frame)
        self.entry_id_worker.grid(row=3, column=1, sticky=for_sticky_1)

        self.entry_for_sim_number = FieldForNumberSimCard(self.main_frame)
        self.entry_for_sim_number.grid(row=4, column=1, sticky=for_sticky_1)

        self.the_owner_this_number = CheckBoxWithText(self.main_frame, name_widget="Принадлежит обратившемуся лицу"
                                                                                       "(Иначе \nзаполнить поле ниже)")
        self.the_owner_this_number.grid(row=5, column=1, sticky=for_sticky_1)

        self.list_banks = PlacePay(self.main_frame, name_widget="Оплата проходила через..")
        self.list_banks.grid(row=6, column=1, sticky=for_sticky_1)

        self.digits_from_number_bank_card = DoubleEntryForNumBankCard(self.main_frame)
        self.digits_from_number_bank_card.grid(row=7, column=1, sticky=for_sticky_1)

        self.list_with_check_box = TariffsWithCheckBox(self.main_frame)
        self.list_with_check_box.grid(row=8, column=1, sticky=for_sticky_1)

        self.place_birthday = PlaceBirthday(self.main_frame)
        self.place_birthday.grid(row=9, column=1, sticky=for_sticky_1)

        self.info_frame = InfoBar(self.main_frame)
        self.info_frame.grid(row=10, column=0, sticky="we", padx=40, pady=20, columnspan=2)
