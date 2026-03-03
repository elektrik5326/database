import sqlite3

def create():
    con = sqlite3.connect('base.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS main (
              title text,
              txt text,
              vievs integer)''')
    print('\n')
    print('БД успешно создана')
    print('\n')

    con.commit()
    con.close()

    
def info():
    con = sqlite3.connect('base.db')
    c = con.cursor()
    c.execute('SELECT rowid,* FROM main')
    print('Все записаные данные:')
    print('\n')
    print(c.fetchall())
    print('\n')
    print('title - заголовок (text текст),txt - текст (text текст),vievs - просмотры (integer целое число)')
    con.commit()
    con.close()



def addelement():
    con = sqlite3.connect('base.db')
    c = con.cursor()
    print('\n')
    t = input('Введите заголовок:')
    m = input('Введите текст:')
    while True:
            try:
                views = int(input('Введите число просмотров: '))
                break
            except:
                print('Ошибка! Введите целое число.')
    c.execute('INSERT INTO main (title, txt, vievs) VALUES (?, ?, ?)',
                (t, m, views))
    
    print('Элементы успешно добавлены')
    print('\n')

    con.commit()
    con.close()

def mainmenu():
    while True:
        print('1 Создание таблицы')
        print('2 Информация')
        print('3 Добавление элемента')
        print('4 Поиск элемента по id')
        print('5 Поиск элемента по кол-ву просмотров')
        num = int(input('Введите номер операции '))
        if num == 1:
            create()
        elif num == 2:
            info()
        elif num == 3:
            addelement()
        elif num == 4:
            search()
        elif num == 5:
            searchvievs()
        else:
            print("Введите правильный номер операции ")

def search():
    con = sqlite3.connect('base.db')
    c = con.cursor()
    id = input('Введите ID: ')
    c.execute('SELECT * FROM main WHERE rowid = ?', (id,))
    print('\n')
    result = c.fetchone()
    if result == None:
        print('По данному id ничего не найдено')
    else:
        print('Найдено:', result)
    print('\n')
    con.close()

def searchvievs():
    con = sqlite3.connect('base.db')
    c = con.cursor()
    print('1 Больше')
    print('2 Меньше')
    print('3 Равно')
    while True:
        search = int(input('Введите номер операции '))
        if search == 1:
            na = int(input('Введите число: '))
            print('\n')
            c.execute('SELECT * FROM main WHERE vievs > ?', (na,))
            print(c.fetchall())
            break
        elif search == 2:
            nb = int(input('Введите число: '))
            print('\n')
            c.execute('SELECT * FROM main WHERE vievs < ?', (nb,))
            print(c.fetchall())
            break
        elif search == 3:
            nc = int(input('Введите число: '))
            print('\n')
            c.execute('SELECT * FROM main WHERE vievs = ?', (nc,))
            print(c.fetchall())
            break
        else:
            print('Введите правильный номер')
    print('\n')

if __name__ == '__main__':
    mainmenu()