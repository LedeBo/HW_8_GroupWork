import view, model 
def start():
    view.greetings()

while True:
        start()
        view.menu
        command = input("Что делаем? Введите номер команды: ")
        if command ==  1:
            name = input("Имя контакта: ")
            last_name = input("Фамилия контакта: ")
            phone_number = input("Телефон: ")
            model.add_contact(name, phone_number) #добавление контакта
        elif command == 2:
            data = input("Удалить этот контакт: ")
            model.del_contact(data) # удаление контакта
        elif command == 3:
            data = input("Кого ищем? Введите данные: ")
            model.find(data) #поиск контакта
        elif command == 4:
            data = input("Редактировать контакт: ")
            model.edit(data) #изменить контакт
        elif command == 5:
            view.bye()
            break
        else:
            model.error() #ошибка ввода
