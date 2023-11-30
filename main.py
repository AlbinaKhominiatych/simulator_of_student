class Group_1012:
    def __init__(self, name, gen, age, evarage_mark): #ініціалізація атрибутів класу
        self.name = name
        self.gen = gen
        self.age = age
        self.evarage_mark = evarage_mark
        self.age += 1
    def study(self):#метод
        print("Гарно вчуся")
        if self.evarage_mark < 12:
            self.evarage_mark += 0.1
        else:
            print("Оцінку немає куди підвищувати")


student1 = Group_1012("Гончарук Олександр", "чол.", 12, 12)#об'єкт, тобто екземпляр класу
student2 = Group_1012("Трофимишин Владислав", "чол", 12, 12)
student3 = Group_1012("Радомська Дарина",  "жін.",  13,  12)
student4 = Group_1012("Коваленко Макар", "чол", 13, 11.1)
student5 = Group_1012("Юраш Максим","чол.", 14, 10)
print("Студента #2 в списку звати ", student2.name)
student1 = Group_1012("Гончарук Олександр", "чол.", 12, 12)
print(student5.age)
student4.study()
student4.study()
student4.study()
print(student4.evarage_mark)
