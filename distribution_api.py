from connection_with_data_base import ConnectWithDataBase
from fuzzywuzzy import fuzz
import pprint
import time
from tkinter.messagebox import showerror

class SearchTownForDefaultInfo:
    def __init__(self, name_town):
        self.name_town = name_town.title()
        self.obj_connect = ConnectWithDataBase()
        self.get_info = self.obj_connect.get_table_from_db("district_town_id")

    def return_found_cities(self):
        self.list_string_with_similar_name = []
        self.list_value_comparison = []

        for similar in self.get_info:
            comparison = fuzz.ratio(similar[1], self.name_town)
            if comparison > 70:
                self.list_value_comparison.append(comparison)
                self.list_string_with_similar_name.append(similar)


        self.list_result_search_all = []

        for string in self.list_string_with_similar_name:
            self.time_help_list = []
            self.result_search_district = self.obj_connect.search_value_by_id(name_table="field_district_id",
                                                                         identification=string[0])


            self.result_search_field = self.obj_connect.search_value_by_id(name_table="field_with_id",
                                                                      identification=self.result_search_district[0][0])

            self.time_help_list.append(string[1])
            self.time_help_list.append(self.result_search_district[0][1])
            self.time_help_list.append(self.result_search_field[0][0])
            self.time_help_list.append(string[0])
            self.time_help_list.append(self.result_search_district[0][0])
            self.list_result_search_all.append(self.time_help_list)

        self.obj_connect.close_connect()
        self.list_sort_tuple = []

        self.start_2 = time.time()
        for count in range(1, 101):
            for com, tup in zip(self.list_value_comparison, self.list_result_search_all):
                if com == count:
                    self.list_sort_tuple.append(tup)

        self.list_sort_tuple.reverse()
        return self.list_sort_tuple


