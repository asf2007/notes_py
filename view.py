def command() :
    return input('команды меню:\n add - новая заметка\ndelete - удалить заметку\nchange - редактировать заметку\nnames - список имен заметок\nprint - вывести заметку на экран\nstop - выйти из программы\nвведите одну из команд: ')

def text_note(text) :
    print(text)

def name_note() :
    return input('введите имя заметки: ')

def text_note() :
    return input('Введите текст заметки: ')