import view
import note
import codecs

def start() :
    while True :
        command = view.command()
        print(command)
        if command == 'add' :
            name = view.name_note()
            text = view.text_note()
            note.save_last_note(note.new_note(name, text))
            print('заметка сохранена')
        elif command == 'stop' :
            break
        elif command == 'names' :
            print(note.read_names())
        elif command == 'print' :
            name = view.name_note()
            lst_note = note.get_note(name)
            if lst_note!=-1 :
                print('-----------------\nимя заметки: {}\nвремя заметки: {}\nтекст заметки: {}\n-----------------------'.format(lst_note[1], lst_note[2], lst_note[3])) 
        elif command == 'change' : 
            name = view.name_note()
            text = view.text_note()
            notes = note.change_note(name, text)
            if notes != -1 :
                note.convert_notes(notes)
                print('заметка изменена')
        elif command == 'delete' :
            name = view.name_note()
            notes = note.delete_note(name)
            
            





     
    
        

    
