import customtkinter
from tkinter import messagebox
from worked_widgets_for_modul import SimpleEntry, SeriesNumberDocument, PersonalNumberDocument, WhoGivePassport, \
    DateReleaseDocument, DateReleaseDocument2, AddressLogging, WorkedNumberTelephone, NumberForExecuteOperation, \
    IdWorker, FieldForNumberSimCard, CheckBoxWithText, PlacePay, DoubleEntryForNumBankCard, TariffsWithCheckBox, \
    PlaceBirthday, InfoBar, Tariffs
from all_classes import TileWithNameModule, ButtonReferenceMod
import time
import pprint
from generation_word_document import generation_document_for_change_tariff, generation_document_including_second_sim_card, \
    generation_document_in_case_error_pay, generation_document_for_change_owner


class ParentClassForWindowModul(customtkinter.CTk):
    def __init__(self,
                 name_window: str,
                 win_width: int,
                 win_height: int,
                 module_code: int=0,
                 pad_x_green_button: int=180,
                 pad_x_red_button: int=0
                 ):
        super().__init__(fg_color="#F5F5DC")
        self.module_code = module_code
        self.column_1 = 1
        self.for_padx_1 = 50
        self.for_sticky_1 = "w"
        self.for_sticky_2 = "w"
        self.for_padx_2 = 0

        self.name_window = name_window
        self.title(self.name_window)
        self.win_width = win_width
        self.win_height = win_height
        self.geometry(f"{self.win_width}x{self.win_height}")
        self.resizable(False, False)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.value_for_checkout_full_name = "on"

        self.main_frame = customtkinter.CTkFrame(self, fg_color="#F5DEB3", corner_radius=15)
        self.main_frame.grid(row=0, column=0, padx=15, pady=(10, 5), sticky="nesw", rowspan=3, columnspan=3)

        self.main_frame.columnconfigure((0, 1), weight=1)

        self.frame_for_name_module = TileWithNameModule(self.main_frame,
                                                                    name_for_tile=self.name_window)
        self.frame_for_name_module.grid(row=0, column=0, sticky="wne", columnspan=3)

        self.checkout_full_name = CheckBoxWithText(master=self.main_frame,
                                                   name_widget="Проверка орфографии \nимен и отчеств", value_on_off="on")
        self.checkout_full_name.grid(row=12, column=0, padx=self.for_padx_1, pady=10, sticky=self.for_sticky_1)

        self.button_execute = ButtonReferenceMod(arg_frame=self.main_frame, button_color="green", text_button="Готово",
                                                 button_len=130, button_command=self.validation_values)
        self.button_execute.grid(row=12, column=0, padx=pad_x_green_button, pady=10, sticky="w", columnspan=2)

        self.button_clean = ButtonReferenceMod(arg_frame=self.main_frame, button_color="red", text_button="Очистить",
                                               button_len=130, button_command=self.clean_entry)
        self.button_clean.grid(row=12, column=self.column_1, padx=pad_x_red_button, pady=10, sticky="w")

        self.status_operation_bar = InfoBar(master=self.main_frame)
        self.status_operation_bar.grid(row=13, column=0, padx=50, pady=(3,10), sticky="w", columnspan=2)

        self.hard_checkout = CheckBoxWithText(master=self.main_frame,
                                                   name_widget="Строгий режим",
                                                   value_on_off="on")
        self.hard_checkout.grid(row=14, column=0, padx=50, pady=2, sticky="w")

    def validation_name(self):
        list_value_checkout = []
        for widget in self.main_frame.winfo_children():
            try:
                result = widget.validation_full_name()
                list_value_checkout.append(result)
                # yield result
            except AttributeError:
                continue
        return list_value_checkout

    def validation_part_2(self):
        list_value_checkout = []
        for widget_2 in self.main_frame.winfo_children():
            try:
                result = widget_2.validation_values()
                list_value_checkout.append(result)
            except AttributeError:
                continue
        return list_value_checkout

    def checkout_list_on_False_value(self, List):
        if False in List:
            mess = messagebox.showerror(title="Ошибка", message="В заполненой форме присутствуют ошибки")
        else:
            self.get_all_value()

    def validation_values(self):
        if self.checkout_full_name.get_values() == "on" and self.hard_checkout.get_values() == "on":
            validation_part_1 = self.validation_name()
            validation_part_2 = self.validation_part_2()
            list_value_checkout = validation_part_1 + validation_part_2
            self.checkout_list_on_False_value(list_value_checkout)
        elif self.checkout_full_name.get_values() == "off" and self.hard_checkout.get_values() == "on":
            validation_part_2 = self.validation_part_2()
            self.checkout_list_on_False_value(validation_part_2)
        elif self.checkout_full_name.get_values() == "on" and self.hard_checkout.get_values() == "off":
            validation_part_1 = self.validation_name()
            self.checkout_list_on_False_value(validation_part_1)
        else:
            self.get_all_value()

    def get_all_value(self):
        list_all_value = []
        for widget in self.main_frame.winfo_children():
            try:
                list_all_value.append(widget.get_values())
            except AttributeError:
                continue
        if self.module_code == 1:
            generation_document_for_change_tariff(list_all_value)
        elif self.module_code == 2:
            generation_document_including_second_sim_card(list_all_value)
        elif self.module_code == 3:
            generation_document_in_case_error_pay(list_all_value)
        elif self.module_code == 4:
            generation_document_for_change_owner(list_all_value)
        elif self.module_code == 5:
            pprint.pprint(list_all_value)

    def clean_entry(self):
        for widget in self.main_frame.winfo_children():
            try:
                widget.clean_en()
            except AttributeError:
                continue


