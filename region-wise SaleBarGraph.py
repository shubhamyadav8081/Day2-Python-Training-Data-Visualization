
import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West', 'Central']
sales = [45000, 30000, 40000, 35000, 50000]

plt.figure(figsize=(8, 6))
plt.bar(regions, sales, color='violet')

plt.xlabel('Regions')
plt.ylabel('Sales')
plt.title('Region-wise Sales')
plt.show()
