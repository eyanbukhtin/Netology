from pprint import pprint
# ----------
# Каталог документов хранится в следующем виде:
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
# ----------
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

# ----------
print("Введите 'p' для входа в меню поиска по документам", "\n")
user_input_people = input()
print("Введите номер документа, который Вы искали", "\n")
user_input_doc = input()
pprint(list(filter(lambda p: user_input_doc in p["number"], documents)))
