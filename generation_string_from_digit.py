class IntToString:
    def __init__(self, value):
        self.first_list_string_for_byn = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

        self.second_list_string_for_byn = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят",
                                           "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

        self.third_list_string_for_byn = ["одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
                                          "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]

        self.fourth_list_string_for_byn = ["сто", "двести", "триста", "четыреста", "пятьсот",
                                           "шестьсот", "семьсот", "восемьсот", "девятьсот"]

        self.first_list_string_for_small_byn = ["одна", "две", "три", "четыре", "пять",
                                                "шесть", "семь", "восемь", "девять"]

        self.byn_dict = {"Рубль": ["1"], "Рубля": ["2", "3", "4"], "Рублей": ["5", "6", "7", "8", "9", "0",
                                                                              "11", "12", "13", "14", "15",
                                                                              "16", "17", "18", "19"]}

        self.small_byn_dict = {"Копейка": ["1"], "Копейки": ["2", "3", "4"], "Копеек": ["5", "6", "7", "8", "9", "0",
                                                                                        "11", "12", "13", "14", "15",
                                                                                        "16", "17", "18", "19"]}

        self.finally_result = ""

        self.str_value = str(value)

        if self.str_value.isdigit() is not True:
            two_half = []
            for y in self.str_value:
                if y in [",", "."]:
                    two_half = self.str_value.split(y)
                    break
            first_half = int(two_half[0])
            second_half = int(two_half[1])

            ready_string_for_byn_without_prefix = self.distributor(digit=first_half)
            result_prefix_for_byn = self.prefix_for_byn(digit=two_half[0])
            ready_string_for_small_byn_without_prefix = self.distributor(digit=second_half)
            result_prefix_for_coin = self.prefix_for_coin(digit=two_half[1])
            first_half_finally_result = ready_string_for_byn_without_prefix + " " + result_prefix_for_byn
            second_half_finally_result = ready_string_for_small_byn_without_prefix + " " +  result_prefix_for_coin
            self.finally_result = first_half_finally_result + " " + second_half_finally_result
        else:
            self.int_value = int(value)
            ready_string_without_prefix = self.distributor(digit=self.int_value)
            result_prefix_for_byn = self.prefix_for_coin(digit=self.str_value)
            self.finally_result = ready_string_without_prefix + " " + result_prefix_for_byn

    def distributor(self,
                    digit: int):
        str_value = str(digit)
        if len(str_value) < 3:
            return self.two_digit_number(digit=digit)
        else:
            return self.three_digit_number(digit=digit)

    def two_digit_number(self,
                         digit: int):
        str_value = str(digit)
        if len(str_value) == 1:
            return self.first_list_string_for_byn[digit-1]
        elif len(str_value) == 2:
            first_half, second_half = int(str_value[0]), int(str_value[1])
            if second_half == 0:
                return self.second_list_string_for_byn[first_half-1]
            elif first_half == 0:
                return self.first_list_string_for_byn[first_half-1]
            elif first_half == 1:
                return self.third_list_string_for_byn[second_half-1]
            else:
                for_first_half = self.second_list_string_for_byn[first_half-1]
                for_second_half = self.first_list_string_for_byn[second_half-1]
                return for_first_half + " " + for_second_half

    def three_digit_number(self,
                           digit: int):
        str_value = str(digit)
        first_half = int(str_value[0])
        second_half = int(str_value[1])
        third_half = int(str_value[2])
        if second_half and third_half == 0:
            return self.fourth_list_string_for_byn[first_half-1]
        else:
            for_first_half = self.fourth_list_string_for_byn[first_half-1]
            for_second_half = self.two_digit_number(digit % 100)
            return for_first_half + " " + for_second_half

    def prefix_for_byn(self,
                       digit: str):
        key_list = []
        count = 0
        for i in self.byn_dict:
            key_list.append(i)
        for x in key_list:
            if digit[-2:] in self.byn_dict[x]:
                count += 1
                return x
        if count == 0:
            for y in key_list:
                if digit[-1] in self.byn_dict[y]:
                    return y

    def prefix_for_coin(self,
                        digit: str):
        key_list = []
        for i in self.small_byn_dict:
            key_list.append(i)
        for x in key_list:
            if digit in self.small_byn_dict[x]:
                return x
            elif digit[-1] in self.small_byn_dict[x]:
                return x

    def return_value(self):
        return self.finally_result

