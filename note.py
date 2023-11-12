from datetime import datetime as dt
from time import time
import codecs



def save_all_notes(notes) :
    with open('notes.csv', 'w', encoding='utf-8') as file:
            file.writelines(notes)

def save_last_note(note) :
    with open('notes.csv','a', encoding='utf-8') as file:
            file.writelines(note)

def read_notes() :
    with open('notes.csv', encoding='utf-8') as file:
            return file.readlines()

def read_names() :
    lst_names = []
    notes = read_notes()
    for note in notes :
        lst_note = note.split(sep=';')
        lst_names.append(lst_note[1])
    return lst_names

def get_notes() :
    lst_notes = []
    notes = read_notes()
    for note in notes :
        lst_note = note.split(sep=';')
        lst_notes.append(lst_note)
    return lst_notes

def get_note(name) :
    lst_notes = get_notes()
    for note in lst_notes :
        if note[1] == name :
            return note
    print("нет такой заметки")
    return -1

    


       
def new_note(name, text) :
    time = dt.now()
    notes = get_notes()
    if len(notes) == 0 :
        id = 1
    else :
        id = int((notes[len(notes)-1])[0]) + 1
    return '{};{};{};{};\n'.format(id, name, time, text)



def change_note(name, text) :
    time = dt.now()
    notes = get_notes()
    for i in range(0, len(notes)) :
        if (notes[i])[1] == name :
            ch_note = notes[i]
            notes[i] = [ch_note[0], ch_note[1], time, text] 
            return notes
    print("Нет такой заметки")
    return -1

def convert_notes(notes) :
    for i in range(0, len(notes)) :
        note = notes[i]
        notes[i] = '{};{};{};{};\n'.format(note[0], note[1], note[2], note[3])
    save_all_notes(notes)

def delete_note(name) :
    notes = get_notes()
    for i in range(0, len(notes)) :
        if (notes[i])[1]==name :
            notes.remove(notes[i])
            print('заметка удалена')
            convert_notes(notes)
            return notes
    print('Нет такой заметки')
    return -1
    
        
        
    
    
    
    