class ParentWindowForTwoModuls(ParentClassForWindowModul):
    def __init__(self,
                 name_window: str,
                 win_width: int = 850,
                 win_height: int = 500,
                 module_code: int = 0
                 ):
        super().__init__(name_window=name_window, win_width=win_width, win_height=win_height, pad_x_green_button=220,
                         module_code=module_code)

        self.number_contract = SimpleEntry(master=self.main_frame, name_widget="Номер договора",
                                                    width_entry=180)
        self.number_contract.grid(row=1, column=0, padx=self.for_padx_1, pady=10, sticky=self.for_sticky_1)

        self.full_name_client = SimpleEntry(master=self.main_frame, name_widget="ФИО", width_entry=220,
                                            checkout_name=self.value_for_checkout_full_name)
        self.full_name_client.grid(row=2, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1)

        self.series_number_date_release_passport = SeriesNumberDocument(master=self.main_frame)
        self.series_number_date_release_passport.grid(row=3, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1)

        self.personal_identification_number = PersonalNumberDocument(master=self.main_frame)
        self.personal_identification_number.grid(row=4, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1)

        self.who_give_passport = WhoGivePassport(master=self.main_frame)
        self.who_give_passport.grid(row=5, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1, columnspan=2)

        self.address_logging = AddressLogging(master=self.main_frame)
        self.address_logging.grid(row=1, column=self.column_1, padx=self.for_padx_2, pady=10, sticky=self.for_sticky_2, rowspan=2)

        self.worked_number_for_connection = WorkedNumberTelephone(master=self.main_frame,
                                                                  name_widget="Контактный номер")
        self.worked_number_for_connection.grid(row=3, column=self.column_1, padx=self.for_padx_2, sticky=self.for_sticky_2)

        self.number_for_operation = NumberForExecuteOperation(master=self.main_frame)
        self.number_for_operation.grid(row=4, column=self.column_1, padx=self.for_padx_2, sticky=self.for_sticky_2)


class WindowForChangeTariff(ParentWindowForTwoModuls):
    def __init__(self):
        start = time.time()
        super().__init__(name_window="Смена ТП на все свои", win_height=500, module_code=1)

        self.entry_for_id_worker = IdWorker(master=self.main_frame)
        self.entry_for_id_worker.grid(row=5, column=self.column_1, padx=self.for_padx_2, sticky=self.for_sticky_2)


class WindowForAddSecondSimCard(ParentWindowForTwoModuls):
    def __init__(self,
                 name_window: str="Подключение twin-Карты",
                 win_height: int=500):
        start = time.time()
        super().__init__(name_window=name_window, win_height=win_height, module_code=2)

        self.entry_for_sim_number = FieldForNumberSimCard(master=self.main_frame)
        self.entry_for_sim_number.grid(row=5, column=self.column_1, padx=self.for_padx_2, sticky=self.for_sticky_2)

        self.id_worker = IdWorker(master=self.main_frame)
        self.id_worker.grid(row=5, column=self.column_1, padx=100, sticky="e")


