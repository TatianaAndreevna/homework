documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "nme": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def display_list():
    input_number = input('Введите номер документа:')
    result = 'Документ не найден'
    for number in documents:
        if number["number"] == input_number:
            result = number["name"]
            break
    print(result)


# display_list()


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def document_list():
    for document in documents:
        result = document["type"], document["number"], document["name"]
        print(result[0], result[1], result[2])


# document_list()


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf_directories():
    input_document = input('Введите номер документа:')
    result = 'Документ не найден'
    for number, shelf in directories.items():
        if input_document in shelf:
            result = number
            break
    print(result)


# shelf_directories()


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def document_add():
    input_type = input('Введите тип документа:')
    input_number = input('Введите номер документа:')
    input_name = input('Введите имя:')
    input_shelf = input('Введите номер полки:')
    for shelf in directories:
        if int(input_shelf) <= 3:
            directories[input_shelf].append(input_number)
            print(directories)
            documents.append({'type': input_type, 'number': input_number, 'name': input_name})
            print(documents)
            break
        else:
            print('Такой полки нет')
            return shelf


# document_add()



def name(documents):
    for document in documents:
        try:
            print(document['name'])
        except KeyError:
            print('В документе номер {} ошибка в "name"'.format(document['number']))


while True:
    user_input = input('\n Команды: p, l, s, a, k, help.\n Для выхода введите: Выход\n Введите команду:')
    if user_input == 'p':
        display_list()
    elif user_input == 'l':
        document_list()
    elif user_input == 's':
        shelf_directories()
    elif user_input == 'a':
        document_add()
    elif user_input == 'k':
        name(documents)
    elif user_input == 'Выход':
        break
    elif user_input == 'help':
        print(
            '\n p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n'
        'l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n'
        's – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n'
        'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    else:
        print("Ошибка")