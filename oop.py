class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
         print(f"hello,my name is {self.name} and my age is {self.age}")
person1=person("ulira",18)
person1.say_hello()
person2=person("krack",20)
person2.say_hello()
person3=person("kryss" , 19)
person3.say_hello()
    # create a class called cars with the following attributes
    # make.model and year then create a function that prints make,model and year
    # then create three objects
class cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model=model
        self.year=year
    def my_brands(self):
        print(f"great rides with {self.make}, type {self.model} ,year of manufacture {self.year}")
car1=cars("isuzu ","tata",2018)
car1.my_brands()
car2=cars("toyota","urban cruiser",2022)
car2.my_brands()
car3=cars("isuzu" , "demio" , 2017)
car3.my_brands()
# friends
class friends:
    def __init__(self,name,years):
        self.name=name
        self.years=years
    def my_friends(self):
        print(f"cheers to {self.name} weve been friends for {self.years} years and many more")
fnd1=friends("steve",4)
fnd1.my_friends()
fnd2=friends("kimberly"," 17")
fnd2.my_friends()
fnd3=friends("alex",2)
fnd3.my_friends()
fnd4=friends("mugah",2)
fnd4.my_friends()


