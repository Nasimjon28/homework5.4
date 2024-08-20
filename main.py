from random import choice, randint


class Buiding:
    total = 0
    def __init__(self, name='Объект'):
        """  Инициализация объекта класса  """
        self.name = name
        self.numberOfFloors = randint(1, 100)
        self.buildingType = choice(['кирпичное', 'панельное', 'каменное', 'бревенчатое', 'из соломы'])
        Buiding.total +=1

    def __str__(self):
        """  Вывод всех атрибутов объекта
          Не по заданию, а просто в качестве эксперимента
          Можно не проверять
          Понимаю, что некрасиво и нечитаемо, но все равно работает так как задумывалось )
        """

        # return str(self.__dict__)    эта строка тоже работает, но хотелось переписать по-своему

        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'\nАтрибуты объекта "{self.name}":\n' + ' '.join(list_)


buid_list = [Buiding('Объект №'+str(i)) for i in range(1, 41)]

print(*buid_list)
print('Всего объектов:', Buiding.total)