import pandas as pd
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_prices.csv')
#linegraph
plt.plot(gas['Year'], gas['USA'], label='USA')
plt.title("Gas Prices")
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend()
plt.show()

#line-graph-style
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,6]

plt.plot(x, y, color='red', linestyle='--', linewidth=2, label='2x')
plt.title("First Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])

plt.legend()
plt.show()

#multi line graph
import pandas as pd
import matplotlib.pyplot as plt
#multi-line-graph
gas = pd.read_csv('gas_prices.csv')

plt.plot(gas['Year'], gas['Italy'], label='Italy')
plt.plot(gas['Year'], gas['Mexico'], label='Mexico')

plt.title("Gas Prices")
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend()
plt.show()

#pie chart 
import matplotlib.pyplot as plt

labels = ['Python','Java','C++','Ruby','JavaScript']
sizes = [215,130,245,210,180]

plt.pie(sizes, labels=labels)
plt.title("Language Usage")

plt.show()


#scatter-plot 
import matplotlib.pyplot as plt

day = [1,2,3,4,5,6,7]
no  = [2,3,1,4,5,3,6]

plt.scatter(day, no)
plt.show()

#scatter-plot style 
import matplotlib.pyplot as plt

day=[1,2,3,4,5,6,7]
no=[2,3,1,4,5,3,6]

plt.scatter(day, no, marker="*", s=200, edgecolor='black')
plt.title("Scatter Plot")
plt.xlabel("Days")
plt.ylabel("Values")
plt.show()

#barplot
import matplotlib.pyplot as plt

labels = ['A','B','C','D']
values = [10,15,7,12]

plt.bar(labels, values)
plt.title("Bar Chart")

plt.show()
