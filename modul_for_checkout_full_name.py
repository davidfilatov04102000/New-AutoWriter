import pprint
from all_classes import show_two_value_in_cycle
from connection_with_data_base import ConnectWithDataBase

# mans_names(id, name_first_case, name_second_case)
# mans_father_names(id, name_first_case, name_second_case)
# girls_names(id, name_first_case, name_second_case)
# girls_father_names(id, name_first_case, name_second_case)


def checkout_full_name(full_name):
    full_name.lower()
    from info_from_data_base import full_list_all_names_in_first_case, full_list_all_fathers_names_in_first_case, \
        full_list_all_names_in_second_case, full_list_all_fathers_names_in_second_case
    all_names_in_first_case = full_list_all_names_in_first_case.copy()
    all_fathers_names_in_first_case = full_list_all_fathers_names_in_first_case.copy()
    all_names_in_second_case = full_list_all_names_in_second_case.copy()
    all_fathers_names_in_second_case = full_list_all_fathers_names_in_second_case.copy()
    all_names = all_names_in_first_case + all_names_in_second_case
    all_fathers_names = all_fathers_names_in_first_case + all_fathers_names_in_second_case
    # pprint.pprint(all_names)
    # pprint.pprint(all_fathers_names)
    list_full_name = full_name.split(" ")
    # print(list_full_name)
    if list_full_name[1] not in all_names:
        return False
    elif list_full_name[2] not in all_fathers_names:
        return False
    else:
        return True


def generator_another_case(full_name):
    # from info_from_data_base import get_data
    #
    # get_data()
    from info_from_data_base import full_list_all_names_in_first_case, full_list_all_fathers_names_in_first_case, \
        full_list_all_names_in_second_case, full_list_all_fathers_names_in_second_case
    dict_all_names = dict(zip(full_list_all_names_in_first_case, full_list_all_names_in_second_case))
    dict_all_fathers_names = dict(zip(full_list_all_fathers_names_in_first_case, full_list_all_fathers_names_in_second_case))
    list_full_name = full_name.lower().split(" ")
    # pprint.pprint(dict_all_names)
    # pprint.pprint(dict_all_fathers_names)

    result_name = dict_all_names[list_full_name[1]].title()
    result_father_name = dict_all_fathers_names[list_full_name[2]].title()

    return f"{list_full_name[0].title()} {result_name} {result_father_name}"










