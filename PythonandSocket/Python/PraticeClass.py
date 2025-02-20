class Animal :

    def __init__(self , name , age , host_name ):
        self.name = name 
        self.age = age 
        self.host_name = host_name 
        self._var = 10

    def introduction(self):
        print (f"Hello {self.host_name} , I am {self.name } and I {self.age} year old . Nice to meet you ! ")

    
dog = Animal("blue dog" , 2 , "Jim")
dog.introduction()

print(f"Access to var : {dog._var}")
dog._var = 20 
print(f"After change var : {dog._var}")