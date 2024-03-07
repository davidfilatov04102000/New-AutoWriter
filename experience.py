import customtkinter
from all_classes import TileWithResultSearch, CustomButton1, ButtonReferenceMod, TileForShowData, ButtonReferenceMod2
from distribution_api import SearchTownForDefaultInfo, RecordDefaultDataInTable, RecordWorkerInDataBase, \
    GetDataForWorkedWidgets
import time
from fuzzywuzzy import fuzz


class AdditionalFunctional:
    def __init__(self, main_frame, object_btn):
        self.main_frame = main_frame
        self.object_btn = object_btn
        self.var_for_logging_last_press = ()

    def hover_click_on_button(self, id_button, name_button):
        if len(self.var_for_logging_last_press) == 0:
            self.var_for_logging_last_press = (id_button, name_button)
            self.object_btn.configure(state="normal")

        elif id_button == self.var_for_logging_last_press[0]:
            for widget in self.main_frame.winfo_children():
                if id(widget) == id_button:
                    widget.configure(fg_color="#DCDFE1")
                    self.object_btn.configure(state="disabled")
                    self.var_for_logging_last_press = ()
                    break
        else:
            for widget in self.main_frame.winfo_children():
                if id(widget) == self.var_for_logging_last_press[0]:
                    widget.configure(fg_color="#DCDFE1")
                    self.var_for_logging_last_press = (id_button, name_button)
                    break

    def inline_search(self, data_for_search, value):
        result_list = []
        for q in data_for_search:
            comparison = fuzz.ratio(q, value)
            if comparison > 40:
                result_list.append(q)
        return result_list

    def clean_work_field(self):
        count = 0
        for widget_1 in self.main_frame.winfo_children():
            count += 1
        if count > 0:
            for widget in self.main_frame.winfo_children():
                widget.destroy()
        else:
            pass

    def show_result(self, argument_list,
                    show_half_data: str = "off"):
        if show_half_data == "on":
            size_small_list = len(argument_list) // 2
            list_for_iteration = argument_list[:size_small_list].copy()
        else:
            list_for_iteration = argument_list.copy()
            self.clean_work_field()
        tiles = []
        for wid in list_for_iteration:
            tiles.append(TileForShowData(master=self.main_frame, main_data=wid,
                                         button_event=self.hover_click_on_button))
        for count, tile in enumerate(tiles):
            tile.grid(row=count, column=0, padx=30, pady=9, sticky="w")

    def show_result_2(self, name_btn, info_id):
        tiles = []
        for name_obj_tile, id_for_tile in zip(name_btn, info_id):
            tiles.append(TileWithResultSearch(master=self.main_frame, name_town=name_obj_tile, list_id=id_for_tile,
                                              button_event=self.hover_click_on_button))
        for count, tile, in enumerate(tiles):
            tile.grid(row=count+1, column=0, padx=5, pady=1, sticky="we", columnspan=3)
    def return_value(self):
        return self.var_for_logging_last_press[1]


