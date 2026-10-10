from animal import Animal, Cat, Dog

my_cat = Cat("Fluffy")
my_dog = Dog("Rex")

neighbours_dog = Dog("Chilly")

my_dog.dog_sees(neighbours_dog)
my_dog.dog_sees(my_cat)