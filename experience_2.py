def separator_name_organs(name_organ):
    list_separators = ["РОВД", "РУВД", "ГОВД"]
    list_separators_2 = ["г."]
    count = 0
    for u in list_separators:
        if u in name_organ:
            count += 1
            if list_separators_2[0] in name_organ:
                index_separator = name_organ.index(list_separators_2[0])
                list_from_name_organ = [name_organ[:index_separator-1], name_organ[index_separator-1::]]
                return list_from_name_organ
            else:
                index_separator = name_organ.index(u)
                list_from_name_organ = [name_organ[:index_separator+4], name_organ[index_separator+5::]]
                return list_from_name_organ
    if count == 0:
        if list_separators_2[0] in name_organ:
            index_separator = name_organ.index(list_separators_2[0])
            list_from_name_organ = [name_organ[:index_separator - 1], name_organ[index_separator - 1::]]
            return list_from_name_organ