class ParentWindowForTwoModuls2(ParentClassForWindowModul):
    def __init__(self,
                 name_window: str,
                 win_width: int = 850,
                 win_height: int = 500,
                 pad_x_green_button: int = 180,
                 pad_x_red_button: int = 0,
                 module_code: int = 0
                 ):
        super().__init__(name_window=name_window, win_width=win_width, win_height=win_height,
                         pad_x_green_button=pad_x_green_button, pad_x_red_button=pad_x_red_button, module_code=module_code)

        self.full_name_client = SimpleEntry(master=self.main_frame, name_widget="ФИО", width_entry=220,
                                            checkout_name=self.value_for_checkout_full_name)
        self.full_name_client.grid(row=1, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1)

        self.series_number_date_release_passport = SeriesNumberDocument(master=self.main_frame)
        self.series_number_date_release_passport.grid(row=2, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1)

        self.personal_identification_number  = PersonalNumberDocument(master=self.main_frame)
        self.personal_identification_number.grid(row=3, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1)

        self.who_give_passport = WhoGivePassport(master=self.main_frame)
        self.who_give_passport.grid(row=4, column=0, padx=self.for_padx_1, sticky=self.for_sticky_1, columnspan=2)


class WindowForHandlerErrorPay(ParentWindowForTwoModuls2):
    def __init__(self):
        super().__init__(name_window="Ошибочная оплата", win_height=585, pad_x_green_button=220, pad_x_red_button=50,
                         module_code=3)

        self.for_padx_301 = 50
        self.for_sticky_301 = "w"
        self.for_padx_302 = 80
        self.for_sticky_302 = "w"

        self.number_for_enrollment_money = WorkedNumberTelephone(master=self.main_frame,
                                                            name_widget="Номер для зачисления")
        self.number_for_enrollment_money.grid(row=5, column=0, padx=self.for_padx_301, sticky=self.for_sticky_301)

        self.checkout_owner_number = CheckBoxWithText(master=self.main_frame, name_widget="Принадлежит обратившемуся лицу"
                                                                                       "(Иначе \nзаполнить поле ниже)")
        self.checkout_owner_number.grid(row=6, column=0, padx=self.for_padx_301, sticky=self.for_sticky_301)

        self.who_owner_number = SimpleEntry(master=self.main_frame, name_widget="Кому принадлежит номер",
                                            width_entry=220, checkout_name=self.value_for_checkout_full_name)
        self.who_owner_number.grid(row=7, column=0, padx=self.for_padx_301, sticky=self.for_sticky_301)

        self.entry_for_amount = SimpleEntry(master=self.main_frame, name_widget="Сумма", width_entry=120)
        self.entry_for_amount.grid(row=1, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)

        self.where_now_money = WorkedNumberTelephone(master=self.main_frame, name_widget="Зачисленная на номер")
        self.where_now_money.grid(row=2, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)

        self.place_pay = PlacePay(master=self.main_frame, name_widget="Оплата проходила через..")
        self.place_pay.grid(row=3, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)

        self.number_pay_document = SimpleEntry(master=self.main_frame, name_widget="Номер чека", width_entry=150)
        self.number_pay_document.grid(row=4, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)

        self.id_worker = IdWorker(master=self.main_frame)
        self.id_worker.grid(row=5, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)

        self.date_pay = DateReleaseDocument2(master=self.main_frame, name_date="Дата оплаты")
        self.date_pay.grid(row=6, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)

        self.number_bank_card = DoubleEntryForNumBankCard(master=self.main_frame)
        self.number_bank_card.grid(row=7, column=self.column_1, padx=self.for_padx_302, sticky=self.for_sticky_302)