class RecordDefaultDataInTable:
    def __init__(self, addresses_list, id_list):
        self.addresses_list = addresses_list
        self.id_list = id_list
        self.obj_connect = ConnectWithDataBase()

    def add_to_list(self, *args):
        raw = args
        for rio in raw:
            self.list_def_data_for_transmit_method.append(rio)

    def record_default_data_in_default_table(self):
        self.obj_connect.record_in_table_default_value(self.list_def_data_for_transmit_method)

        self.obj_connect.record_in_table_default_lists(name_table="table_default_list_district",
                                                       name_column="name_district",
                                                       DEF_list=self.default_list_district)

        self.obj_connect.record_in_table_default_lists(name_table="table_default_list_town",
                                                       name_column="name_town",
                                                       DEF_list=self.default_list_town)

        self.obj_connect.record_in_table_default_lists(name_table="table_default_list_organs",
                                                       name_column="name_organ",
                                                       DEF_list=self.finally_list_organs)

    def record_into_table(self):
        self.list_def_data_for_transmit_method = []


        self.field = self.addresses_list[2]
        self.district = self.addresses_list[1]
        self.from_table_field_district_id = self.obj_connect.search_value_by_column(name_table="field_district_id",
                                                                                    column="id_field",
                                                                                    identification=self.id_list[1])
        self.default_list_district = []

        for yi in self.from_table_field_district_id:
            self.default_list_district.append(yi[1])

        self.town = self.addresses_list[0]

        self.from_table_district_town_id = self.obj_connect.search_value_by_column(name_table="district_town_id",
                                                                                   column="id_district",
                                                                                   identification=self.id_list[0])
        self.default_list_town = []

        for yo in self.from_table_district_town_id:
            self.default_list_town.append(yo[1])

        self.default_series_letter = self.obj_connect.search_value_by_column(name_table="series_letter",
                                                                             column="id_field",
                                                                             identification=self.id_list[1])
        if self.town == "Минск":
            self.default_series = "МР"
        else:
            self.default_series = self.default_series_letter[0][2]

        self.default_letter = self.default_series_letter[0][1]
        self.id_citizen_list = self.obj_connect.get_table_from_db(name_table="id_citizen")
        self.id_citizen = self.id_citizen_list[0][0]

        self.from_table_town_organ = self.obj_connect.get_table_from_db(name_table="town_organ")


        self.list_organs_in_field = self.obj_connect.search_value_by_column(name_table="organs_in_fields_2",
                                                                       column="id_field",
                                                                       identification=self.id_list[1])
        self.finally_list_organs = []
        self.finally_default_organ = ""

        for lt in self.from_table_town_organ:
            if lt[0] == self.town:
                self.finally_list_organs.append(lt[1])

        if len(self.finally_list_organs) > 0:
            self.finally_default_organ = self.finally_list_organs[0]
            for pt in self.list_organs_in_field:
                if pt[2] not in self.finally_list_organs:
                    self.finally_list_organs.append(pt[2])
                else:
                    continue
        else:
            self.from_table_district_organ = self.obj_connect.search_value_by_column(name_table="district_organ",
                                                    column="id_district",
                                                    identification=self.id_list[0])
            self.finally_default_organ = self.from_table_district_organ[0][1]

            self.finally_list_organs.append(self.finally_default_organ)

            for y in self.list_organs_in_field:
                if y[2] not in self.finally_list_organs:
                    self.finally_list_organs.append(y[2])
                else:
                    continue

        self.add_to_list(self.field, self.district, self.town, self.default_series, self.default_letter,
                         self.id_citizen, self.finally_default_organ)

        # table_default_info(field, district, town, series, letter, pb, organ)
        # table_default_list_district(name_district)
        # table_default_list_town(name_town)
        # table_default_list_organs(name_organ)

        self.name_1 = "table_default_info"

        self.result_checkout_exist_table = self.obj_connect.checkout_exist_table(name_table=self.name_1)

        if self.result_checkout_exist_table == 1:
            print("табла есть по этому удаляем и делаем заново")
            self.obj_connect.remove_any_table(name_table="table_default_info")
            self.obj_connect.remove_any_table(name_table="table_default_list_district")
            self.obj_connect.remove_any_table(name_table="table_default_list_town")
            self.obj_connect.remove_any_table(name_table="table_default_list_organs")

            self.obj_connect.create_table_default_data()

            self.record_default_data_in_default_table()

            self.obj_connect.show_table(name_table="table_default_info")

            self.obj_connect.show_table(name_table="table_default_list_district")

            self.obj_connect.show_table(name_table="table_default_list_town")

            self.obj_connect.show_table(name_table="table_default_list_organs")

            return self.list_def_data_for_transmit_method[:3]


        else:
            self.obj_connect.create_table_default_data()

            self.record_default_data_in_default_table()

            self.obj_connect.show_table(name_table="table_default_info")

            self.obj_connect.show_table(name_table="table_default_list_district")

            self.obj_connect.show_table(name_table="table_default_list_town")

            self.obj_connect.show_table(name_table="table_default_list_organs")

            return self.list_def_data_for_transmit_method[:3]


class RecordWorkerInDataBase:
    def __init__(self, name_worker, id_worker):
        self.obj_connect = ConnectWithDataBase()
        self.name_worker = name_worker.title()
        self.id_worker = int(id_worker)

    def record_in_data_base(self):
        # workers(id_worker, init_worker, full_name_worker)
        self.list_from_name_worker = self.name_worker.split(" ")
        self.last_name_worker = self.list_from_name_worker[0]
        self.inits_worker = self.list_from_name_worker[1][0] + "." + self.list_from_name_worker[2][0] + "."
        self.full_init = self.last_name_worker + " " + self.inits_worker

        self.obj_connect.record_data_worker(name=self.name_worker, init=self.full_init, id=self.id_worker)
        self.obj_connect.close_connect()


