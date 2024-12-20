class Employee():
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary
    def show(self):
      print(self.name + self.salary)
employee1 = Employee('john, ', '67000')
employee1.show()