class WindowForChangeOwner(ParentClassForWindowModul):
    def __init__(self):
        super().__init__(name_window="Смена владельца", win_width=850, win_height=775, pad_x_green_button=220,
                         module_code=4)

        self.for_padx_601 = 50
        self.for_sticky_601 = "w"
        self.for_padx_602 = 0
        self.for_sticky_602 = "w"

        self.number_contract = SimpleEntry(master=self.main_frame, name_widget="Номер договора", width_entry=180)
        self.number_contract.grid(row=1, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.number_for_change_owner = WorkedNumberTelephone(master=self.main_frame,
                                                             name_widget="Номер для смены владельца")
        self.number_for_change_owner.grid(row=2, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.full_name_old_client = SimpleEntry(master=self.main_frame, name_widget="ФИО передающей стороны",
                                                width_entry=220, checkout_name=self.value_for_checkout_full_name)
        self.full_name_old_client.grid(row=3, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.series_number_date_release_passport = SeriesNumberDocument(master=self.main_frame)
        self.series_number_date_release_passport.grid(row=4, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.personal_number_passport = PersonalNumberDocument(master=self.main_frame)
        self.personal_number_passport.grid(row=5, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.who_give_passport = WhoGivePassport(master=self.main_frame)
        self.who_give_passport.grid(row=6, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.address_logging = AddressLogging(master=self.main_frame)
        self.address_logging.grid(row=7, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601, rowspan=2)

        self.full_name_new_client = SimpleEntry(master=self.main_frame, name_widget="ФИО Принимающей стороны",
                                                width_entry=220, checkout_name="on")
        self.full_name_new_client.grid(row=9, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.number_sim_card = FieldForNumberSimCard(master=self.main_frame)
        self.number_sim_card.grid(row=10, column=0, padx=self.for_padx_601, sticky=self.for_sticky_601)

        self.date_birthday = DateReleaseDocument(master=self.main_frame, name_date="Дата рождения")
        self.date_birthday.grid(row=10, column=0, padx=120, sticky="e")

        self.tariff_with_checkout = TariffsWithCheckBox(master=self.main_frame)
        self.tariff_with_checkout.grid(row=1, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602)

        self.place_birthday = PlaceBirthday(master=self.main_frame)
        self.place_birthday.grid(row=2, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602)

        self.series_number_date_release_passport_new_client = SeriesNumberDocument(master=self.main_frame)
        self.series_number_date_release_passport_new_client.grid(row=3, column=1, padx=self.for_padx_602,
                                                                 sticky=self.for_sticky_602)

        self.who_give_passport_new_client = WhoGivePassport(master=self.main_frame)
        self.who_give_passport_new_client.grid(row=4, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602)

        self.personal_number_passport_new_client = PersonalNumberDocument(master=self.main_frame)
        self.personal_number_passport_new_client.grid(row=5, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602)

        self.address_logging = AddressLogging(master=self.main_frame)
        self.address_logging.grid(row=6, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602, rowspan=2)

        self.checkout_address_logging = CheckBoxWithText(master=self.main_frame, name_widget="Адреса сторон совпадают",
                                                         non_change_value="off")
        self.checkout_address_logging.grid(row=8, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602)

        self.id_worker = IdWorker(master=self.main_frame)
        self.id_worker.grid(row=9, column=1, padx=self.for_padx_602, sticky=self.for_sticky_602)


class WindowForRefundNumberLastOwner(ParentWindowForTwoModuls2):
    def __init__(self):
        super().__init__(name_window="Предоставление номера прежднему владельцу", win_height=580,
                         pad_x_green_button=220, module_code=5)

        self.for_padx_501 = 50
        self.for_sticky_501 = "w"
        self.for_padx_502 = 0
        self.for_sticky_502 = "w"

        self.place_birthday = PlaceBirthday(master=self.main_frame)
        self.place_birthday.grid(row=5, column=0, padx=self.for_padx_501, sticky=self.for_sticky_501)

        self.date_birthday = DateReleaseDocument(master=self.main_frame, name_date="Дата рождения")
        self.date_birthday.grid(row=6, column=0, padx=self.for_padx_501, sticky=self.for_sticky_501)

        self.address_logging = AddressLogging(master=self.main_frame)
        self.address_logging.grid(row=1, column=self.column_1, padx=self.for_padx_502, sticky=self.for_sticky_502,
                                  rowspan=2)

        self.number_sim_card = FieldForNumberSimCard(master=self.main_frame)
        self.number_sim_card.grid(row=3, column=self.column_1, padx=self.for_padx_502, sticky=self.for_sticky_502)

        self.tariff = Tariffs(master=self.main_frame)
        self.tariff.grid(row=4, column=self.column_1, padx=self.for_padx_502, sticky=self.for_sticky_502)

        self.number_for_refund = NumberForExecuteOperation(master=self.main_frame)
        self.number_for_refund.grid(row=5, column=self.column_1, padx=self.for_padx_502, sticky=self.for_sticky_502)

        self.amount_pay = SimpleEntry(master=self.main_frame, name_widget="Сумма", width_entry=120)
        self.amount_pay.grid(row=6, column=self.column_1, padx=self.for_padx_502, sticky=self.for_sticky_502)

        self.id_worker = IdWorker(master=self.main_frame)
        self.id_worker.grid(row=6, column=self.column_1, padx=90, sticky="e")

