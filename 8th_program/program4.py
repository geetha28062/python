import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [500, 650, 600, 800, 950, 1100, 1000]

plt.plot(days, visitors, marker="o", color="purple")

plt.title("Website Visitors")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.grid(True)

plt.savefig("website_visitors.png")
plt.show()
