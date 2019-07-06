from resources.employees import Employees

bobEmployee = Employees(23000,0)

print(bobEmployee.get_gross_salary())
print(bobEmployee.get_nssf())
print(bobEmployee.get_nhif())
print(bobEmployee.get_net_salary())
print(bobEmployee.get_payee())

print('--------------------------------')

ribiroEmployee = Employees(400000, 2000)
print(ribiroEmployee.get_gross_salary())
print(ribiroEmployee.get_nssf())
print(ribiroEmployee.get_nhif())
print(ribiroEmployee.get_net_salary())
print(ribiroEmployee.get_payee())

