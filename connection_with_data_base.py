import sqlite3
import pprint
from fuzzywuzzy import fuzz
from all_classes import show_three_value_in_cycle

# field_district(name_field, letter_region, series_passport, list_district) - table
# district_town(district, town) - table
# all_town(name_town) - table
# all_organs(name_organs) - table
# organs_field(name_field, name_organ) - table

# field_with_id(field, id)
# field_district_id(id_field, district, id)
# district_town_id(id_district, name_town)
# series_letter(id_field, letter, series)
# district_organ(id_district, name_organ)
# town_organ(name_town, name_organ)
# town_organ_not_exists(name_town, name_organ)

# organs_in_fields(id_field, name_organ)
# organs_in_fields_2(id_field, name_field, name_organ)
# banks(name_bank)
# series_docx(name_series)
# letters(name_letters)
# id_citizen(id)
# tariff_plan(name)
# operator_codes(code)
# workers(id_worker, init_worker, full_name_worker)
# table_default_info(field, district, town, series, letter, pb, organ)
# table_default_list_district(name_district)
# table_default_list_town(name_town)
# table_default_list_organs(name_organ)

class ConnectWithDataBase:
    def __init__(self):
        self.connected = sqlite3.connect("main_data_base.db")
        self.obj_cursor = self.connected.cursor()

    def get_table_from_db(self,
                          name_table: str):
        self.obj_cursor.execute(f"SELECT * FROM {name_table}")
        self.result_read_table = self.obj_cursor.fetchall()
        return self.result_read_table

    def search_value_by_id(self,
                           name_table: str,
                           identification: int):
        self.obj_cursor.execute(f"SELECT * FROM {name_table} WHERE id= {identification}")
        self.result_read_column = self.obj_cursor.fetchall()
        return self.result_read_column

    def search_value_by_column(self,
                               name_table: str,
                               column: str,
                               identification):
        self.obj_cursor.execute(f"SELECT * FROM {name_table} WHERE {column}={identification}")
        self.result_read_column = self.obj_cursor.fetchall()
        return self.result_read_column

    def checkout_exist_table(self, name_table):
        try:
            self.obj_cursor.execute(f"SELECT * FROM {name_table}")
            self.result_checkout_exist = self.obj_cursor.fetchall()
            return 1
        except sqlite3.OperationalError:
            return 0

    def create_table_default_data(self):
        # table_default_info(field, district, town, series, letter, pb, organ)
        # table_default_list_district(name_district)
        # table_default_list_town(name_town)
        # table_default_list_organs(name_organ)
        self.obj_cursor.execute("CREATE TABLE IF NOT EXISTS table_default_info(field TEXT, district TEXT, town TEXT, "
                                "series TEXT, letter TEXT, pb TEXT, organ TEXT)")

        self.obj_cursor.execute("CREATE TABLE IF NOT EXISTS table_default_list_district(name_district TEXT)")

        self.obj_cursor.execute("CREATE TABLE IF NOT EXISTS table_default_list_town(name_town TEXT)")

        self.obj_cursor.execute("CREATE TABLE IF NOT EXISTS table_default_list_organs(name_organ TEXT)")

    def record_in_table_default_value(self, DEF_list):
        self.obj_cursor.execute("INSERT INTO table_default_info(field, district, town, series, letter, pb, organ) "
                                "VALUES (?,?,?,?,?,?,?)", (DEF_list[0], DEF_list[1], DEF_list[2], DEF_list[3], DEF_list[4],
                                                   DEF_list[5], DEF_list[6]))
        self.connected.commit()

    def record_in_table_default_lists(self, name_table, name_column, DEF_list):
        for any_thing in DEF_list:
            self.obj_cursor.execute(f"INSERT INTO {name_table}({name_column}) VALUES (?)", (any_thing, ))
        self.connected.commit()

    def record_data_worker(self, name, init, id):
        self.obj_cursor.execute("INSERT INTO workers(id_worker, init_worker, full_name_worker) VALUES (?,?,?)",
                                (id, init, name))
        self.connected.commit()

    def delete_string_from_table(self, name_table, name_column, result):
        self.obj_cursor.execute(f"DELETE FROM {name_table} WHERE {name_column} = {result}")
        self.connected.commit()


    def remove_any_table(self, name_table):
        self.obj_cursor.execute(f"DROP TABLE {name_table}")
        self.connected.commit()


    def show_table(self, name_table):
        self.obj_cursor.execute(f"SELECT * FROM {name_table}")
        self.show = self.obj_cursor.fetchall()
        print(self.show)
    def close_connect(self):
        self.obj_cursor.close()
        self.connected.close()


