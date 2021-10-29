class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count

    def __str__(self):
        res = "Dog is "
        if not self.angry:
            res += "not "
        res += "angry"
        return res

    def say_gaw(self):
        if self.angry:
            print('GAW-' * (self.count - 1) + 'GAW')
        else:
            print('gaw-' * (self.count - 1) + 'gaw')

    def ping(self):
        # angry - атрибут (?)
        self.angry = True

    def feed(self, food_count):
        if food_count > 10:
            self.angry = False



my_dog = Dog(True, 3) #my_dog - объект класса
my_dog.say_gaw()
my_dog.feed(100)
my_dog.say_gaw()
print(my_dog)

