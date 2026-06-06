import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales_a = [34,65,76,54,66,76]
plt.plot(months,sales_a,marker="o",label = "sales A")
sales_b = [66,45,35,75,88,99]
plt.plot(months,sales_b,marker="o",label = "sales b")
sales_c = [77,23,41,59,60,88]
plt.plot(months,sales_c,marker="o",label = "sales c")
plt.show()
