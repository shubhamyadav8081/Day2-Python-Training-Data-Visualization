import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [1500, 1800, 2200, 2000, 2500, 3000]
plt.plot(months, sales, marker='o', color="blue")
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales trend')
plt.grid(True)
plt.show()