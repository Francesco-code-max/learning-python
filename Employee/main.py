def showEmployee(name, salary):
    sal = 9000
    if salary == 0:
        salary = sal
    print(name, salary)
    
showEmployee("Kevin", 0)