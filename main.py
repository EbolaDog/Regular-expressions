import csv
import re


class Phonebook:

    def read_file(x, file_name):
        with open(file_name, encoding="utf-8") as file:
            rows = csv.reader(file, delimiter=",")
            contacts_list = list(rows)
        return contacts_list
    
    def change_number(x, y):
        x.new_contacts_list = []
        number_pattern = r"(\+7|8)\s*\(?(\d{1,4})\)?(\s|-)*(\d{1,3})(\s|-)*(\d{1,3})(\s|-)*(\d{1,3})(\s?)\(?(доб\.)?\s?(\d{1,5})(\)?)"
        result_number =r"+7(\2)-\4-\6-\8\9\10\11\12"
        for text in y:
            text_search = ','.join(text)
            format_text = re.sub(number_pattern, result_number, text_search)
            format_list = format_text.split(',')
            x.new_contacts_list.append(format_list)
        return x.new_contacts_list
    
    def change_name(x, y):
        x.data = y
        x.new_contacts_list = []
        name_pattern = r'(^[А-ё]*)(\s*)(\,?)([А-ё]*)(\s*)(\,?)([А-ё]+)?(\,?)(\,?)(\,?)'
        result_name = r'\1,\4\6\9\7\8'
        for text in y:
            text_search = ','.join(text)
            format_text = re.sub(name_pattern, result_name, text_search)
            format_list = format_text.split(',')
            x.new_contacts_list.append(format_list)
        return x.new_contacts_list
    
    def duplicate(i, x):
        i.data = x
        i.dict_ = {}
        i.new_contacts_list = []
        for x in x:
            if x[0] not in i.dict_.keys():
                i.dict_[x[0]] = x[1:]
            else:
                for j, element in enumerate(i.dict_[x[0]]):
                    if element == "" and x[1:][j] != "":
                        i.dict_[x[0]][j] = x[1:][j]

        for x in i.dict_.items():
            x[1].insert(0, x[0])
            i.new_contacts_list.append(x[1])
        return i.new_contacts_list
    
    def write_file(self, data):
        self.data = data
        with open("phonebook.csv", "w", encoding='utf-8') as file:
            data_writer = csv.writer(file, delimiter=',')
            data_writer.writerows(data)


if __name__ == '__main__':
    phonebook = Phonebook()
    i = phonebook.read_file('phonebook_raw.csv')
    i = phonebook.change_number(i)
    i = phonebook.change_name(i)
    i = phonebook.duplicate(i)
    phonebook.write_file(i)

