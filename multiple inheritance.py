class person:
    def walk(self):
        print("Walking")
    def eating(self):
        print("Eating Cookies")
    def sleep(self):
        print("sleeping")
class student:
    def read(self):
        print("Reading")
    def write(self):
        print("writting")
class professional(person,student):
    def work(self):
        print("working")
    def login(self):
        print("Incoming")
    def salary(self):
        print("salary")
p=professional()
p.walk()
p.read()
p.work()
