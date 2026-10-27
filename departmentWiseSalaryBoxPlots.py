
import matplotlib.pyplot as plt

it_salary = [50000, 55000, 60000, 65000, 70000]
Hr_salary = [35000, 40000, 45000, 50000, 55000]
finance_salary = [45000, 50000, 60000, 70000, 80000]

salary_data = [it_salary, Hr_salary, finance_salary]

plt.figure(figsize=(8, 6))

plt.boxplot(salary_data)
plt.xticks([1, 2, 3], ['IT', 'HR', 'Finance'])

plt.xlabel('Departments')
plt.ylabel('Salary')
plt.title('Department-wise Salary Box Plot')

plt.show()
