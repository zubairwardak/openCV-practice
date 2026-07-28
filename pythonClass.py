class mycls:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name } is {self.age} years old"
    
cls = mycls("John", 36)
print(cls)



#  class myclass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# cls = myclass("John", 36)
# print(cls.name)
# print(cls.age)


# class afghan:
#     language = "Pashto"

# af = afghan()
# print(af.language)