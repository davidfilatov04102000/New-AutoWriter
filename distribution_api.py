from connection_with_data_base import ConnectWithDataBase
from fuzzywuzzy import fuzz
import pprint

class DistributionDefaultInfo:
    def __init__(self, name_town):
        self.name_town = name_town.title()
        self.obj_connect = ConnectWithDataBase()
        self.get_info = self.obj_connect.get_table_from_db("district_town_id")

    def return_found_cities(self):
        self.list_string_with_similar_name = []
        self.list_value_comparison = []

        for similar in self.get_info:
            comparison = fuzz.ratio(similar[1], self.name_town)
            if comparison > 65:
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
            self.list_result_search_all.append(self.time_help_list)

        self.obj_connect.close_connect()
        self.list_sort_tuple = []

        for count in range(1, 101):
            for com, tup in zip(self.list_value_comparison, self.list_result_search_all):
                if com == count:
                    self.list_sort_tuple.append(tup)

        self.list_sort_tuple.reverse()
        return self.list_sort_tuple


# raw = DistributionDefaultInfo(name_town="кожан-городок")
# qwe = raw.return_found_cities()
# pprint.pprint(qwe)

