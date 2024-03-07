from distribution_api import GetDataForWorkedWidgets
import pprint

from_table_series_docx = []
from_table_letters = []
from_table_id_citizen = []
from_table_default_list_organs = []
list_data_for_dates = []
data_for_widget_address_logging = []
from_table_workers = []
from_table_banks = []
from_table_tariff_plan = []
data_for_window_for_show_organs = []
full_list_all_names_in_first_case = []
full_list_all_fathers_names_in_first_case = []
full_list_all_names_in_second_case = []
full_list_all_fathers_names_in_second_case = []



def get_data():
    global from_table_series_docx, from_table_letters, from_table_id_citizen
    global from_table_default_list_organs, list_data_for_dates, data_for_widget_address_logging
    global from_table_workers, from_table_banks, from_table_tariff_plan, data_for_window_for_show_organs
    global full_list_all_names_in_first_case, full_list_all_fathers_names_in_first_case
    global full_list_all_names_in_second_case, full_list_all_fathers_names_in_second_case
    object_for_get_data = GetDataForWorkedWidgets()
    from_table_series_docx = object_for_get_data.get_data(second_table="series_docx", index_element=3).copy()
    from_table_letters = object_for_get_data.get_data(second_table="letters", index_element=4).copy()
    from_table_id_citizen = object_for_get_data.get_data(second_table="id_citizen", index_element=5).copy()
    from_table_default_list_organs = object_for_get_data.get_data(second_table="table_default_list_organs",
                                                                  index_element=6).copy()
    list_data_for_dates = object_for_get_data.return_data_for_dates().copy()
    data_for_widget_address_logging = object_for_get_data.get_data_for_widget_place_logging().copy()
    from_table_workers = object_for_get_data.get_data_about_workers().copy()
    from_table_banks = object_for_get_data.get_any_list(table="banks").copy()
    from_table_tariff_plan = object_for_get_data.get_any_list(table="tariff_plan").copy()
    data_for_window_for_show_organs = object_for_get_data.data_for_window_for_show_organs().copy()
    full_list_all_names_in_first_case = object_for_get_data.get_data_from_table_names()[0].copy()
    full_list_all_fathers_names_in_first_case = object_for_get_data.get_data_from_table_names()[1].copy()
    full_list_all_names_in_second_case = object_for_get_data.get_data_from_table_names()[2].copy()
    full_list_all_fathers_names_in_second_case = object_for_get_data.get_data_from_table_names()[3].copy()
    object_for_get_data.close_data_base()