class GetDataForWorkedWidgets:
    def __init__(self):
        self.connected = ConnectWithDataBase()

    def get_data(self,
                 second_table: str,
                 index_element: int):
        # table_default_info(field, district, town, series, letter, pb, organ)
        # series_docx(name_series)
        # letters(name_letters)
        # id_citizen(id)
        # tariff_plan(name)
        # operator_codes(code)
        # workers(id_worker, init_worker, full_name_worker)
        # table_default_list_organs(name_organ)
        from_table_default_info = self.connected.get_table_from_db(name_table="table_default_info")
        self.from_any_table = self.connected.get_table_from_db(name_table=second_table)


        default_list = []
        default_value = from_table_default_info[0][index_element]

        for i in self.from_any_table:
            default_list.append(i[0])

        return [default_list, default_value]

    def data_for_window_for_show_organs(self):
        # organs_in_fields_2(id_field, name_field, name_organ)
        list_for_return = []
        list_name_field = []

        for i in range(1, 8):
            self.from_table_organs_in_fields = self.connected.search_value_by_column(name_table="organs_in_fields_2",
                                                  column="id_field",
                                                  identification=i)
            local_list = []
            for e in self.from_table_organs_in_fields:
                local_list.append(e[2])
            list_name_field.append(self.from_table_organs_in_fields[0][1])
            list_for_return.append(local_list)

        return [list_name_field, list_for_return]

    def get_data_for_widget_place_logging(self):
        # table_default_info(field, district, town, series, letter, pb, organ)
        # field_with_id(field, id)
        # table_default_list_district(name_district)
        # table_default_list_town(name_town)
        # field_district_id(id_field, district, id)
        # district_town_id(id_district, name_town)
        from_table_default_info = self.connected.get_table_from_db(name_table="table_default_info")
        from_table_field_with_id = self.connected.get_table_from_db(name_table="field_with_id")

        list_default_value = []
        for Def in range(0, 3):
            list_default_value.append(from_table_default_info[0][Def])

        full_list_field = []
        list_district_in_field = []
        full_list_district = []
        full_list_town = []

        for dist in from_table_field_with_id:
            full_list_field.append(dist[0])
            from_table_field_district_id = self.connected.search_value_by_column(name_table="field_district_id",
                                                                                 column="id_field",
                                                                                 identification=dist[1])
            local_list_district = []
            for dist_2 in from_table_field_district_id:
                local_list_district.append(dist_2[1])
                full_list_district.append(dist_2[1])
                from_table_district_town_id = self.connected.search_value_by_column(name_table="district_town_id",
                                                                                    column="id_district",
                                                                                    identification=dist_2[2])
                local_list_town = []
                for town in from_table_district_town_id:
                    local_list_town.append(town[1])
                full_list_town.append(local_list_town)
            list_district_in_field.append(local_list_district)
        full_list_field.remove("Минск")

        id_field = full_list_field.index(list_default_value[0])
        id_district = full_list_district.index(list_default_value[1])

        return (list_default_value, [id_field, id_district], full_list_field,
                list_district_in_field, full_list_district, full_list_town)

    def return_data_for_dates(self):
        days_of_month = []

        month_list = []

        year_list = []

        for i in range(1, 32):
            if i < 10:
                days_of_month.append("0" + str(i))
                month_list.append("0" + str(i))
            elif i < 13:
                days_of_month.append(str(i))
                month_list.append(str(i))
            else:
                days_of_month.append(str(i))

        second = time.time()
        today = time.localtime(second)
        today_year = today.tm_year
        for y in range(1990, today_year+1):
            year_list.append(str(y))
        year_list.reverse()

        return [days_of_month, month_list, year_list]

    def get_data_about_workers(self):
        from_table_workers = self.connected.get_table_from_db(name_table="workers")
        # workers(id_worker, init_worker, full_name_worker)
        id_worker = []
        name_init_worker_list = []
        for w in from_table_workers:
            id_worker.append(w[0])
            local_list = [w[1], w[2]]
            name_init_worker_list.append(local_list)

        return [id_worker, name_init_worker_list]

    def get_any_list(self, table):
        self.from_table_banks = self.connected.get_table_from_db(name_table=table)

        any_list = []

        for y in self.from_table_banks:
            any_list.append(y[0])

        return any_list


    def close_data_base(self):
        self.connected.close_connect()

