
import matplotlib.pyplot as plt

categories = ['electronics', 'clothing', 'grocery', 'sports', 'hardware']
sale = [4500, 3000, 700, 3302, 11000]

plt.figure(figsize=(8, 6))
plt.pie(sale, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Product Category Sales Distribution')
plt.show()
