def read_csv(filename:str):
    data = []
    fields = ["Заголовок","ID", "Дата", "Текст"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(';')))
            data.append(record)
    return data

def write_txt(filename:str, data:list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ';'
            f_out.write(f'{s[:-1]}\n')

def print_result(data:list):
    print('-'*10)
    for elem in data:
        for key in elem:
            print(f"{key} : {elem[key]}")
        print('-'*10)

def get_search_heading():
    return input('Введите заголовок заметки, которую хотите удалить:')

def find_by_id(data:list, id:str):
    result = []
    for elem in data:
        if elem['ID'] == id:
            result.append(elem)
    return result

def find_by_date(data:list, date: str):
    result = []
    for elem in data:
        if elem['Дата'] == date:
            result.append(elem)
    return result

def get_new_note():
    fields = ["Заголовок","ID","Дата","Текст"]
    record = dict(zip(fields, input('Введите заголовок, номер заметки, дату заполнения, текст через(;):').strip().split(',')))
    return record
    
def add_note(data:list, note:dict):
    return data.append(note)

def write_csv(filename:str, data:list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ';'
            f_out.write(f'{s[:-1]}\n')

def delete_by_heading(data:list, heading: str):
    for elem in data:
        if elem['Заголовок'] == heading:
            data.remove(elem)
    return data

def show_menu():
    print("\nВыберите нужное действие: \n"
          "1.Отобразить все заметки\n"
          "2.Найти заметку по ID номеру\n"
          "3.Найти заметку по дате \n"
          "4.Добавить заметку\n"
          "5.Удалить заметку\n"
          "6.Сохранить заметку в текстовом формате\n"
          "7.Закончить работу\n")
    choice = int(input())
    return choice

def work_with_notebook():
    choice = show_menu()
    notebook = read_csv('Notes.csv')
    
    while(choice!=7):
        if choice == 1:
            print_result(notebook)
        elif choice == 2:
            id = input('введите пробел, ID заметки и Enter:')                 
            print_result(find_by_id(notebook, id))           
        elif choice == 3:
            date = input('введите пробел, дату написания заметки и Enter:')
            print_result(find_by_date(notebook, date))
        elif choice == 4:
            new_note = get_new_note()
            add_note(notebook, new_note)
            write_csv('Notes.csv', notebook)
        elif choice == 5:
            del_heading = get_search_heading()
            delete_by_heading(notebook, del_heading)
            write_csv('Notes.csv', notebook)
        elif choice == 6:
            write_txt('Notes.txt', notebook)

        choice = show_menu()


work_with_notebook()

