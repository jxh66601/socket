import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 8})
x = range(11)
y = range(11)
plt.plot(x, y)


def to_percent(temp, position):
     return '%1.0f' % (10 * temp) + '%'


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

plt.show()