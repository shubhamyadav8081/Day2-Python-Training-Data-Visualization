
import matplotlib.pyplot as plt

salary = ['55000','20000','80000','7000','99000','40000','60000','10000',
          '60000']

plt.figure(figsize=(8, 6))
plt.hist(salary, bins=5, color='lightblue', edgecolor='black')

plt.xlabel('monthly Salary')
plt.ylabel('Number of Employees')
plt.title('Employee Salary Distribution')

plt.show()
