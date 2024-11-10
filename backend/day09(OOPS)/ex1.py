# class employee(object):
#     name=input("Enter employee name:")
#     Age =int(input("Enter Employee Age:"))
#     Monthly_salary=input("Enter your Monthly Salary:")
#     place=input("Enter your Location:")
# print(f' Name:{employee.name}\n Age{employee.Age}\n Monthly:{employee.Monthly_salary}\n Location:{employee.place}')
# Name: pradeep
# Age28
# Monthly: 80000
# Location: bangaluru
from types import new_class


# class employee(object):
#     name=input("Enter employee name:")
#     Age =int(input("Enter Employee Age:"))
#     Monthly_salary=input("Enter your Monthly Salary:")
#     place=input("Enter your Location:")
# var=[employee.name,
# employee.Age,
# employee.place,
# employee.Monthly_salary]
# print(var)
#
# ['vijay', 21, 'bangaluru', '60000']



class employee(object):
     name=input("Enter employee name:")
     Age =int(input("Enter Employee Age:"))
     Monthly_salary=input("Enter your Monthly Salary:")
     place=input("Enter your Location:")
     print()

print(f"Name:{employee.name}\n Age{employee.Age}\n Monthly:{employee.Monthly_salary}\n Location:{employee.place}")


print(employee.name)
