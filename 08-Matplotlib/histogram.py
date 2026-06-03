import matplotlib.pyplot as plt

scores = [77,56,45,67,69,89,70,90,66,77,88,34,56,14]

plt.hist(scores,bins=5,edgecolor="black")
plt.title("Histogram")
plt.show()
