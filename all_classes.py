import customtkinter
# from classes_help_window import WindowForFastSearchOrgan


def show_two_value_in_cycle(arg1, arg2):
    for vfr, bgt in zip(arg1, arg2):
        print(vfr, bgt, sep="   ---   ")


def show_three_value_in_cycle(arg1, arg2, arg3):
    for vfr, bgt, nhy in zip(arg1, arg2, arg3):
        print(vfr, bgt, nhy, sep="   ---   ")


class TileWithResultSearch(customtkinter.CTkFrame):
    def __init__(self,
                 master: any,
                 name_town: str,
                 ):
        super().__init__(master=master,
                         border_width=1,
                         border_color="gray",
                         width=400)
        self.checkbox_variable = customtkinter.IntVar(value=0)
        self.checkbox = customtkinter.CTkCheckBox(self, text=name_town,
                                                  variable=self.checkbox_variable,
                                                  onvalue=1, offvalue=0,
                                                  font=("Arial Bold", 16))
        self.checkbox.grid(row=0, column=0, padx=5, pady=(3,3))


class ButtonReferenceMod:
    def __init__(self,
                 arg_frame: any,
                 text_button: str,
                 string: int = 0,
                 text_size: int = 15,
                 button_len: int = 200,
                 button_radius: int = 10,
                 button_column: int = 0,
                 button_corner: int = 10,
                 button_text_color: str = "white",
                 grid_pad_x: int = 10,
                 grid_pad_y: int = 15,
                 button_command=None,
                 ):
        self.button = customtkinter.CTkButton(arg_frame, text=text_button, font=("Arial Bold", text_size),
                                              width=button_len, corner_radius=button_corner,
                                              command=button_command, text_color=button_text_color)
        self.button.grid(row=string, column=button_column, padx=grid_pad_x, pady=grid_pad_y)


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
        self.text_label = customtkinter.CTkLabel(self, text=name_for_tile, text_color="#585858",
                                                 font=("Arial Black", 16))
        self.text_label.grid(row=0, column=0, padx=300, pady=(5,5))






