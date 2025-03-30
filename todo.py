HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи.
exit - выход"""

tasks = {

}

run = True

while run:
    command = input("Введите команду: ")

    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        date = input("Введите дату выполнения задачи: ")
        task = input("Введите название задачи: ")
        if date in tasks:
            #Дата есть в словаре
            #Добавляем задачу в список
            tasks[date].append(task)
        else:
            #Даты нет в словаре
            #Создаем запись с ключем date
            tasks[date] = [task]
        print("Задача", task, "добавлена на дату", date)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        print("До свиданья!")
        break
