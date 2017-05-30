class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary: ", self.salary

if __name__ ==  "__main__":
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni",5000)
    emp1.displayCount()
    emp2.displayEmployee()

    print "Total employee %d" % Employee.empCount