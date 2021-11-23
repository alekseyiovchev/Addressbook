class Address:

    dict = dict()


    def __init__(self):
        Address.dict = dict()

    def add(self,name,number):
        self.name = input('Введите имя: ')
        self.number = input('Введите номер: ')
        Address.dict[self.name] = self.number

        print('\nКонтакт добавлен/изменен.')
        print('\n',Address.dict)

    def delete(self,name):
        self.name = input('Введите имя: ')
        del Address.dict[self.name]
        
    def edit(self,name):
        self.name = input('Введите имя для изменения контакта: ')
        print()
        del Address.dict[self.name]

    def find(self,name):
        self.name = input('\nВведите имя для поиска: ')
        if self.name in Address.dict:
            print('\nАдресс:', Address.dict[self.name])
        else:
            print('Контакт не найден.')

    

a = Address()
while True:
    print(f'\nВ адресной книге: {len(Address.dict)} контактов\n')
    s = int(input('1. Добавить контакт \n2. Удалить контакт \n3. Изменить контакт \n4. Поиск контакта \n0.Выход \nВведите цифру ---------------> '))
    if s == 1:
        a.add('','')
        continue
    if s == 2:
        a.delete('')
        print('\n',Address.dict)
        continue
    if s == 3:
        a.edit('')
        a.add('','')
        a.write()
        print('Контакт изменен.')
        continue
    if s == 4:
        a.find('')
        break
    if s == 0:
        break
    else:
        print('Неверная цифра.')
        continue