class Operation:
    def __init__(self):
        self.conn = None
        self.obj_cursor = None

    def connected(self):
        self.conn = sqlite3.connect("main_data_base.db")
        self.obj_cursor = self.conn.cursor()

    def show_table(self, name_table):
        self.connected()
        self.obj_cursor.execute(f"SELECT * FROM {name_table}")
        self.result_read_5 = self.obj_cursor.fetchall()
        pprint.pprint(self.result_read_5)
        self.close_connection()

    def create_table(self):
        self.connected()
        self.obj_cursor.execute(f"CREATE TABLE IF NOT EXISTS table_default_info(field TEXT, district TEXT, town TEXT,"
                                f"series TEXT, letter TEXT, pb TEXT, organ TEXT)")
        self.close_connection()

    def remove_any_table(self, name_table):
        self.connected()
        self.obj_cursor.execute(f"DROP TABLE {name_table}")
        self.conn.commit()
        self.close_connection()

    def write_table_series(self):
        pass

    def update_value_in_table(self, new_name):
        self.connected()
        self.obj_cursor.execute(f"""UPDATE field_district_id SET district='{new_name}' WHERE id=?""")
        self.conn.commit()
        self.close_connection()
        print("Все четко")

    def list_all_table_in_database(self):
        self.connected()
        sql_query = """SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"""
        self.obj_cursor.execute(sql_query)
        self.reads = self.obj_cursor.fetchall()
        pprint.pprint(self.reads)
        self.close_connection()

    def rewrite_table_organs_in_fields(self):
        # organs_in_fields(id_field, name_organ)
        self.connected()
        self.obj_cursor.execute("SELECT * FROM organs_in_fields")
        self.from_table_organs_in_fields = self.obj_cursor.fetchall()
        list_name_fields = []
        list_name_organs = []

        for qt in self.from_table_organs_in_fields:
            list_name_fields.append(qt[0])
            list_name_organs.append(qt[1])

        # pprint.pprint(list_name_fields)
        # pprint.pprint(list_name_organs)

        list_name_field_from_table_field_with_id = []
        list_id_field_from_table_field_with_id = []

        self.obj_cursor.execute(f"SELECT * FROM field_with_id")
        self.from_table_field_with_id = self.obj_cursor.fetchall()

        finally_list_id_fields = []

        for io in self.from_table_field_with_id:
            list_name_field_from_table_field_with_id.append(io[0])
            list_id_field_from_table_field_with_id.append(io[1])

        for iu in list_name_fields:
            for yt, uo in zip(list_name_field_from_table_field_with_id,
                              list_id_field_from_table_field_with_id):
                if iu == yt:
                    finally_list_id_fields.append(uo)

        show_three_value_in_cycle(finally_list_id_fields,
                                  list_name_fields,
                                  list_name_organs)

        self.obj_cursor.execute("CREATE TABLE IF NOT EXISTS organs_in_fields_2(id_field INTEGER, name_field TEXT, "
                                "name_organ TEXT)")

        for one, two, three in zip(finally_list_id_fields,
                                   list_name_fields,
                                   list_name_organs):
            self.obj_cursor.execute("INSERT INTO organs_in_fields_2(id_field, name_field, name_organ) VALUES (?,?,?)",
                                    (one, two, three))
            self.conn.commit()

        self.close_connection()




    def close_connection(self):
        self.obj_cursor.close()
        self.conn.close()
        print("Все чётко")


# ert = Operation()
# ert.remove_any_table(name_table="table_default_info")
# ert.remove_any_table(name_table="table_default_list_district")
# ert.remove_any_table(name_table="table_default_list_town")
# ert.remove_any_table(name_table="table_default_list_organs")

# ert.show_table("series_docx")
# connect = sqlite3.connect("main_data_base.db")
# cursor = connect.cursor()
#
# cursor.execute("INSERT INTO town_organ(name_town, name_organ) VALUES ('Минск', 'Минское РУВД г.Минска')")
#
# connect.commit()
