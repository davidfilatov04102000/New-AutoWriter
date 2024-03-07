import customtkinter
# from classes_help_window import WindowForFastSearchOrgan


def show_two_value_in_cycle(arg1, arg2):
    for vfr, bgt in zip(arg1, arg2):
        print(vfr, bgt, sep="   ---   ")


def show_three_value_in_cycle(arg1, arg2, arg3):
    for vfr, bgt, nhy in zip(arg1, arg2, arg3):
        print(vfr, bgt, nhy, sep="   ---   ")


class TileWithResultSearch(customtkinter.CTkButton):
    def __init__(self,
                 master: any,
                 name_town: str,
                 list_id: list,
                 button_event=None):
        super().__init__(master=master,
                         text=name_town,
                         corner_radius=8,
                         fg_color="#DCDFE1",
                         border_color="#878580",
                         border_width=1,
                         font=("Arial Bold", 20),
                         text_color="black",
                         hover_color="#5A97B6",
                         command=self.configure_fg_color)
        self.button_event = button_event
        self.name_town = name_town
        self.list_id = list_id

    def configure_fg_color(self):
        self.configure(fg_color="#5A97B6")
        self.button_event(id(self), [self.name_town, self.list_id])


class TileForWatchListWorkers(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 button_event: any,
                 full_name: str,
                 id_worker: int):
        super().__init__(master=master, fg_color="#F5D0A9", border_color="#F7BE81",
                         corner_radius=8, border_width=2)
        self.button_event = button_event
        self.full_name = full_name
        self.id_worker = id_worker

        self.text_label_1 = customtkinter.CTkLabel(self, text=f"{self.full_name}:", font=("Arial Bold", 13))
        self.text_label_1.grid(row=0, column=0, padx=10, pady=4, sticky="w")

        self.text_label_2 = customtkinter.CTkLabel(self, text=f"{self.id_worker}", font=("Arial Bold", 13))
        self.text_label_2.grid(row=0, column=1, padx=30, pady=4, sticky="w")

        self.button_delete_worker = customtkinter.CTkButton(self, text="❌", width=22, height=22,
                                                            fg_color="red", command=self.press_button_delete_worker)
        self.button_delete_worker.grid(row=0, column=2, padx=(60,2), sticky="e")

    def press_button_delete_worker(self):
        self.button_event(id(self), self.id_worker)


class TileForShowData(customtkinter.CTkButton):
    def __init__(self,
                 master: any,
                 main_data: str,
                 corner_radius: int=8,
                 fg_color: str="#DCDFE1",
                 border_color: str="#878580",
                 border_width: int=1,
                 font_size: int=20,
                 text_color: str="black",
                 hover_color: str="#5A97B6",
                 button_event=None):
        super().__init__(master=master, text=main_data, corner_radius=corner_radius,
                         fg_color=fg_color, border_color=border_color, border_width=border_width,
                         font=("Arial Bold", font_size), text_color=text_color, hover_color=hover_color,
                         command=self.configure_fg_color)
        self.button_event = button_event
        self.main_data = main_data

    def configure_fg_color(self):
        self.configure(fg_color="#5A97B6")
        self.button_event(id(self), self.main_data)


class ButtonReferenceMod(customtkinter.CTkButton):
    def __init__(self,
                 arg_frame: any,
                 text_button: str,
                 text_size: int = 15,
                 button_len: int = 200,
                 button_height: int = 28,
                 button_corner: int = 10,
                 button_color: str = "#2E9AFE",
                 button_text_color: str = "white",
                 button_command=None,
                 ):
        super().__init__(master=arg_frame, text=text_button, font=("Arial Bold", text_size),
                                              width=button_len, height=button_height, corner_radius=button_corner,
                                              command=button_command, fg_color=button_color, text_color=button_text_color)


class ButtonReferenceMod2(customtkinter.CTkButton):
    def __init__(self,
                 arg_frame: any,
                 text_button: str,
                 text_size: int = 15,
                 button_len: int = 200,
                 button_corner: int = 10,
                 button_text_color: str = "white",
                 button_command=None,
                 ):
        super().__init__(master=arg_frame, text=text_button, font=("Arial Bold", text_size),
                         width=button_len, corner_radius=button_corner,
                         command=self.event_press, text_color=button_text_color)
        self.button_command = button_command
        self.text_button = text_button

    def event_press(self):
        self.button_command(self.text_button)


class CustomButton1:
    def __init__(self,
                 arg_frame: any,
                 button_text: str,
                 arg_row: int,
                 arg_column: int,
                 arg_padx: int = 17,
                 arg_pady: int = 10,
                 button_event=None
                 ):
        self.custom_button = customtkinter.CTkButton(arg_frame, text=button_text, font=("Arial Bold", 12),
                                                     width=150, corner_radius=11, fg_color="white", text_color="black",
                                                     border_color="black", hover_color="green", command=button_event)
        self.custom_button.grid(row=arg_row, column=arg_column, padx=arg_padx, pady=arg_pady)


class TileWithNameModule(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_for_tile: str
                 ):
        super().__init__(master=master, fg_color="#F7BE81")
        adit_pad_x = 300
        max_len = 20
        if len(name_for_tile) > max_len:
            how_many = len(name_for_tile) - max_len
            adit_pad_x = adit_pad_x - (how_many * 5)
        self.text_label = customtkinter.CTkLabel(self, text=name_for_tile, text_color="#585858",
                                                 font=("Arial Black", 16))
        self.text_label.grid(row=0, column=0, padx=adit_pad_x, pady=(5,5))






