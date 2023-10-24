import sqlite3
import pprint
from fuzzywuzzy import fuzz
import all_classes

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
# banks(name_bank)
# series_docx(name_series)
# letters(name_letters)
# id_citizen(id)
# tariff_plan(name)
# operator_codes(code)
# workers(id_worker, init_worker, full_name_worker)


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

    def close_connection(self):
        self.obj_cursor.close()
        self.conn.close()
        print("Все чётко")





