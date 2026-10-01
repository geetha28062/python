import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 33, 35, 34, 32]

plt.plot(days, temperature, marker="o", color="red")

plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.savefig("weekly_temperature.png")
plt.show()

