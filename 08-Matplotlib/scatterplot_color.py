import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [23,45,67,89,45]
color = ["blue","green","red","yellow","brown"]

plt.scatter(x,y,c=color)
plt.title("Multicolor Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
