class Book:
    def __init__(self,title, pages , author ):
        self.title = title
        self.pages = pages
        self.author = author
bk = Book("river and the source", 156, "ogolla")
print(bk.title)
print(bk.pages)
print(bk.author)

class Cars:
    def __init__(self , model , year , name):
        self.name = name
        self.model = model
        self.year = year
    def md(self):
        # print(f"{self.name} was realesed in {self.year} and its model is {self.model}")
         print(f"{self.name} was released in {self.year} and its model is {self.model}")
    
details = Cars("impreza", 2012 , "subaru" )

details.md()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
    