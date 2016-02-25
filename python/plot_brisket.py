import matplotlib.pyplot as plt

# 7.2 pound brisket smoked on 2/7/2016

# times in minutes from start
times = [0,   20,  30,  50,  55,  60,  63,  74,  94,  114, 126, 138, 154, 168, 189, 202]

# temps in degrees read from digital thermometer
temps = [158, 161, 159, 161, 162, 163, 164, 169, 173, 177, 182, 186, 191, 194, 201, 203]
plt.plot(times, temps)

# show the plot
# plt.show()

plt.savefig("plot_brisket.png")
